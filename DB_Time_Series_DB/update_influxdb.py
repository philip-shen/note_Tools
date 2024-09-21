'''
https://github.com/x01963815/grab-stocks-data-to-influxdb/blob/master/update_influxdb.ipynb
'''
'''

更新InfluxDB股價資料庫

請先執行過 init_influxdb.ipynb 檔，本程式預設是抓取分鐘頻率的資料，而 Google Finance 只保留最近15天的分鐘資料，因此要累積資料的話需要至少每15天更新一次資料庫。

InfluxDB 的其中一項優勢是，當匯入的資料點與資料庫中現有的資料重覆時，InfluxDB 會自動忽略重覆的部份，只匯入不重覆的資料點，例如從 Google Finance 抓下來的公司股價是4/1到4/15這段時間的資料，而現有資料庫中的公司股價資料時間是3/1到4/10，InfluxDB 依然可以匯入，並且會自動檢查重覆資料點，並且只更新4/11到4/15的資料。如果4/1到4/10的資料有不一樣的地方，InfluxDB會將兩筆資料皆保留下來，而不會做取代的動作。
執行步驟

    請先從 InfluxData Download 下載 InfluxDB 並解壓縮並至 C:\influxdb
    利用 cmd 至 C:\influxdb> 輸入 influxd 以開啟 InfluxDB server
    執行 init_influxdb.ipynb
    日後更新請執行 update_influxdb.ipynb
'''

# -*- coding: utf-8 -*-
import pandas as pd
import googlefinance.client as gf
import time
from influxdb import DataFrameClient

# 從 Login.txt 中匯入 InfluxDB 登入資料，這邊皆是使用 InfluxDB 預設值
with open('Login.txt', 'r') as loginfile:
    login_info = loginfile.read()
    login_info = login_info.split()
    
    host = login_info[0]      # localhost
    port = int(login_info[1]) # 8086
    user = login_info[2]      # root
    password = login_info[3]  # root

# 資料庫
database = 'taiwan_securities_db'

# 相當於是 SQL 中的 Table
measurement = 'stocks'

client = DataFrameClient(host, port, user, password, database)
client.switch_database(database)

# 匯入 InfluxDB 中現有公司資料名單
stocks_code = client.query('SHOW TAG VALUES ON {0} FROM {1} WITH KEY = "code"'
                           .format(database, measurement))   
stocks_code = pd.DataFrame(stocks_code.get_points())['value'].values

def get_price(company, intervel='60', period='1Y', market='TPE'):
    ''' 使用 googlefinance.client 取得 Google Finance 的價格資料並以 DataFrame
    的型示回傳，index為時間，欄位有 Open、High、Low、Close、Volume，
    
    Parameters
    ----------
    company : string，台灣上市公司代碼，例如：鴻海為'2317'。
    intervel : string，查詢的資料頻率以秒換算，例如：查詢分鐘資料為'60'、。
        查詢日資料為'86400'。
    period : string，查詢期間，'1Y'表示距今 1 年內的資料，'10d'為距今 10 天內資料。
    market : string，目標市場，'TPE'表示台灣市場。
    
    Returns
    ------
    Dataframe    
    '''
    param = {
        'q': company, # Stock symbol (ex: "AAPL")
        'i': intervel,   # Interval size in seconds ("86400" = 1 day intervals)
        'x': market,  # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': period    # Period (Ex: "1Y" = 1 year)
        }
    df = gf.get_price_data(param)
    return df

def update_data_of(company_code):
    '''從 Google Finance 更新資料庫中一家公司股價資料'''
    if company_code not in stocks_code:
        raise KeyError('Company with code \"{0}\" is not in the database.'
                       .format(company_code))
    
    db_data = client.query('SELECT * FROM \"{0}\" WHERE \"code\" = \'{1}\' ' 
                           'ORDER BY \"time\" DESC LIMIT 1'
                           .format(measurement, company_code))[measurement]  
    tags = {'code':db_data.code[0],
            'name':db_data.name[0],
            'industry':db_data.industry[0]}

    company_df = get_price(company_code)
    if company_df.empty:
        print('Company data with code {0} from Google Finance is empty.'
              .format(company_code))
    else:
        client.write_points(company_df, measurement, tags, protocol='json')    
    return

def update_all_data(sleep_time=0.3):
    '''匯入在 InfluxDB 資料庫中全部公司的股價資料'''
    for code in stocks_code:
        update_data_of(code)
        time.sleep(sleep_time)
    return

if __name__ == '__main__':
    update_all_data(0.1)
    
    point_count = client.query('SELECT COUNT("Open") FROM {0}'
                           .format(measurement))[measurement].iloc[0,0]
    print('資料表 {0} 中一共有 {1} 家上市公司，合計 {2} 筆分鐘資料'
          .format(measurement,len(stocks_code),point_count))
    client.close()
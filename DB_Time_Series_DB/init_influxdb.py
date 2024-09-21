'''
https://github.com/x01963815/grab-stocks-data-to-influxdb/blob/master/init_influxdb.ipynb
'''
'''
初始化InfluxDB股價資料庫

本程式會由抓取全台灣911家上市公司的分鐘資料作為 InfluxDB 資料庫的初始資料，執行過一次之後日後的資料更新請執行 update_influxdb.ipynb檔，上市公司的名單資料存在 tw_stocks.pkl 檔中，由 grap_taiwan_stock_list.ipynb 檔案抓取，其中資料來源是由 台灣證券交易所 取得資料上市公司資料。

會將資料儲存至 InfluxDB 的 taiwan_securities_db 資料庫中，並將全部公司的股價資料儲存至 stocks 資料表內，各公司利用 code tag 區分，如需叫出鴻海(2317)的股價資料，請利用 InfluxQL 語法， SELECT * FROM "stocks" WHERE "code"='2317' ，即可。
執行步驟

    請先從 InfluxData Download 下載 InfluxDB 並解壓縮並至 C:\influxdb
    利用 cmd 至 C:\influxdb> 輸入 influxd 以開啟 InfluxDB server
    執行 init_influxdb.ipynb
'''

# -*- coding: utf-8 -*-
import pandas as pd
import googlefinance.client as gf
import time
from influxdb import DataFrameClient



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

def init_data_of(company_code):
    ''' 匯入一家公司的股價資料'''
    tags = {'code':tw_stocks_meta.loc[company_code,'Code'],
            'name':tw_stocks_meta.loc[company_code,'Name'],
            'industry':tw_stocks_meta.loc[company_code,'Industry']}

    company_df = get_price(company_code)
    if company_df.empty:
        print(company_code, ' is empty.')
    else:
        client.write_points(company_df, measurement, tags, protocol='json')    
    return

def init_all_data(sleep_time=0.3):
    '''匯入在 tw_stocks_meta 全部公司的股價資料'''
    for code in tw_stocks_meta.Code:
        init_data_of(code)
        time.sleep(sleep_time)
    return

if __name__ == '__main__':
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
    client.create_database(database)
    client.switch_database(database)

    # 由 tw_stocks.pkl 中匯入台灣上市公司名單 DataFrame ，抓取方式請參考
    # grap_taiwan_stock_list.ipynb 檔。
    tw_stocks_meta = pd.read_pickle('tw_stocks.pkl')

    init_all_data()
    
    point_count = client.query('SELECT COUNT("Open") FROM {0}'
                           .format(measurement))[measurement].iloc[0,0]
    print('資料表 {0} 中一共有 {1} 筆分鐘資料'
          .format(measurement,point_count))
    client.close()

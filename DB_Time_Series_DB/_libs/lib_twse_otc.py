from IPython.core.display import HTML
#from pyquery import PyQuery as pq
import pandas as pd
import scrapy
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
import pickle
import openpyxl, difflib
import yfinance as yf

from .logger_setup import *

"""
本國上市證券國際證券辨識號碼一覽表
https://isin.twse.com.tw/isin/C_public.jsp?strMode=2
本國上櫃證券國際證券辨識號碼一覽表
https://isin.twse.com.tw/isin/C_public.jsp?strMode=4
"""


__all__ = [
    'query_twse_otc_code_00',
    'StockCodeSpider',
    'query_twse_otc_code_01',
    'query_twse_otc_info',
    'query_twse_otc_info_by_pickle',
    'query_twse_otc_idx',
    'dump_pickle',
    'getTWSE',
    'query_twse_otc_code_02',
    
]
"""
[Python] 抓取證券編碼一覽表
https://jerrynest.io/python-twse-stock-list/
"""
def query_twse_otc_code_01(str_url, opt_verbose= 'OFF'):
    #url = "http://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
    res = requests.get(str_url, verify = False)
    soup = BeautifulSoup(res.text, 'html.parser')
    logger.info(soup)
    
    table = soup.find("table", {"class" : "h4"})
    c = 0
    for row in table.find_all("tr"):
        data = []
        for col in row.find_all('td'):
            col.attrs = {}
            data.append(col.text.strip().replace('\u3000', ''))
        
        if len(data) == 1:
            pass # title 股票, 上市認購(售)權證, ...
        else:
            #print(data)
            if opt_verbose.lower() == 'on':
                logger.info(data )

"""
實際數據串接 2023-09-28 
https://ithelp.ithome.com.tw/articles/10329919?sc=rss.iron
"""
"""
         code    name      國際證券辨識號碼         上市日 市場別   產業別     CFI
0        1102      亞泥  TW0001102002  1962/06/08  上市  水泥工業  ESVUFR
1        1103      嘉泥  TW0001103000  1969/11/14  上市  水泥工業  ESVUFR
2        1104      環泥  TW0001104008  1971/02/01  上市  水泥工業  ESVUFR
3        1108      幸福  TW0001108009  1990/06/06  上市  水泥工業  ESVUFR
4        1109      信大  TW0001109007  1991/12/05  上市  水泥工業  ESVUFR
...       ...     ...           ...         ...  ..   ...     ...
36154  01002T  土銀國泰R1  TW00001002T6  2005/10/03  上市        CBCIXU
36155  01004T  土銀富邦R2  TW00001004T2  2006/04/13  上市        CBCIXU
36156  01007T  兆豐國泰R2  TW00001007T5  2006/10/13  上市        CBCIXU
36157  01009T  王道圓滿R1  TW00001009T1  2018/06/21  上市        CBCIXU
36158  01010T  京城樂富R1  TW00001010T9  2018/12/05  上市        CBCIXU

[36159 rows x 7 columns]
"""
"""
6526　達發	TW0006526007	2023/10/19	上市	半導體業	ESVUFR	

6757　台灣虎航-創	TW0006757008	2023/08/15	上市臺灣創新板	航運業	ESVUFR	

0056　元大高股息	TW0000056001	2007/12/26	上市		CEOGEU	
00730　富邦臺灣優質高息	TW0000073006	2018/02/08	上市		CEOIEU
00878　國泰永續高股息	TW0000087808	2020/07/20	上市		CEOJEU	
00919　群益台灣精選高息	TW0000091909	2022/10/20	上市		CEOIEU
"""
"""
Pandas: How to Select Rows Based on Column Values
https://www.statology.org/pandas-select-rows-based-on-column-values/

Method 2: Select Rows where Column Value is in List of Values
df.loc[df['col1'].isin([value1, value2, value3, ...])]
"""

def query_twse_otc_code_02(list_str_url, path_pickle_stock_id, path_csv_stock_id= '', opt_verbose= 'OFF'):
    columns = ['code', 'name', '國際證券辨識號碼', '上市日', '市場別', '產業別', 'CFI']
    
    tds = []        
    for str_url in list_str_url:
        res = requests.get(str_url)
        soup = BeautifulSoup(res.text, "lxml") 
        tr = soup.findAll('tr')

        for raw in tr:
            table = [td.get_text() for td in raw.findAll("td")]
            if len(table) == 7:
                #tds.append(table)
                if "有價證券代號及名稱" not in table[0]:
                    #logger.info(f'table[0]: {table[0]}')        
                    code, name = table[0].split('\u3000')
                    tds.append(dict(zip(columns, [code, name, *table[1: -1]])))

    dict_data=  {}
    data_temp= pd.DataFrame()
    data = pd.DataFrame(tds[1:],columns=tds[0])
    data_temp= data.loc[data['CFI'].isin(['ESVUFR', 'CEOGEU', 'CEOIEU', 'CEOJEU'])].copy()
    data_temp.loc[data_temp['市場別'] == '上市', 'code']= data_temp['code']+'.TW'
    data_temp.loc[data_temp['市場別'] == '上櫃', 'code']= data_temp['code']+'.TWO'
    
    if path_csv_stock_id != "":
        data_temp.to_csv(path_csv_stock_id, index=False) 
    
    dict_data= dict(zip(data_temp.code, data_temp.name))
    list_data= data_temp['code'].values.tolist()
    
    if opt_verbose.lower() == 'on':
        for key, value in dict_data.items():
            logger.info('\n key: {}; value: {}'.format(key, value) )
    
    # save dictionary to pickle file
    with open(path_pickle_stock_id, 'wb') as file:
        #pickle.dump(dict_data, file, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(list_data, file, protocol=pickle.HIGHEST_PROTOCOL)
    
    logger.info(f'data_temp: \n{data_temp}')

"""
07.爬股票代號、產業別 
https://ithelp.ithome.com.tw/articles/10203803
"""

"""
How do I select rows from a DataFrame based on column values?
https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values
"""
"""
How to convert a dataframe to a dictionary
https://stackoverflow.com/questions/18695605/how-to-convert-a-dataframe-to-a-dictionary
"""
"""
Save Python Dictionary to a Pickle File
https://datascienceparichay.com/article/save-python-dictionary-to-a-pickle-file/
"""
"""
How to Convert Pandas Index to a List (With Examples)
https://www.statology.org/pandas-index-to-list/
"""
"""
20240227 query_twse_otc_code_00 can't work
"""
def query_twse_otc_code_00(list_str_url, path_xlsx_stock_id, path_pickle_stock_id, opt_verbose= 'OFF'):
    columns = ['dtype', 'code', 'name', '國際證券辨識號碼', '上市日', '市場別', '產業別', 'CFI']
    
    items = []
    for str_url in list_str_url:
        response_dom = pq(str_url)
        for tr in response_dom('.h4 tr:eq(0)').next_all().items():
            if tr('b'):
                dtype = tr.text()
            else:
                row = [td.text() for td in tr('td').items()]
                code, name = row[0].split('\u3000')
                items.append(dict(zip(columns, [dtype, code, name, *row[1: -1]])))
    
    dict_data=  {}
    data_temp= pd.DataFrame()
    data= pd.DataFrame(items)
    #data.to_excel(path_xlsx_stock_id, sheet_name='twse_otc_id', index=False, header=True)
    data_temp= data.loc[data['dtype'] == '股票'].copy()
    data_temp= data_temp[['code', 'name', '國際證券辨識號碼', '市場別']].copy()
    data_temp.loc[data_temp['市場別'] == '上市', 'code']= data_temp['code']+'.TW'
    data_temp.loc[data_temp['市場別'] == '上櫃', 'code']= data_temp['code']+'.TWO'
    data_temp.to_excel(path_xlsx_stock_id, sheet_name='twse_otc_id', index=False, header=True)
    dict_data= dict(zip(data_temp.code, data_temp.name))
    list_data= data_temp['code'].values.tolist()

    if opt_verbose.lower() == 'on':
        for key, value in dict_data.items():
            logger.info('\n key: {}; value: {}'.format(key, value) )
    
    # save dictionary to pickle file
    with open(path_pickle_stock_id, 'wb') as file:
        #pickle.dump(dict_data, file, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(list_data, file, protocol=pickle.HIGHEST_PROTOCOL)
    
    #data_temp.to_pickle(path_pickle_stock_id)

    HTML(data.head().to_html())

class StockCodeSpider(scrapy.Spider):
    str_twse_url= 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
    str_tpex_url = 'http://isin.twse.com.tw/isin/C_public.jsp?strMode=4'
    name = 'stock_code'
    start_urls = [str_twse_url, str_tpex_url]

    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'CONCURRENT_REQUESTS': 1,
        'MONGODB_COLLECTION': name,
        'MONGODB_ITEM_CACHE': 1000,
        'MONGODB_DROP': True
    }

    def parse(self, response):
        for tr in response.dom('.h4 tr:eq(0)').next_all().items():
            if tr('b'):
                dtype = tr.text()
            else:
                row = [td.text() for td in tr('td').items()]
                code, name = row[0].split('\u3000')
                yield dict(zip(columns, [dtype, code, name, *row[1: -1]]))

    
"""
Python 擷取上市櫃公司名稱與代號及股利資訊
Apr 22, 2020
https://medium.com/phelps-laboratory/%E6%93%B7%E5%8F%96%E4%B8%8A%E5%B8%82%E6%AB%83%E5%85%AC%E5%8F%B8%E5%90%8D%E7%A8%B1%E8%88%87%E4%BB%A3%E8%99%9F%E5%8F%8A%E8%82%A1%E5%88%A9%E8%B3%87%E8%A8%8A-afe6b31f9c46
"""

def getTWSE(str_url, path_stock_id):
    # read_html
    twsedf = pd.read_html(str_url, encoding="Big5")
    logger.info(f"twsedf: {twsedf}")   
    # open file
    fp = open(path_stock_id, "a")

    for str in twsedf[0][0]:
        encodeStr = str.encode('utf-8')
        strArray = encodeStr.split(' ')
        if len(strArray) == 2:
            print(strArray[0], strArray[1])
            # write to output file
            if len(strArray[0]) == 4:
                fp.writelines(strArray[0] + " " + strArray[1] + "\n")

    fp.close()

"""
Python — 透過Yahoo Finance API抓取台股歷史
https://aronhack.medium.com/python-%E9%80%8F%E9%81%8Eyahoo-finance-api%E6%8A%93%E5%8F%96%E5%8F%B0%E8%82%A1%E6%AD%B7%E5%8F%B2%E8%B3%87%E6%96%99-a97feb373e8f            
"""
        
def twse_idx():
    link = 'https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e'
    r = requests.get(link)
    data = pd.DataFrame(r.json())
    
    data.to_csv('./data' + '/stock_id.csv', index=False, header = True)

"""
爬取台股清單並且寫入 Datebase
May 10, 2021
https://medium.com/%E5%B7%A5%E7%A8%8B%E9%9A%A8%E5%AF%AB%E7%AD%86%E8%A8%98/%E7%88%AC%E5%8F%96%E5%8F%B0%E8%82%A1%E6%B8%85%E5%96%AE%E4%B8%A6%E4%B8%94%E5%AF%AB%E5%85%A5-datebase-87c6d3f1348b
"""
def twse_otc_idx(str_url, opt_verbose='OFF'):
    # 抓取股票資訊
    #url = "https://histock.tw/stock/rank.aspx?p=all"
    user_agent = UserAgent()
    headers = {'user-agent': user_agent.random}

    # 獲取 html 資訊
    res = requests.get(str_url, headers = headers)
    
    tmp = BeautifulSoup(res.text, 'lxml').select_one('#CPHB1_gv')
    df = pd.read_html(tmp.prettify())[0]
    # 優化一下欄位名稱
    df.columns = ['stock_no', 'stock_name', 'price', 'ud', 'udp', 'ud_w', 'amp','open', 'high', 'low', 'price_y', 'vol', 'vol_p']
    # 新增欄位註記資料更新時間
    df["etl_date"] = datetime.now()

    return df

class Asset:
    """Class to initialize the stock, given a ticker, period and interval"""
    def __init__(self, ticker, period='1y', interval='1d'):
        self.ticker = ticker.upper()
        self.period = period
        self.interval = interval

    def __repr__(self):
        return f"Ticker: {self.ticker}, Period: {self.period}, Interval: {self.interval}"

    def get_info(self):
        """Uses yfinance to get information about the ticker
        returns a dictionary filled with at-point information about the ticker"""
        ticker_info = yf.Ticker(self.ticker).info
        return ticker_info

    def get_data(self):
        """Uses yfinance to get data, returns a Pandas DataFrame object
        Index: Date
        Columns: Open, High, Low, Close, Adj Close, Volume
        """
        try:
            self.data = yf.download(
                tickers=self.ticker,
                period=self.period,
                interval=self.interval)
            return self.data
        except Exception as e:
            return e

def query_twse_otc_info(ticker, period='1y', interval='1d', opt_verbose='OFF'):
    asset = Asset(ticker, period, interval)
    asset_info = asset.get_info()  # Information about the Company
    asset_df = asset.get_data()    # Historical price data
    
    # Check in terminal for n_clicks and status
    print('asset_df: {}'.format(asset_df))

def query_twse_otc_info_by_pickle(path_pickle_tickers, period='1y', interval='1d', opt_verbose='OFF'):
    with open(path_pickle_tickers, "rb") as f:
        list_ticker= pickle.load(f)
    
    for ticker in list_ticker:
        asset = Asset(ticker, period, interval)
        asset_info = asset.get_info()  # Information about the Company
        asset_df = asset.get_data()    # Historical price data
    
        # Check in terminal for n_clicks and status
        #print('asset_df: {}'.format(asset_df))
        logger.info( '\n ticker: {}'.format(ticker) )
        logger.info( 'asset_df: \n {}'.format(asset_df) )
"""
PythonでExcel操作（読み込み編）
https://qiita.com/adgjmptw0/items/e21bef0e773fc0e3e47f

PythonでExcel操作（読み書き編集編）
https://qiita.com/adgjmptw0/items/afbf2a0c26e993249ae2
"""
"""
Python - difference between two strings
https://stackoverflow.com/questions/17904097/python-difference-between-two-strings
"""
def query_twse_otc_idx(path_xlsx, path_pickle, opt_verbose='OFF'):
    wb = openpyxl.load_workbook(path_xlsx)

    ws= wb["Sheet1"]
    list_value= []
    dict_value_ticker, list_twse_otc_ticker= {}, []

    for row in ws.iter_rows(min_row=2, min_col=2, max_row=130, max_col=2):        
        for c in row:
            if str(c.value).lower() != 'none':list_value.append(c.value) 
        
    with open(path_pickle, "rb") as f:
        list_ticker = pickle.load(f)

    for value in list_value:
        for ticker in list_ticker:
            output_list = [li for li in difflib.ndiff(str(value), str(ticker)) if li[0] != ' ']
            if output_list== ['+ .', '+ T', '+ W'] or output_list== ['+ .', '+ T', '+ W', '+ O']:
                
                if opt_verbose.lower() == 'on':
                    logger.info('value: {}; ticker: {}'.format(value, ticker) )
                
                dict_value_ticker.update( {'{}'.format(value): '{}'.format(ticker)} )
                list_twse_otc_ticker.append(ticker)

    if opt_verbose.lower() == 'on':
        logger.info('list_value: {}'.format(list_value) )
        
        for ticker in list_ticker:
            logger.info('ticker: {}'.format(ticker))
    
    return dict_value_ticker, list_twse_otc_ticker

def dump_pickle(path_pickle, out_pickle_cont, opt_verbose='OFF'):
    with open(path_pickle, 'wb') as f:
        pickle.dump(out_pickle_cont, f)

    with open(path_pickle, 'rb') as f:
        new_pickle_cont = pickle.load(f)

    if opt_verbose.lower() == 'on':
        logger.info('\n output_pickle: {}'.format(path_pickle) )
        logger.info('\n new_pickle_cont: {}'.format(new_pickle_cont) )
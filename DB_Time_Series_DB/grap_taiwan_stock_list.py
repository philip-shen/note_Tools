'''
https://github.com/x01963815/grab-stocks-data-to-influxdb/blob/master/grap_taiwan_stock_list.ipynb
'''
import pandas as pd
'''從 台灣證券交易所 取得資料
首頁 > 產品與服務 > 證券編碼 > 證券編碼公告 > 本國上市證券國際證券辨識號碼一覽表'''
data = pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2')

tw_list = data[0]
tw_stocks = tw_list.loc[:tw_list[tw_list[0]=='上市認購(售)權證'].index.values[0]-1]
tw_stocks = tw_stocks.drop([0,1])
tw_stocks.columns = ['Code_Name', 'ISIN', 'ListedDate', 'Market', 'Industry', 'CFI', 'Note']
tw_stocks = tw_stocks.reset_index(drop=True)
tw_stocks['Code'] = tw_stocks.Code_Name.str.split('　').str.get(0) # 4148 全宇生技-KY 有問題
tw_stocks['Name'] = tw_stocks.Code_Name.str.split('　').str.get(1)
tw_stocks.index = tw_stocks.Code

tw_stocks.loc['2353','Name'] = '宏碁'
tw_stocks.loc['6285','Name'] = '啟碁'
tw_stocks.loc['3046','Name'] = '建碁'

tw_stocks.to_pickle('tw_stocks.pkl')

#### for ETF  
ETFlist = pd.read_html('http://md.jsun.com/event/jsun_school/ETF_stock09.html')
ETFlist[0]

ETFlist = ETFlist.iloc[:-1]
ETFlist.index.name = 'Code'
ETFlist

ETFlist.columns = ['Name', 'Type', 'TargetIndex']
ETFlist
'''
Name 	Type 	TargetIndex
Code 			
0050 	元大台灣50 	國內成分證券ETF 	臺灣50指數
0051 	元大中型100 	國內成分證券ETF 	臺灣中型100指數
0053 	元大電子 	國內成分證券ETF 	電子類加權股價指數
0054 	元大台商50 	國內成分證券ETF 	S&P台商收成指數
0055 	元大MSCI金融 	國內成分證券ETF 	MSCI台灣金融指數
0056 	元大高股息 	國內成分證券ETF 	臺灣高股息指數
006201 	元大富櫃50 	國內成分證券ETF 	富櫃五十指數
006203 	元大MSCI台灣 	國內成分證券ETF 	MSCI®臺灣指數
00631L 	元大台灣50正2 	槓桿型ETF 	臺灣50指數
00632R 	元大台灣50反1 	反向型ETF 	臺灣50指數
0052 	FB科技 	國內成分證券ETF 	臺灣資訊科技指數
0057 	FB摩台 	國內成分證券ETF 	MSCI®臺灣指數
0058 	FB發達 	國內成分證券ETF 	臺灣發達指數
0059 	FB金融 	國內成分證券ETF 	金融保險類股指數
006208 	FB台50 	國內成分證券ETF 	臺灣50指數
006204 	永豐臺灣加權 	國內成分證券ET 	臺灣證券交易所發行量加權股價指數
00663L 	國泰臺灣加權正2 	槓桿型ETF 	臺灣日報酬兩倍指數
006204 	永豐臺灣加權 	國內成分證券ET 	臺灣證券交易所發行量加權股價指數
'''
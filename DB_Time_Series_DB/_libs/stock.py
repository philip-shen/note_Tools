from _libs.logger_setup import *

import asyncio
from pstock import Bars, BarsMulti

'''
To get Bars there are a couple of arguments that can be specified:

    interval: one of 1m, 2m, 5m, 15m, 30m, 1h, 1d, 5d, 1mo, 3mo, defaults to None
    period: one of 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max, defaults to None
    start: Any date/datetime supported by pydnatic, defaults to None
    end: Any date/datetime supported by pydnatic, defaults to None
    events: one of div, split, div,splits, defaults to div,splits
    include_prepost: Bool, include Pre and Post market bars, default to False

'''
'''
INFO: HTTP Request: GET https://query2.finance.yahoo.com/v8/finance/chart/2330.TW?interval=1h&events=div%2Csplits&includePrePost=false&period1=1717372800&period2=1726790400 "HTTP/1.1 200 OK"
INFO: ticker: 2330.TW; stock name: 台積電
INFO: bars.df:
                         date   open   high    low  close  adj_close     volume        interval
0   2024-06-03 01:00:00+00:00  839.0  847.0  837.0  847.0      847.0        0.0 0 days 01:00:00
1   2024-06-03 02:00:00+00:00  847.0  853.0  846.0  852.0      852.0  5924046.0 0 days 01:00:00
2   2024-06-03 03:00:00+00:00  853.0  853.0  850.0  851.0      851.0  2344066.0 0 days 01:00:00
3   2024-06-03 04:00:00+00:00  851.0  851.0  848.0  849.0      849.0  3034463.0 0 days 01:00:00
4   2024-06-03 05:00:00+00:00  849.0  852.0  849.0  850.0      850.0  2087760.0 0 days 01:00:00
..                        ...    ...    ...    ...    ...        ...        ...             ...
371 2024-09-19 02:00:00+00:00  938.0  950.0  938.0  949.0      949.0  7523344.0 0 days 01:00:00
372 2024-09-19 03:00:00+00:00  950.0  952.0  947.0  952.0      952.0  6381810.0 0 days 01:00:00
373 2024-09-19 04:00:00+00:00  952.0  952.0  949.0  952.0      952.0  4122869.0 0 days 01:00:00
374 2024-09-19 05:00:00+00:00  951.0  955.0  951.0  955.0      955.0  4916511.0 0 days 01:00:00
375 2024-09-19 05:30:00+00:00  960.0  960.0  960.0  960.0      960.0        0.0 0 days 01:00:00
'''

class stock_indicator_pstock:
    def __init__(self, ticker, startdate, enddate, period='1y', interval='1d', opt_verbose='OFF'):
        self.stock_ticker = ticker.upper()
        self.opt_verbose = opt_verbose
        self.interval = interval
        self.period = period
        self.startdate = startdate
        self.enddate = enddate
            
    def pstock_interval_period(self):
        # initialize Asset object 
        try:
            bars = asyncio.run(Bars.get(self.stock_ticker, period=self.period, interval=self.interval))
            self.stock_data = bars.df.copy()
            self.stock_data.reset_index(inplace=True)
        except Exception as e:
            logger.info(f'Error: {e}')
            exit(0)
    
    def pstock_interval_startdate_enddate(self):
        # initialize Asset object 
        try:
            bars = asyncio.run(Bars.get(self.stock_ticker, start=self.startdate, end=self.enddate, interval=self.interval))
            self.stock_data = bars.df.copy()
            self.stock_data.reset_index(inplace=True)
        except Exception as e:
            logger.info(f'Error: {e}')
            exit(0)
                    
    # 移動平均線を計算する関数
    def calculate_moving_averages(self, weekly_window=5, Dweekly_window=10, \
                                    monthly_window=20, quarterly_window=60):
        self.stock_data['MA_5'] = self.stock_data['close'].rolling(window=weekly_window).mean()
        self.stock_data['MA_10'] = self.stock_data['close'].rolling(window=Dweekly_window).mean()
        self.stock_data['MA_20'] = self.stock_data['close'].rolling(window=monthly_window).mean()
        self.stock_data['MA_60'] = self.stock_data['close'].rolling(window=quarterly_window).mean()
        #return data

    def calculate_exponential_moving_averages(self, weekly_window=5, Dweekly_window=10, \
                                    monthly_window=20, quarterly_window=60):
        self.stock_data['EMA_5'] = self.stock_data['close'].ewm(ignore_na=False, span=weekly_window, min_periods=0, adjust=False).mean()
        self.stock_data['EMA_10'] = self.stock_data['close'].ewm(ignore_na=False, span=Dweekly_window, min_periods=0, adjust=False).mean()
        self.stock_data['EMA_20'] = self.stock_data['close'].ewm(ignore_na=False, span=monthly_window, min_periods=0, adjust=False).mean()
        self.stock_data['EMA_60'] = self.stock_data['close'].ewm(ignore_na=False, span=quarterly_window, min_periods=0, adjust=False).mean()
    
    # ボリンジャーバンドを計算する関数
    def calculate_bollinger_bands(self, window=20):
        sma = self.stock_data['close'].rolling(window=window).mean()
        std = self.stock_data['close'].rolling(window=window).std()
        self.stock_data['Bollinger Middle'] = sma
        self.stock_data['Bollinger Upper'] = sma + (std * 2)
        self.stock_data['Bollinger Lower'] = sma - (std * 2)
        
'''
株価の投入
https://qiita.com/ixtlan001/items/c87e4b2c4a97d7dba800#%E6%A0%AA%E4%BE%A1%E3%81%AE%E6%8A%95%E5%85%A5
'''
import os, sys, time
import pandas as pd
import argparse
#import pandas_datareader.data as web
from datetime import datetime

from influxdb_client import InfluxDBClient, BucketRetentionRules, WriteOptions
from influxdb_client.client.write_api import PointSettings

# Bollinger Band, SMA(simple moving average)を計算して追加
#import talib

import _libs.lib_misc as lib_misc
from _libs.logger_setup import *
from _libs.lib_twse_otc import *
from _libs.stock import *

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.3f} seconds.'
    logger.info(msg)

def write_dataframe(client, bucket, df, point_settings):
        
        with client.write_api(write_options=WriteOptions(batch_size=1000, flush_interval=30_000, jitter_interval=10_000, retry_interval=30_000), point_settings=point_settings) as write_api:

            write_api.write(bucket=bucket, record=df,
                data_frame_tag_columns=['retrieved from', 'inject time', 'SYMBOL', 'name'],
                data_frame_measurement_name="stock prices")

if __name__ == '__main__':
    INFLUXDB_TOKEN = '（上記のAPI TOKENをここにコピペ）'
    URL    = "http://influxdb:8086" # "influxdb"はdocker-compose.ymlのcontainer_nameで指定した名前。
    ORG    = "myorg"                # InfluxDB初期設定で指定した組織名
    BUCKET = 'influxdb-test'        # 任意のBUCKET名

    start_date = datetime(2000,1,1)
    end_date  = datetime(2024,1,1)
    
    '''
    # Bucketの生成
    #https://github.com/influxdata/influxdb-client-python/blob/master/influxdb_client/domain/bucket_retention_rules.py
    '''
    with InfluxDBClient(url=URL, token=INFLUXDB_TOKEN) as client:
        buckets_api = client.buckets_api()
        retention_rules = BucketRetentionRules(type="expire", every_seconds=0, shard_group_duration_seconds=3600*24*365*10) # every_seconds = 0 means infinite
        created_bucket = buckets_api.create_bucket(bucket_name=BUCKET,
                                                   retention_rules=retention_rules,
                                                   org=ORG)
        print(created_bucket)

    #株価をyahoo financeからダウンロード(例としてfordとGE)
    #Tesla, Inc. (TSLA)
    target_ticker = 'TSLA'
    local_stock_indicator_TSLA = stock_indicator_pstock(ticker=target_ticker, interval="1d", \
                                                                startdate= start_date, enddate= end_date)
    local_stock_indicator_TSLA.pstock_interval_startdate_enddate()
    #NVIDIA Corporation (NVDA)            
    target_ticker = 'NVDA'
    local_stock_indicator_NVDA = stock_indicator_pstock(ticker=target_ticker, interval="1d", \
                                                                startdate= start_date, enddate= end_date)
    local_stock_indicator_NVDA.pstock_interval_startdate_enddate()
    
    #ford = web.DataReader('F', 'yahoo', start=start, end=end)
    #GE = web.DataReader('GE', 'yahoo', start=start, end=end)

    #後にGrafanaでのローソク足表示の際にすんなり認識される様に列名を変更
    #また、調整済みcloseの値（Adj close）をcloseとする
    #ford.columns = ["high", "low", "open", "close.raw", "volume", "close"]
    #GE.columns =  ["high", "low", "open", "close.raw", "volume", "close"]

    #タイムスタンプを米国東部時間でのNasdaqとNYSEのOpen時間（午前9:30）に設定

    #ford.index = ford.index.tz_localize(tz='US/Eastern')+pd.DateOffset(hours=9.5)
    #ford.index = ford.index.tz_convert(tz='UTC')

    #GE.index = GE.index.tz_localize(tz='US/Eastern')+pd.DateOffset(hours=9.5)
    #GE.index = GE.index.tz_convert(tz='UTC')

    timeperiod = 20
    
    local_stock_indicator_TSLA.calculate_bollinger_bands(window= timeperiod)
    upper, middle, lower = local_stock_indicator_TSLA.stock_data['Bollinger Upper'], \
                            local_stock_indicator_TSLA.stock_data['Bollinger Middle'], \
                            local_stock_indicator_TSLA.stock_data['Bollinger Lower']    
    SMA = local_stock_indicator_TSLA.stock_data['MA_20']
    tsla = pd.concat([local_stock_indicator_TSLA.stock_data, upper.rename('Upper Bollinger Band'), \
                        middle.rename('Middle Bollinger Band'), lower.rename('Lower Bollinger Band'), SMA.rename('SMA')], axis=1)
    
    local_stock_indicator_NVDA.calculate_bollinger_bands(window= timeperiod)
    upper, middle, lower = local_stock_indicator_NVDA.stock_data['Bollinger Upper'], \
                            local_stock_indicator_NVDA.stock_data['Bollinger Middle'], \
                            local_stock_indicator_NVDA.stock_data['Bollinger Lower']    
    SMA = local_stock_indicator_NVDA.stock_data['MA_20']                        
    nvda = pd.concat([local_stock_indicator_NVDA.stock_data, upper.rename('Upper Bollinger Band'), \
                        middle.rename('Middle Bollinger Band'), lower.rename('Lower Bollinger Band'), SMA.rename('SMA')], axis=1)
    
    # 株価を投入   
    client = InfluxDBClient(url=URL, token=INFLUXDB_TOKEN, org=ORG, timeout=30_000)

    # Tsla株価投入
    point_settings = PointSettings(**{"retrieved from" : "yahoo finance", "inject time": str(datetime.now()), \
                                        "SYMBOL" : "TSLA", "NAME" : "Tesla, Inc.", "transform" : "original"})
    write_dataframe(client, BUCKET, tsla, point_settings)

    # NVIDIA株価投入
    point_settings = PointSettings(**{"retrieved from" : "yahoo finance", "inject time": str(datetime.now()), \
                                        "SYMBOL" : "NVDA", "NAME" : "NVIDIA Corporation", "transform" : "original"})
    write_dataframe(client, BUCKET, nvda, point_settings)
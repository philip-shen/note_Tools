'''
株価の投入
https://qiita.com/ixtlan001/items/c87e4b2c4a97d7dba800#%E6%A0%AA%E4%BE%A1%E3%81%AE%E6%8A%95%E5%85%A5
'''
import os, sys, time
import pandas as pd
import argparse
#import pandas_datareader.data as web
from datetime import datetime
import pathlib
import json, pickle

from influxdb_client import InfluxDBClient, BucketRetentionRules, WriteOptions
from influxdb_client.client.write_api import PointSettings

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
   #instantiate the WriteAPI        
   with client.write_api(write_options=WriteOptions(batch_size=1000, flush_interval=30_000, jitter_interval=10_000, retry_interval=30_000), 
                         point_settings=point_settings) as write_api:
        write_api.write(bucket=bucket, 
                        record=df,
                        data_frame_tag_columns=['retrieved from', 'inject time', 'SYMBOL', 'name'],
                        data_frame_measurement_name="stock prices")

def query_influxdb(client, org, query):
    #instantiate the WriteAPI and QueryAPI
     #return the table and print the result
    result = client.query_api().query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_value(), record.get_field()))
    
    logger.info(f'results: {results}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stock indicator')
    parser.add_argument('--conf_json', type=str, default='config.json', help='Config json')
    
    args = parser.parse_args()

    logger_set(strdirname)
    
    # Get present time
    t0 = time.time()
    local_time = time.localtime(t0)
    msg = 'Start Time is {}/{}/{} {}:{}:{}'
    logger.info(msg.format( local_time.tm_year,local_time.tm_mon,local_time.tm_mday,\
                            local_time.tm_hour,local_time.tm_min,local_time.tm_sec))
    
    json_file= args.conf_json
    
    json_path_file = pathlib.Path(strdirname)/json_file
    
    if (not os.path.isfile(json_file))  :
        msg = 'Please check json file:{}  if exist!!! '
        logger.info(msg.format(json_file) )    
        est_timer(t0)
        sys.exit()

    with open(json_file, encoding="utf-8") as f:
        json_data = json.load(f)  
        
    opt_verbose= 'OFF'

    INFLUXDB_TOKEN = json_data["INFLUXDB_TOKEN"]
    URL    = json_data["URL"] # "influxdb"はdocker-compose.ymlのcontainer_nameで指定した名前。
    ORG    = json_data["ORG"]       # InfluxDB初期設定で指定した組織名
    BUCKET = json_data["BUCKET"]        # 任意のBUCKET名

    start_date = datetime(2012,1,1)
    end_date  = datetime(2024,9,24)    
    
    #株価をyahoo financeからダウンロード(例としてfordとGE)
    #Tesla, Inc. (TSLA)
    tsla_ticker = 'TSLA'
    local_stock_indicator_TSLA = stock_indicator_pstock(ticker=tsla_ticker, interval="1d", \
                                                                startdate= start_date, enddate= end_date)
    local_stock_indicator_TSLA.pstock_interval_startdate_enddate()
    #NVIDIA Corporation (NVDA)            
    nvda_ticker = 'NVDA'
    local_stock_indicator_NVDA = stock_indicator_pstock(ticker=nvda_ticker, interval="1d", \
                                                                startdate= start_date, enddate= end_date)
    local_stock_indicator_NVDA.pstock_interval_startdate_enddate()
        
    #後にGrafanaでのローソク足表示の際にすんなり認識される様に列名を変更
    #また、調整済みcloseの値（Adj close）をcloseとする
    #ford.columns = ["high", "low", "open", "close.raw", "volume", "close"]
    #GE.columns =  ["high", "low", "open", "close.raw", "volume", "close"]

    '''
    # Bucketの生成
    #https://github.com/influxdata/influxdb-client-python/blob/master/influxdb_client/domain/bucket_retention_rules.py
    '''
    '''
    Reason: Unauthorized
    HTTP response headers: HTTPHeaderDict({'Content-Type': 'application/json; charset=utf-8', 'X-Influxdb-Build': 'OSS', 'X-Influxdb-Version': 'v2.7.10', 'X-Platform-Error-Code': 'unauthorized', 'Date': 'Sun, 22 Sep 2024 16:46:09 GMT', 'Content-Length': '55'})
    HTTP response body: {"code":"unauthorized","message":"unauthorized access"}
    '''
    '''
    getting {"code":"unauthorized","message":"unauthorized access"} after using "query" http api for InfluxDB 2.0

    https://stackoverflow.com/questions/69771271/getting-codeunauthorized-messageunauthorized-access-after-using-que
    '''
    '''
    HTTP response body: {
	"code": "conflict",
	"message": "bucket with name my-bucket already exists"
    }
    using another new bucket name
    '''
    with InfluxDBClient(url=URL, token=INFLUXDB_TOKEN) as client:
        buckets_api = client.buckets_api()
    #    retention_rules = BucketRetentionRules(type="expire", every_seconds=0, shard_group_duration_seconds=3600*24*365*10) # every_seconds = 0 means infinite
    #    created_bucket = buckets_api.create_bucket(bucket_name=BUCKET,
    #                                               retention_rules=retention_rules, org=ORG)
    #    logger.info(f"created_bucket: {created_bucket}")

    
    # Bollinger Band, SMA(simple moving average)を計算して追加
    timeperiod = 20
    
    '''
    Cannot convert timezone for a timestamp in pandas Jul 21, 2022    
    https://stackoverflow.com/questions/73064425/cannot-convert-timezone-for-a-timestamp-in-pandas
    '''
    #タイムスタンプを米国東部時間でのNasdaqとNYSEのOpen時間（午前9:30）に設定
    #tsla = tsla.tz_localize(tz='US/Eastern')+pd.DateOffset(hours=9.5)
    
    #if input is DataFrame with column 0
    local_stock_indicator_TSLA.stock_data['date'] = local_stock_indicator_TSLA.stock_data['date'].dt.tz_localize(tz='US/Eastern').\
                                            dt.tz_convert(tz='UTC')
    # remove column 'interval' for insert data
    local_stock_indicator_TSLA.stock_data.drop(['interval'], axis=1, inplace=True)

    logger.info(f'TSLA.stock_data:\n{local_stock_indicator_TSLA.stock_data}')
    
    local_stock_indicator_TSLA.calculate_bollinger_bands(window= timeperiod)
    local_stock_indicator_TSLA.calculate_moving_averages()
    tsla = local_stock_indicator_TSLA.stock_data.rename(columns={'Bollinger Upper': 'Upper Bollinger Band',
                                                                 'Bollinger Middle': 'Middle Bollinger Band',
                                                                 'Bollinger Lower': 'Lower Bollinger Band',
                                                                 'MA_20': 'SMA'})
    logger.info(f'tsla:\n{tsla}')
        
    local_stock_indicator_NVDA.calculate_bollinger_bands(window= timeperiod)
    local_stock_indicator_NVDA.calculate_moving_averages()
    
    local_stock_indicator_NVDA.stock_data['date'] = local_stock_indicator_NVDA.stock_data['date'].dt.tz_localize(tz='US/Eastern').\
                                            dt.tz_convert(tz='UTC')
    #タイムスタンプを米国東部時間でのNasdaqとNYSEのOpen時間（午前9:30）に設定
    #nvda = nvda.tz_localize(tz='US/Eastern')+pd.DateOffset(hours=9.5)
    
    # remove column 'interval' for insert data
    local_stock_indicator_NVDA.stock_data.drop(['interval'], axis=1, inplace=True)
    logger.info(f'NVDA.stock_data:\n{local_stock_indicator_NVDA.stock_data}')
    
    nvda = local_stock_indicator_NVDA.stock_data.rename(columns={'Bollinger Upper': 'Upper Bollinger Band',
                                                                 'Bollinger Middle': 'Middle Bollinger Band',
                                                                 'Bollinger Lower': 'Lower Bollinger Band',
                                                                 'MA_20': 'SMA'})
    logger.info(f'nvda:\n{nvda}')
        
    
    # 株価を投入   
    client = InfluxDBClient(url=URL, token=INFLUXDB_TOKEN, org=ORG, timeout=30_000)

    # Tsla株価投入
    point_settings = PointSettings(**{"retrieved from" : "yahoo finance", 
                                      "inject time": str(datetime.now()), \
                                    "SYMBOL" : "TSLA", "NAME" : "Tesla, Inc.", "transform" : "original"})
    write_dataframe(client, BUCKET, tsla, point_settings)

    # NVIDIA株価投入
    point_settings = PointSettings(**{"retrieved from" : "yahoo finance", 
                                      "inject time": str(datetime.now()), \
                                    "SYMBOL" : "NVDA", "NAME" : "NVIDIA Corporation", "transform" : "original"})
    write_dataframe(client, BUCKET, nvda, point_settings)

    est_timer(t0)
    
    # Get present time
    t0 = time.time()    
    query = f'from(bucket: "{BUCKET}") \
    |> range(start: -10y)\
    |> filter(fn: (r) => r["_measurement"] == "stock prices")\
    |> filter(fn: (r) => r["NAME"] == "NVIDIA Corporation")\
    |> filter(fn: (r) => r["SYMBOL"] == "{nvda_ticker}")\
    |> filter(fn: (r) => r["_field"] == "open")\
    |> last()'
    
    logger.info(f'query: {query}')
    query_influxdb(client, ORG, query)

    est_timer(t0)

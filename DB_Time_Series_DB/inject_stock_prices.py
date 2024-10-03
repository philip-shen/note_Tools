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
from _libs.lib_db import *

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.3f} seconds.'
    logger.info(msg)


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
    end_date  = datetime(2024,10,4)    
    measurement_name="stock_prices"
    measurement_name_bb_band="stock_prices_bb_band"
    # Influxdb client
    client = InfluxDBClient(url=URL, token=INFLUXDB_TOKEN, org=ORG, timeout=30_000)
    
    #Delete measurement
    delete_measurement(client, 
                       startdate='2012-01-03T05:00:00Z', 
                       stopdate='2024-10-01T04:00:00Z',
                       measurement= measurement_name, bucket=BUCKET, organization= ORG)
    logger.info(f'Delete measurement: {measurement_name}')

    delete_measurement(client, 
                       startdate='2012-01-03T05:00:00Z', 
                       stopdate='2024-10-01T04:00:00Z',
                       measurement= measurement_name_bb_band, bucket=BUCKET, organization= ORG)
    logger.info(f'Delete measurement: {measurement_name_bb_band}')

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
    # Bollinger Band, SMA(simple moving average)を計算して追加
    timeperiod = 20
    
    '''
    Cannot convert timezone for a timestamp in pandas Jul 21, 2022    
    https://stackoverflow.com/questions/73064425/cannot-convert-timezone-for-a-timestamp-in-pandas
    '''
    
    logger.info(f'TSLA.stock_data:\n{local_stock_indicator_TSLA.stock_data}')
    
    local_stock_indicator_TSLA.calculate_moving_averages()
    tsla = local_stock_indicator_TSLA.stock_data
    tsla = df_datetime_toUTC_drop_interval(tsla)

    local_stock_indicator_TSLA.pstock_interval_startdate_enddate()
    local_stock_indicator_TSLA.calculate_bollinger_bands(window= timeperiod)
    tsla_bb_band = local_stock_indicator_TSLA.stock_data.rename(columns={'Bollinger Upper': 'Upper Bollinger Band',
                                                                 'Bollinger Middle': 'Middle Bollinger Band',
                                                                 'Bollinger Lower': 'Lower Bollinger Band'}
                                                        )
    tsla_bb_band = df_datetime_toUTC_drop_interval((tsla_bb_band))
    '''
    Understanding how to write pandas DF with tags, to influxDB #510
    Sep 30, 2017
    https://github.com/influxdata/influxdb-python/issues/510
    '''
    
    '''    
    data frame with tag columns #286
    Jan 26, 2016
    https://github.com/influxdata/influxdb-python/issues/286
    '''
    '''
    gte620V on Oct 2, 2017
    Sorry, I didn't look at the error closely before. Your problem is that the index is not a datetime index.

    You need to do some combination of pd.to_datetime and df.set_index to get your dataframe to have a datetimeindex. 
    You seem to have a column of string called index, which is not the same thing. 
    You need convert these strings to datetime objects with pd.to_datetime and then pass that column to df.set_index.
    '''

    # Set 'TimeStamp' field as index of dataframe
    tsla = tsla.set_index('date')
    logger.info(f'tsla:\n{tsla}')
    tsla.to_csv(path_or_buf='tsla.csv', sep=',', encoding = 'utf-8',index = False)

    tsla_bb_band = tsla_bb_band.set_index('date')
    logger.info(f'tsla_bb_band:\n{tsla_bb_band}')
    tsla_bb_band.to_csv(path_or_buf='tsla_bb_band.csv', sep=',', encoding = 'utf-8',index = False)

    
    logger.info(f'NVDA.stock_data:\n{local_stock_indicator_NVDA.stock_data}')
    
    local_stock_indicator_NVDA.calculate_moving_averages()
    nvda = local_stock_indicator_NVDA.stock_data
    nvda = df_datetime_toUTC_drop_interval(nvda)

    local_stock_indicator_NVDA.pstock_interval_startdate_enddate()
    local_stock_indicator_NVDA.calculate_bollinger_bands(window= timeperiod)
    nvda_bb_band = local_stock_indicator_NVDA.stock_data.rename(columns={'Bollinger Upper': 'Upper Bollinger Band',
                                                                 'Bollinger Middle': 'Middle Bollinger Band',
                                                                 'Bollinger Lower': 'Lower Bollinger Band'}
                                                                 )
    nvda_bb_band = df_datetime_toUTC_drop_interval(nvda_bb_band)
    
    # Set 'TimeStamp' field as index of dataframe
    nvda = nvda.set_index('date')
    logger.info(f'nvda:\n{nvda}')
    nvda.to_csv(path_or_buf='nvda.csv', sep=',', encoding = 'utf-8',index = False)
    
    nvda_bb_band = nvda_bb_band.set_index('date')
    logger.info(f'nvda_bb_band:\n{nvda_bb_band}')
    nvda_bb_band.to_csv(path_or_buf='nvda_bb_band.csv', sep=',', encoding = 'utf-8',index = False)

    # Tsla株価投入
    point_settings = PointSettings(**{"retrieved from" : "yahoo finance", 
                                    #  "inject time": str(datetime.now()), \
                                    "SYMBOL" : "TSLA", "NAME" : "Tesla, Inc.", "transform" : "original"})
    write_dataframe(client, BUCKET, tsla, measurement_name, point_settings)
    write_dataframe(client, BUCKET, tsla_bb_band, measurement_name_bb_band, point_settings)

    # NVIDIA株価投入
    point_settings = PointSettings(**{"retrieved from" : "yahoo finance", 
                                    #  "inject time": str(datetime.now()), \
                                    "SYMBOL" : "NVDA", "NAME" : "NVIDIA Corporation", "transform" : "original"})
    write_dataframe(client, BUCKET, nvda, measurement_name, point_settings)
    write_dataframe(client, BUCKET, nvda_bb_band, measurement_name_bb_band, point_settings)

    est_timer(t0)
    
    # Get present time
    t0 = time.time()    
    # query MA    
    query_str = query_flux_str(BUCKET, measurement_name, "Tesla, Inc.", tsla_ticker, "open")
    logger.info(f'query_str: {query_str}')
    query_influxdb(client, ORG, query_str)

    query_str = query_flux_str(BUCKET, measurement_name, "NVIDIA Corporation", nvda_ticker, "open")
    logger.info(f'query_str: {query_str}')
    query_influxdb(client, ORG, query_str)

    # query bollinger_bands
    query_str = query_flux_str(BUCKET, measurement_name_bb_band, "Tesla, Inc.", tsla_ticker, "close")
    logger.info(f'query_str: {query_str}')
    query_influxdb(client, ORG, query_str)
    
    query_str = query_flux_str(BUCKET, measurement_name_bb_band, "NVIDIA Corporation", nvda_ticker, "close")
    logger.info(f'query_str: {query_str}')
    query_influxdb(client, ORG, query_str)

    est_timer(t0)

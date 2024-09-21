from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime
import time
from binance.client import Client
 
def toinflux(token,org,bucket):
 
    with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
        try:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            #get btc 歷史資料
            api_key = ''
            api_secret = ''
            client = Client(api_key, api_secret)
            try:
                klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, "10 minutes ago UTC") # 一分鐘資料 # "1 day ago UTC"
            except Exception as e:
                print(e)
                pass
            data = []
            print('資料總數: {} 筆'.format(len(klines)))
            print('start to insert data to influxdb')
             
            for ind , ds in enumerate(klines):
                point = Point("data") \
                .tag("type", "btc") \
                .field("open", float(ds[1])) \
                .field("high", float(ds[2])) \
                .field("low", float(ds[3])) \
                .field("close", float(ds[4])) \
                .field("volume", float(ds[5])) \
                .time(datetime.datetime.fromtimestamp(ds[0]/ 1e3),WritePrecision.NS)
                data.append(point)
            try:    
                write_api.write(bucket, org, data)
            except Exception as e:
                print(e)
 
            print("寫入InfluxDB")
        except Exception as e:
            print(e)
 
 
if __name__ == "__main__":
    token = "your_influxdb_token"
    org = "your_org"
    bucket = "your_bucket"
    while True:
        toinflux(token,org,bucket)
        time.sleep(9)
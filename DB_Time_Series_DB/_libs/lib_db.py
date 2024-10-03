'''
株価の投入
https://qiita.com/ixtlan001/items/c87e4b2c4a97d7dba800#%E6%A0%AA%E4%BE%A1%E3%81%AE%E6%8A%95%E5%85%A5
'''

from influxdb_client import BucketRetentionRules, WriteOptions

from _libs.logger_setup import *

def create_bucket(client, bucket, organization):

    with client.buckets_api() as buckets_api:        
        retention_rules = BucketRetentionRules(type="expire", every_seconds=0, shard_group_duration_seconds=3600*24*365*10) # every_seconds = 0 means infinite
        created_bucket = buckets_api.create_bucket(bucket_name=bucket,
                                                   retention_rules=retention_rules, org= organization)
        logger.info(f"created_bucket: {created_bucket}")

def write_dataframe(client, bucket, df, measurement, point_settings):
   #instantiate the WriteAPI        
   with client.write_api(write_options=WriteOptions(batch_size=1000, flush_interval=30_000, jitter_interval=10_000, retry_interval=30_000), 
                         point_settings=point_settings) as write_api:
        write_api.write(bucket=bucket, 
                        record=df,
                        data_frame_tag_columns= ['retrieved from', 'inject time', 'SYMBOL', 'name'],
                        data_frame_measurement_name= measurement)

def query_influxdb(client, org, query):
    #instantiate the WriteAPI and QueryAPI
     #return the table and print the result
    result = client.query_api().query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_value(), record.get_field()))
    
    logger.info(f'results: {results}')

def delete_measurement(client, startdate, stopdate, measurement, bucket, organization):
    delete_api = client.delete_api()
    delete_api.delete(startdate, stopdate, f'_measurement="{measurement}"', bucket=bucket, org=organization)

#タイムスタンプを米国東部時間でのNasdaqとNYSEのOpen時間（午前9:30）に設定
#tsla = tsla.tz_localize(tz='US/Eastern')+pd.DateOffset(hours=9.5)    
def df_datetime_toUTC_drop_interval(dataframe):
    #if input is DataFrame with column 0
    dataframe['date'] = dataframe['date'].dt.tz_localize(tz='US/Eastern').dt.tz_convert(tz='UTC')
    # remove column 'interval' for insert data
    dataframe.drop(['interval'], axis=1, inplace=True)

    return dataframe

def query_flux_str(bucket, measurement, name, ticker, field):
    query = f'from(bucket: "{bucket}") \
        |> range(start: -10y)\
        |> filter(fn: (r) => r["_measurement"] == "{measurement}")\
        |> filter(fn: (r) => r["NAME"] == "{name}")\
        |> filter(fn: (r) => r["SYMBOL"] == "{ticker}")\
        |> filter(fn: (r) => r["_field"] == "{field}")\
        |> last()'
    
    return query

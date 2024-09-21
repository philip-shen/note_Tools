'''
https://github.com/x01963815/grab-stocks-data-to-influxdb/blob/master/grap_taiwan_stock_list.ipynb
'''
import os, sys, time
import pandas as pd
import argparse

import _libs.lib_misc as lib_misc
from _libs.logger_setup import *
from _libs.lib_twse_otc import *

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
    parser = argparse.ArgumentParser(description='grap taiwan stock tikcer')
    args = parser.parse_args()
    
    opt_verbose='ON'
    #opt_verbose='OFF'
    
    str_twse_url= 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
    str_tpex_url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=4'

    logger_set(strdirname)
    
    # Get present time
    t0 = time.time()
    local_time = time.localtime(t0)
    msg = 'Start Time is {}/{}/{} {}:{}:{}'
    logger.info(msg.format( local_time.tm_year,local_time.tm_mon,local_time.tm_mday,\
                            local_time.tm_hour,local_time.tm_min,local_time.tm_sec))
    pickle_fname = 'tw_stocks.pkl'
    
    query_twse_otc_code_02([str_twse_url], pickle_fname, opt_verbose=opt_verbose)
    '''
               code      name      國際證券辨識號碼         上市日 市場別   產業別     CFI
    0       1102.TW        亞泥  TW0001102002  1962/06/08  上市  水泥工業  ESVUFR
    1       1103.TW        嘉泥  TW0001103000  1969/11/14  上市  水泥工業  ESVUFR
    2       1104.TW        環泥  TW0001104008  1971/02/01  上市  水泥工業  ESVUFR
    3       1108.TW        幸福  TW0001108009  1990/06/06  上市  水泥工業  ESVUFR
    4       1109.TW        信大  TW0001109007  1991/12/05  上市  水泥工業  ESVUFR
    ...         ...       ...           ...         ...  ..   ...     ...
    38709  00951.TW   台新日本半導體  TW0000095108  2024/07/25  上市        CEOIEU
    38710  00952.TW  凱基台灣AI50  TW0000095207  2024/09/05  上市        CEOIEU
    38712  00954.TW   中信日本半導體  TW0000095405  2024/08/20  上市        CEOIEU
    38713  00956.TW   中信日經高股息  TW0000095603  2024/08/20  上市        CEOIEU
    38714  00960.TW  野村全球航運龍頭  TW0000096007  2024/09/20  上市        CEOIEU
    '''
    
    est_timer(t0) 
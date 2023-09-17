'''
OpenCVの勉強①（インストール、画像処理）
https://qiita.com/takanorimutoh/items/1085c102fa7023f50bc9
'''
'''
PythonでOpenCVの顔認識を試してみた
https://qiita.com/s-kajioka/items/b9207812fc968161f78b
'''

import cv2
import matplotlib.pyplot as plt
import os,sys,time

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

sys.path.append('./libs')

from logger_setup import *
from libs import lib_misc

def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.2f} seconds.'
    logger.info(msg)

if __name__ == "__main__":
    logger_set(strdirname)

    filename = "media/hisyo.jpg"

    # Get present ti    me
    t0 = time.time()
    local_time = time.localtime(t0)
    msg = 'Start Time is {}/{}/{} {}:{}:{}'
    logger.info(msg.format( local_time.tm_year,local_time.tm_mon,local_time.tm_mday,\
                            local_time.tm_hour,local_time.tm_min,local_time.tm_sec))
    
    img = cv2.imread(filename)

    
    #print(img.shape)
    logger.info(f'img.shape: {img.shape}')
    # (1136, 1600, 3)  ←(縦pixel size, 横のpixel size, 色の深さ=RBG=3色)

    #print(type(img))
    logger.info(f'type(img): {type(img)}')
    # <class 'numpy.ndarray'>  ←NumPyの配列(ndarray)で配列されている

    #print(img.dtype)
    logger.info(f'img.dtype: {img.dtype}')
    # uint8  ←8ビットの符号なし整数

    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()

    est_timer(start_time=t0)
'''
輪郭から四角形を検出
Posted at 2020-12-09
https://qiita.com/sitar-harmonics/items/ac584f99043574670cf3
'''

import math
import numpy as np
import os, sys, time
import cv2
from matplotlib import pyplot as plt
import argparse

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

sys.path.append('./libs')

from logger_setup import *
from libs import lib_misc, lib_common

(major, minor, _) = cv2.__version__.split(".")
    
def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.2f} seconds.'
    logger.info(msg)

# pt0-> pt1およびpt0-> pt2からの
# ベクトル間の角度の余弦(コサイン)を算出
def angle(pt1, pt2, pt0) -> float:
    dx1 = float(pt1[0,0] - pt0[0,0])
    dy1 = float(pt1[0,1] - pt0[0,1])
    dx2 = float(pt2[0,0] - pt0[0,0])
    dy2 = float(pt2[0,1] - pt0[0,1])
    v = math.sqrt((dx1*dx1 + dy1*dy1)*(dx2*dx2 + dy2*dy2) )
    return (dx1*dx2 + dy1*dy2)/ v

# 画像上の四角形を検出
def findSquares(bin_image, image, cond_area = 1000):
    # 輪郭取得
    # OpenCV version == 3 or other 
    if major == '3':
        _, contours, _ = cv2.findContours(bin_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, _ = cv2.findContours(bin_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for i, cnt in enumerate(contours):
        # 輪郭の周囲に比例する精度で輪郭を近似する
        arclen = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, arclen*0.02, True)

        #四角形の輪郭は、近似後に4つの頂点があります。
        #比較的広い領域が凸状になります。

        # 凸性の確認 
        area = abs(cv2.contourArea(approx))
        if approx.shape[0] == 4 and area > cond_area and cv2.isContourConvex(approx) :
            maxCosine = 0

            for j in range(2, 5):
                # 辺間の角度の最大コサインを算出
                cosine = abs(angle(approx[j%4], approx[j-2], approx[j-1]))
                maxCosine = max(maxCosine, cosine)

            # すべての角度の余弦定理が小さい場合
            #（すべての角度は約90度です）次に、quandrangeを書き込みます
            # 結果のシーケンスへの頂点
            if maxCosine < 0.3 :
                # 四角判定!!
                rcnt = approx.reshape(-1,2)
                cv2.polylines(image, [rcnt], True, (0,0,255), thickness=2, lineType=cv2.LINE_8)
    return image

def main(in_img):
    image = cv2.imread(in_img, cv2.IMREAD_COLOR)
    if image is None :
        exit(1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    rimage = findSquares(bw, image)
    cv2.imshow('Square Detector', rimage)
    c = cv2.waitKey()

    cv2.imwrite("media/34_4_pattern_square.jpg", rimage)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='34_4_pattern_square')
   
    parser.add_argument('--img', type=str, default='lena.bmp', help='image file')    
    args = parser.parse_args()

    logger_set(strdirname)
    
    # Get present time
    t0 = time.time()
    local_time = time.localtime(t0)
    msg = 'Start Time is {}/{}/{} {}:{}:{}'
    logger.info(msg.format( local_time.tm_year,local_time.tm_mon,local_time.tm_mday,\
                            local_time.tm_hour,local_time.tm_min,local_time.tm_sec))
    opt_verbose = 'On'
    img_file = args.img    
    path_infinicloud = '/home/philphoenix/infinicloud/OpenCV'
    if os.path.isfile(os.path.join(path_infinicloud, img_file)):
        main((os.path.join(path_infinicloud, img_file)))           
    
    est_timer(start_time=t0)
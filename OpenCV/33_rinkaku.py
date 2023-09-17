"""
pythonで一から画像処理 (4)輪郭抽出
https://qiita.com/fugunoko/items/7e5056449e172cbeadd9

"""
from pylab import rcParams #画像表示の大きさを変える
#%matplotlib inline
#rcParams['figure.figsize'] = 25, 20  #画像表示の大きさ
import os, sys, time
import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

sys.path.append('./libs')

from logger_setup import *
from libs import lib_misc, lib_common

def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.2f} seconds.'
    logger.info(msg)

def read_image(img_file, scale_value=0.8):
    img_bgr = cv2.imread(img_file)
    h, w = img_bgr.shape[:2]
    scale = (640 * 480 / (w * h)) ** scale_value#0.5
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)
    return img_rgb, img_gray

"""
OpenCV Python: cv2.findContours - ValueError: too many values to unpack

https://stackoverflow.com/questions/25504964/opencv-python-cv2-findcontours-valueerror-too-many-values-to-unpack

contours, hierarchy = cv2.findContours(
    skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

Explanation: By using [-2:], we are basically taking the last two values from the tuple returned by cv2.findContours. 
Since in some versions, it returns (image, contours, hierarchy) and 
in other versions, it returns (contours, hierarchy), contours, hierarchy are always the last two values.
"""
def rinkaku(img_file):
    '''
    img = cv2.imread(img_file,0)
    #画像を圧縮しておく
    img = cv2.resize(img, dsize=None, fx=0.15, fy=0.15)
    '''
    img_rgb, img_gray = read_image(img_file)

    #2値化(閾値は大津の二値化から)
    ret,thresh = cv2.threshold(img_gray,59,255,0)
    #反転
    thresh= cv2.bitwise_not(thresh)

    #輪郭抽出(RETR_CCOMPは2階層にする)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #RGB形式に変換する

    #見つけた輪郭を元画像に描画
    for i in range(len(contours)):

        #最上層の階層を描画（緑）
        if hierarchy[0][i][3] == -1:        
            cv2.drawContours(img_rgb, contours, i, (0, 255, 0), 2)
        #2階層目を描画（水色）
        else:
            cv2.drawContours(img_rgb, contours, i, (0, 255, 255), 2)        
    
    plt.legend()
    plt.imshow(img_rgb)
    plt.show()
    
def rinkakukinzi(img_file):
    img = cv2.imread(img_file,0)
    img = cv2.resize(img, dsize=None, fx=0.15, fy=0.15)
    ret,thresh = cv2.threshold(img,59,255,0)
    thresh= cv2.bitwise_not(thresh)

    #輪郭抽出
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #RGB形式に変換する

    #足の部分の輪郭
    cnt = contours[7]

    #輪郭近似 epsilonは近似の程度
    epsilon = 0.01*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    #近似輪郭を元画像に描画
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

    plt.imshow(img)

def gaisetsu(img_file):
    img = cv2.imread('C:/brabra/6.jpg',0)
    img = cv2.resize(img, dsize=None, fx=0.15, fy=0.15)
    ret,thresh = cv2.threshold(img,59,255,0)
    thresh= cv2.bitwise_not(thresh)

    #輪郭抽出
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #RGB形式に変換する

    #足部の輪郭を描画
    cv2.drawContours(img, contours, 7, (0, 255, 0), 2)

    cnt = contours[7]

    #外接矩形
    x,y,w,h = cv2.boundingRect(cnt)
    img0 = img.copy()
    img0 = cv2.rectangle(img0,(x,y),(x+w,y+h),(0,255,0),2)

    #回転を考慮した外接矩形
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    img00 = img.copy()
    img00 = cv2.drawContours(img00,[box],0,(0,0,255),2)

    #最小外接円
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    img1 = img.copy()
    img1 = cv2.circle(img1,center,radius,(0,255,255),2)

    #楕円fitting
    ellipse = cv2.fitEllipse(cnt)
    img2 = img.copy()
    img2 = cv2.ellipse(img2,ellipse,(255,255,0),2)

    #直線fitting
    rows,cols = img.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    img3 = img.copy()
    img3 = cv2.line(img3,(cols-1,righty),(0,lefty),(255,255,255),2)

    plt.subplot(231),plt.imshow(img0)
    plt.title('en'), plt.xticks([]), plt.yticks([])
    plt.subplot(232),plt.imshow(img00)
    plt.title('en'), plt.xticks([]), plt.yticks([])
    plt.subplot(233),plt.imshow(img1)
    plt.title('en'), plt.xticks([]), plt.yticks([])
    plt.subplot(234),plt.imshow(img2)
    plt.title('daen'), plt.xticks([]), plt.yticks([])
    plt.subplot(235),plt.imshow(img3)
    plt.title('line'), plt.xticks([]), plt.yticks([])

    plt.show()

def main(img_file):
    rinkaku(img_file)
    
"""
https://github.com/RyuSeiri/ContourDetectionAndApproximation/blob/master/contour.py

[OpenCV][Python3]検出した輪郭を描画し、輪郭線を近似して滑らかにする
https://qiita.com/y_kani/items/c9861b1f3517c32491d6#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB
"""

def approx_contour(contours):
    ######################################################
    # 輪郭直線近似
    ######################################################
    approx = []
    for i in range(len(contours)):
        cnt = contours[i]
        epsilon = 0.0001*cv2.arcLength(cnt,True)
        approx.append(cv2.approxPolyDP(cnt,epsilon,True))
    return approx


def drawing_edge(org_img, contours, cp_org_img_for_draw):
    ######################################################
    # 輪郭線描画
    ######################################################
    min_area = 100
    large_contours = [
        cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    cv2.drawContours(cp_org_img_for_draw, large_contours, -1, (255, 0, 0), 5)


def setting_for_display(org_img, h_img, s_img, v_img, hist_s_img,
        result_bin, result_morphing, cp_org_img_for_draw):
    ######################################################
    # 表示設定
    # 概要: imshow()で表示する際のウィンドウをサイズ変更可能にする設定
    ######################################################

    # 元画像
    cv2.namedWindow('org_img', cv2.WINDOW_NORMAL)
    cv2.namedWindow("h", cv2.WINDOW_NORMAL)
    cv2.namedWindow("s", cv2.WINDOW_NORMAL)
    cv2.namedWindow("v", cv2.WINDOW_NORMAL)

    # # Hヒストグラム平坦化後
    cv2.namedWindow('hist_s_img', cv2.WINDOW_NORMAL)

    # 二値化
    cv2.namedWindow('result_bin', cv2.WINDOW_NORMAL)

    # モーフィング
    cv2.namedWindow('result_morphing', cv2.WINDOW_NORMAL)

    # 輪郭線描画
    cv2.namedWindow('cp_org_img_for_draw', cv2.WINDOW_NORMAL)

    # 元画像
    cv2.imshow('org_img', org_img)
    cv2.imshow("h", h_img)
    cv2.imshow("s", s_img)
    cv2.imshow("v", v_img)

    # Hヒストグラム平坦化後
    cv2.imshow('hist_s_img', hist_s_img)

    # 二値化
    cv2.imshow('result_bin', result_bin)

    # モーフィング
    cv2.imshow('result_morphing', result_morphing)

    # 輪郭線描画
    cv2.imshow('cp_org_img_for_draw', cp_org_img_for_draw)
    
def display_result(
        org_img, h_img, s_img, v_img, hist_s_img,
        result_bin, result_morphing, cp_org_img_for_draw):
    ######################################################
    # 表示処理
    ######################################################
    
    plt.figure(figsize=(9, 9))  # 画像の表示サイズ
    plt.subplot(241), plt.imshow(org_img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(242), plt.imshow(h_img), plt.title("h")
    plt.xticks([]), plt.yticks([])
    plt.subplot(243), plt.imshow(s_img), plt.title("s")
    plt.xticks([]), plt.yticks([])
    plt.subplot(244), plt.imshow(v_img), plt.title("v")
    plt.xticks([]), plt.yticks([])
    #plt.tight_layout()

    plt.subplot(245), plt.imshow(hist_s_img), plt.title("hist_s_img")
    plt.xticks([]), plt.yticks([])
    plt.subplot(246), plt.imshow(result_bin), plt.title("result_bin")
    plt.xticks([]), plt.yticks([])
    plt.subplot(247), plt.imshow(result_morphing), plt.title("result_morphing")
    plt.xticks([]), plt.yticks([])
    plt.subplot(248), plt.imshow(cp_org_img_for_draw), plt.title("cp_org_img_for_draw")
    plt.xticks([]), plt.yticks([])
    plt.show()

    # 入力待機（これがないとimshow()の表示がされないため注意）
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

def main2(img_file):

    # Reading the original image
    org_img = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(org_img, cv2.COLOR_BGR2HSV)

    # Spliting to H,S,V
    h_img, s_img, v_img = cv2.split(hsv)
    s_img = cv2.bitwise_not(s_img)

    # Flattening a histgram of s_img
    hist_s_img = cv2.equalizeHist(s_img)

    # Binarization
    _, result_bin = cv2.threshold(
        s_img, 200, 255, cv2.THRESH_BINARY)

    # Morphing（Closing）
    ## Setting filters
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 4))
    ## Execution morphing
    result_morphing = cv2.morphologyEx(
        result_bin, cv2.MORPH_CLOSE, kernel)

    # Detection contours
    #tmp_img, contours, _ = cv2.findContours(
    contours, _ = cv2.findContours(    
        result_morphing, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Contour approximation
    approx = approx_contour(contours)

    # Contour line drawing
    cp_org_img_for_draw = np.copy(org_img)
    drawing_edge(org_img, approx, cp_org_img_for_draw)

    # Setting for display
    setting_for_display(
        org_img, h_img, s_img, v_img, hist_s_img,
        result_bin, result_morphing, cp_org_img_for_draw)
    # Execution display
    display_result(
        img_rgb, h_img, s_img, v_img, hist_s_img,
        result_bin, result_morphing, cp_org_img_for_draw)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='33_rinkaku')
   
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
    
    if os.path.isfile(os.path.join('media', img_file)):
        main((os.path.join('media', img_file)))           

    '''
    if os.path.isfile(os.path.join('media', img_file)):
        main2((os.path.join('media', img_file)))           
    '''
    est_timer(start_time=t0)

    
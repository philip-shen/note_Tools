import os, sys, time
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import scipy.special as special

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

'''
使用SciPy提供的特殊函數，可以用來計算Beta矯正的轉換函數，以實現影像對比的增強。
'''
def beta_correction(img_file, a = 2.0, b = 2.0):
    img1 = cv2.imread(img_file, -1)

    g = img1.copy()
    nr, nc = img1.shape[:2]
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x) * 255, 0)
    if img1.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[img1[x, y]]

    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[img1[x,y,k]]
    
    
    cv2.imshow(f"Beta Correction: {a}, {b}", g)
    cv2.waitKey()
'''
本程式採用OpenCV提供的calcHist函式計算直方圖，
並利用matplotlib套件繪圖，且此程式同時適用於灰階和色彩影像。
'''
def histogram(img_file):
    img = cv2.imread(img_file, -1)
    img_bgr = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    if img.ndim != 3:
        hist = cv2.calcHist([img], [0], None, [256], [0,256])
        plt.plot(hist)
    else:
        color = ('b', 'g', 'r')
        '''
        for i, col in enumerate(color):
            hist = cv2.calcHist([img], [i], None, [256], [0,256])
            plt.plot(hist, color = col)
            plt.xlim([0,256])
            plt.xlabel("Intensity")
            plt.ylabel("#Intensities")
            plt.show()
        '''
        hist_full_b = cv2.calcHist([img],[0],None,[256],[0,256])
        hist_full_g = cv2.calcHist([img],[1],None,[256],[0,256])
        hist_full_r = cv2.calcHist([img],[2],None,[256],[0,256])

        plt.figure(figsize=(8, 8))  # 画像の表示サイズ
        plt.subplot(211), plt.imshow(img_rgb)
        plt.subplot(212)
        plt.plot(hist_full_r, color[2])
        plt.plot(hist_full_g, color[1])
        plt.plot(hist_full_b, color[0])
        plt.xlim([0,256])
        plt.xlabel("Intensity")
        plt.ylabel("#Intensities")
        plt.show()

    cv2.waitKey()

def histogram_equalize(img_file):
    #img1 = cv2.imread(img_file, -1)
    img_bgr = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # For Gray
    if img_bgr.ndim != 3:#if img1.ndim != 3:        
        img2 = cv2.equalizeHist(img_bgr)#cv2.equalizeHist(img1)
    # For Color
    else:
        #R, G, B = cv2.split(img1)
        R, G, B = cv2.split(img_rgb)

        output1_R = cv2.equalizeHist(R)
        output1_G = cv2.equalizeHist(G)
        output1_B = cv2.equalizeHist(B)
        img2 = cv2.merge((output1_R, output1_G, output1_B))
    
    #cv2.imshow("Orignial", img1)
    cv2.imshow("Orignial", img_bgr)
    cv2.imshow("Histogram Equalize", img2)
    cv2.waitKey()

def read_rgb(img_file):
    img_bgr = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    plt.imshow(img_rgb)
    plt.show()

def histogram2(img_file):
    img = cv2.imread(img_file, -1)
    img_bgr = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # read_rgba.pyと同様に画像をアルファチャンネル込みのRGBA画像として読み込む
    img_rgba = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)

    # グラフ生成時にx軸として使用する長さ256のNumPy配列をcnt[i] = iで初期化する
    cnt = np.arange(256)

    # RGBの各色の値をカウントする長さ256のNumPy配列を0で初期化する
    cnt_red = np.zeros(256)
    cnt_green = np.zeros(256)
    cnt_blue = np.zeros(256)

    # 画像の縦横を得る
    height = img_rgba.shape[0]
    width = img_rgba.shape[1]

    for i in range(height):
        for j in range(width):
	    # アルファチャンネルが0(透明)であればスキップする
            if img_rgba.item(i, j, 3) == 0:
                continue
            else:
	        # 不透明であればRGBの各色の値をカウントしていく
                cnt_red[img_rgba.item(i, j, 0)] += 1
                cnt_blue[img_rgba.item(i, j, 1)] += 1
                cnt_green[img_rgba.item(i, j, 2)] += 1

    plt.figure(figsize=(10, 10))  # 画像の表示サイズ
    plt.subplot(311), plt.imshow(img_bgr), plt.title('COLOR_BGR')
    plt.subplot(312), plt.imshow(img_rgb), plt.title('COLOR_RGB')
    plt.subplot(313), plt.title('Historgam')
    plt.plot(cnt, cnt_red, color = 'red', label = 'red')
    plt.plot(cnt, cnt_green, color = 'green', label = 'green')
    plt.plot(cnt, cnt_blue, color = 'blue', label = 'blue')
    plt.legend()
    plt.xlabel("Intensity")
    plt.ylabel("#Intensities")
    plt.show()

def main(img_file, a = 0.5, b = 0.5):
    read_rgb(img_file)
    histogram(img_file)
    histogram2(img_file)
    histogram_equalize(img_file)
    beta_correction(img_file, a, b)
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='24_beta_correct_histogram_equalize')
   
    parser.add_argument('--img', type=str, default='lena.bmp', help='image file')
    parser.add_argument('--beta_a', type=float, default=0.1, help='Beat a coefficient')
    parser.add_argument('--beta_b', type=float, default=0.1, help='Beat b coefficient')
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
    beta_a = args.beta_a
    beta_b = args.beta_b

    if os.path.isfile(os.path.join('media', img_file)):
        main((os.path.join('media', img_file)), beta_a, beta_b)           
        
    est_timer(start_time=t0)
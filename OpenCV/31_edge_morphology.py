"""
pythonで一から画像処理 (3)エッジ検出、モルフォロジー変換
https://qiita.com/fugunoko/items/8997e3d160d8ed93eaa9

"""

import os, sys, time
import numpy as np
from numpy.random import normal
import scipy as sp
import cv2
import argparse
from matplotlib import pyplot as plt
from PIL import Image,ImageSequence

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

def img_read(img_file, scale_val=0.7):
    img_bgr = cv2.imread(img_file)
    h, w = img_bgr.shape[:2]
    scale = (700 * 600 / (w * h)) ** scale_val
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)

    return img_bgr_resize, img_rgb, img_gray

def sobel_laplacian_filter(img_file):
    _, img, _ = img_read(img_file, scale_val=0.9)

    #Laplacianフィルタ
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    #Sobelフィルタx方向
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=15)
    #Sobelフィルタy方向
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=15)

    plt.figure(figsize=(7, 5))  # 画像の表示サイズ
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.waitKey()  

def canny(img_file):
    _, img, _ = img_read(img_file, scale_val=0.9)
    minVal = 50
    maxVal = 250
    SobelSize = 20

    edges = cv2.Canny(img,minVal,maxVal,SobelSize)

    plt.figure(figsize=(7, 5))  # 画像の表示サイズ
    plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()
    cv2.waitKey()  

"""
・Erosion(収縮)
・Dilation(膨張)
・Opening(収縮⇒膨張　小さい点のようなノイズ除去)
・Closing(膨張⇒収縮　小さい箇所の穴埋め)
・勾配（膨張-収縮で輪郭を得る）
・トップハット（入力-Opening）
・ブラックハット（入力-Closing）
"""
def mol(img_file):
    #img = cv2.imread(img_file,0)
    _, _, img = img_read(img_file, scale_val=0.9)
    
    #大津の2値化されたパンダ
    abc,two = cv2.threshold(img,0,255,
                            cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #白黒反転（白に適用されるため）
    two = cv2.bitwise_not(two)

    #Erositon
    kernel = np.ones((35,35),np.uint8)
    erosion = cv2.erode(two,kernel,iterations = 1)
    #Dilation
    kernel = np.ones((35,35),np.uint8)
    dilation = cv2.dilate(two,kernel,iterations = 1)
    #Opening
    kernel = np.ones((35,35),np.uint8)
    opening = cv2.morphologyEx(two, cv2.MORPH_OPEN, kernel)
    #Closing
    kernel = np.ones((35,35),np.uint8)
    closing = cv2.morphologyEx(two, cv2.MORPH_CLOSE, kernel)
    #Gradient
    kernel = np.ones((35,35),np.uint8)
    gradient = cv2.morphologyEx(two, cv2.MORPH_GRADIENT, kernel)
    #Tophat
    kernel = np.ones((35,35),np.uint8)
    tophat = cv2.morphologyEx(two, cv2.MORPH_TOPHAT, kernel)
    #Blackhat
    kernel = np.ones((35,35),np.uint8)
    blackhat = cv2.morphologyEx(two, cv2.MORPH_BLACKHAT, kernel)

    plt.figure(figsize=(7, 6))  # 画像の表示サイズ
    
    plt.subplot(331),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(332),plt.imshow(two,cmap = 'gray')
    plt.title('2value Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(333),plt.imshow(erosion,cmap = 'gray')
    plt.title('Erosion Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(334),plt.imshow(dilation,cmap = 'gray')
    plt.title('Dilation Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(335),plt.imshow(opening,cmap = 'gray')
    plt.title('Opening Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(336),plt.imshow(closing,cmap = 'gray')
    plt.title('Closing Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(337),plt.imshow(gradient,cmap = 'gray')
    plt.title('Gradient Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(338),plt.imshow(tophat,cmap = 'gray')
    plt.title('Tophat Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(339),plt.imshow(blackhat,cmap = 'gray')
    plt.title('Blackhat Image'), plt.xticks([]), plt.yticks([])

    plt.tight_layout()    
    plt.show()
    cv2.waitKey()  

def rinkaku(img_file):
    img = cv2.imread(img_file,0)
    edges = cv2.Canny(img,50,250,10)

    #Closing
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((35,35),np.uint8)
    closing2 = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((135,135),np.uint8)
    closing3 = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    plt.figure(figsize=(7, 6))  # 画像の表示サイズ    
    plt.subplot(231),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(232),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(233),plt.imshow(closing,cmap = 'gray')
    plt.title('Closing Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(234),plt.imshow(closing2,cmap = 'gray')
    plt.title('Closing2 Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(235),plt.imshow(closing3,cmap = 'gray')
    plt.title('Closing3 Image'), plt.xticks([]), plt.yticks([])

    plt.tight_layout()    
    plt.show()
    cv2.waitKey()  

def main(img_file):
    rinkaku(img_file)
    mol(img_file)
    canny(img_file)
    sobel_laplacian_filter(img_file)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='31_edge_morphology')
   
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

    est_timer(start_time=t0)

import os, sys, time
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

from pylab import rcParams #画像表示の大きさを変える
#%matplotlib inline
rcParams['figure.figsize'] = 25, 20  #画像表示の大きさ

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



"""
pythonで一から画像処理 (1)閾値処理
https://qiita.com/fugunoko/items/95627e36e0363e4806c2
"""
def histgram(img_file):
    #画像読み込み
    image = cv2.imread(img_file,0) #grayscaleで読み込み
    img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #RGB形式に変換する

    #画像表示
    plt.subplot(2,1,1),plt.imshow(img,'gray')
    #graysscaleのヒストグラム表示
    plt.subplot(2,1,2),plt.hist(img.ravel(),256)
    plt.show()

def threshold(img_file):
    img = cv2.imread(img_file,0)

    #閾値は100
    #retには閾値、thresh1~3には処理画像が入る

    #閾値以下を黒にする
    ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    #閾値以上を黒にする
    ret,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
    #閾値以上を閾値に、以下は変更なし
    ret,thresh3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
    #閾値以上は変更なし、それ以下は黒
    ret,thresh4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
    #閾値以上は黒、それ以下は変更なし
    ret,thresh5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()

def threshold2(img_file):
    img = cv2.imread(img_file,0)

    #50~300まで閾値を変化させる
    ret1,thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
    ret3,thresh3 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    ret4,thresh4 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    ret5,thresh5 = cv2.threshold(img,250,255,cv2.THRESH_BINARY)
    ret6,thresh6 = cv2.threshold(img,300,255,cv2.THRESH_BINARY)

    titles = [ret1,ret2,ret3,ret4,ret5,ret6]
    images = [thresh1, thresh2, thresh3, thresh4, thresh5, thresh6]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    plt.show()

def adaptive_thresholding(img_file):
    img = cv2.imread(img_file,0)

    #基本の閾値処理
    ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

    #adaptive mean thresholding
    #画像の小領域毎に閾値処理。その領域の平均値を閾値とする。
    #後ろの引数は近傍のサイズ、閾値から引く定数
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,51,0)

    #adaptive Gaussian thresholding
    #画像の小領域毎に閾値処理。その領域の正規分布で重み付けした平均値を閾値とする
    #後ろの引数は近傍のサイズ、閾値から引く定数
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,0)

    titles = ['Original Image', 'Global Thresholding (v = 100)',
                'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]

    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    
    plt.show()

def Ootu(img_file):
    img = cv2.imread(img_file,0)

    #基本の閾値処理 閾値は50
    ret1,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

    #大津の二値化
    ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #ガウシアン平均化+大津の二値化
    blur = cv2.GaussianBlur(img,(11,11),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    images = [img, 0, th1,
              img, 0, th2,
              blur, 0, th3]
    titles = ['Original Noisy Image','Histogram','Global Thresholding (v=50)',
              'Original Noisy Image','Histogram',"Otsu's Thresholding_Thr="+str(ret2),
              'Gaussian filtered Image','Histogram',"Otsu's Thresholding_Thr="+str(ret3)]

    for i in range(3):
        plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    
    plt.show()

def main(img_file):
    
    histgram(img_file)
    threshold(img_file)
    threshold2(img_file)
    adaptive_thresholding(img_file)
    Ootu(img_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='21_image_quantization')
   
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
    img_file= args.img

    if os.path.isfile(os.path.join('media', img_file)):
        main((os.path.join('media', img_file)))   
        
    est_timer(start_time=t0)
    

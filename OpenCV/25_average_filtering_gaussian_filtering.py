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

def blur(img_file):
    img1 = cv2.imread(img_file, -1)
    img2 = cv2.blur(img1, (5, 5))
    img3 = cv2.blur(img1, (11, 11))
    img4 = cv2.blur(img1, (20, 20))
    '''
    cv2.imshow("Orignial", img1)
    cv2.imshow("5x5", img2)
    cv2.imshow("11x11", img3)
    cv2.imshow("20x20", img4)
    cv2.waitKey()
    '''
    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    plt.subplot(221), plt.imshow(img1), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(img2), plt.title("Averaging kernel: 5x5")
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(img3), plt.title("Averaging kernel: 10x10")
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img4), plt.title("Averaging kernel: 20x20")
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.show()
'''
Python OpenCV 影像平滑模糊化 blur 
https://shengyu7697.github.io/python-opencv-blur/
'''
def blur2(img_file):
    img = cv2.imread(img_file)

    blur = cv2.blur(img, (5, 5))

    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.show()

'''
Python OpenCV cv2.GaussianBlur 高斯濾波 
https://shengyu7697.github.io/python-opencv-gaussianblur/
'''

def gaussianBlur(img_file):
    img = cv2.imread(img_file)

    blur_3 = cv2.GaussianBlur(img, (3, 3), 0)
    blur_7 = cv2.GaussianBlur(img, (7, 7), 0)
    blur_5 = cv2.GaussianBlur(img, (5, 5), 0)
    
    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    plt.subplot(221), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(blur_3), plt.title('Gaussian Blurred: 3*3')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(blur_5), plt.title('Gaussian Blurred: 5*5')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(blur_7), plt.title('Gaussian Blurred: 7*7')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.show()
    
def sepFilter2D(img_file):
    img = cv2.imread(img_file)

    kernel_size = 5
    sigma = 0
    kernel_1d = cv2.getGaussianKernel(kernel_size, sigma)

    blur = cv2.sepFilter2D(img, -1, kernel_1d, kernel_1d)

    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('sepFilter2D Blurred')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.show()

def main(img_file):
    blur(img_file)
    blur2(img_file)
    gaussianBlur(img_file)
    sepFilter2D(img_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='24_beta_correct_histogram_equalize')
   
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

    
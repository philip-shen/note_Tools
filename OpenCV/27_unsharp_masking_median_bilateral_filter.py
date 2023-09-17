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

def unsharp_masking(f, k = 1.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    f_avg = cv2.GaussianBlur(f,(15, 15), 0)
    for x in range(nr):
        for y in range(nc):
            g_mask = int(f[x, y]) - int(f_avg[x, y])

    return g

def median_filter(img_file):
    img1 = cv2.imread(img_file, -1)
    img2 = cv2.medianBlur(img1, 3)
    
    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()

    return img1, img2

def bilateral_filter(img_file):
    img1 = cv2.imread(img_file,-1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.bilateralFilter(img1, 5, 50, 50)

    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()

    return img1, img2

def main(img_file):
    img1 = cv2.imread( os.path.join('media', img_file[0]) , 0)
    img2 = unsharp_masking(img1, 10.0)
    
    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()

    img3, img4 = median_filter(os.path.join('media', img_file[1]))
    img5, img6 = bilateral_filter(os.path.join('media', img_file[2]))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='27_unsharp_masking_median_bilateral_filter')
   
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

    #if os.path.isfile(os.path.join('media', img_file)):
    #    main((os.path.join('media', img_file)))           
    list_img_files = ['church_02.jpg', 'salt-and-pepper-noise-Lena.png', 'lena.bmp']
    main(list_img_files)

    est_timer(start_time=t0)




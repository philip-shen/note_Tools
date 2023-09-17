import os, sys, time
import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt

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

def image_negative(img_file):
    img1 = cv2.imread(img_file, -1)
    
    img2 = 255 - img1
    cv2.imshow("image negative", img2)
    cv2.waitKey()
    
def gamma_correction(img_file, gamma = 2.0):
    img1 = cv2.imread(img_file, -1)
    g = img1.copy()
    nr,nc = img1.shape[:2]

    c = 255.0 / (255.0 ** gamma)
    table = np.zeros(256)
    for i in range(256):
        table[i] = round(i ** gamma * c, 0)
    
    if img1.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[x, y]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[img1[x, y, k]]

    cv2.imshow("gamma correction", g)
    cv2.waitKey()

def main(img_file, gamma_num):
    image_negative(img_file)
    gamma_correction(img_file, gamma_num)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='23_image_negative_gamma_correct')
   
    parser.add_argument('--img', type=str, default='lena.bmp', help='image file')
    parser.add_argument('--gamma', type=float, default=0.1, help='image file')
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
    gamma = args.gamma

    if os.path.isfile(os.path.join('media', img_file)):
        main((os.path.join('media', img_file)), gamma)           

    est_timer(start_time=t0)

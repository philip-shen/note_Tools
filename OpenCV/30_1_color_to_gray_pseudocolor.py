import os, sys, time
import numpy as np
from numpy.random import normal
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

def gray_to_color(img_file):

    img1 = cv2.imread(img_file, -1)
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

def pseudocolor(img_file):
    img1 = cv2.imread(img_file, -1)
    img2 = cv2.applyColorMap(img1, cv2.COLORMAP_HSV)

    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()

def main(img_file):
    gray_to_color(img_file)
    pseudocolor(img_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='30_1_color_to_gray_pseudocolor')
   
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
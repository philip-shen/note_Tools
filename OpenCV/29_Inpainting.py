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

def inpainting(f, method = 1):
    nr, nc = f.shape[:2]
    mask = np.zeros([nr, nc], dtype = 'uint8')
    for x in range(nr):
        for y in range(nc):
            if f[x, y, 0] == 0 and f[x, y, 1] == 255 and f[x, y, 2] == 255:
                mask[x, y] = 255
    
    if method == 1:
        g = cv2.inpaint(f, mask, 3, cv2.INPAINT_NS)
    else:
        g = cv2.inpaint(f, mask, 3, cv2.INPAINT_TELEA)
    return g

def main(img_file):
    img1 = cv2.imread(img_file,-1)
    img2 = inpainting(img1, 1)
    img3 = inpainting(img1, 0)
    
    cv2.imshow("Original", img1)
    cv2.imshow("Inpainting: INPAINT_NS", img2)
    cv2.imshow("Inpainting: INPAINT_TELEA", img3)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='29_Inpainting')
   
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

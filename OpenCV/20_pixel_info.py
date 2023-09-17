'''
Image_Processing/[Day2]OpenCV Introdution/pixel_info.py

https://github.com/Damien-Chen/Image_Processing/blob/main/%5BDay2%5DOpenCV%20Introdution/pixel_info.py

'''
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

def onMouse(event, x, y, flags, param):
    x, y = y, x
    if img.ndim != 3:
        logger.info('(x, y) = ({:d}, {:d}); Gray level = {:3d}'.format(x,y,img[x,y]))
        #logger.info('Gray level = {:3d}'.format(img[x,y]))
    else:
        logger.info("(x, y) = ({:d}, {:d}); (R, G, B) = ({:3d}, {:3d}, {:3d})".format(x,y,img[x,y,2],img[x,y,1],img[x,y,0]))
        #logger.info("(R, G, B) = ({:3d}, {:3d}, {:3d})".format(img[x,y,2],img[x,y,1],img[x,y,0]))

def pixel_info(img_file):
    global img
    img = cv2.imread(img_file, -1)
    cv2.namedWindow(img_file)
    cv2.setMouseCallback(img_file, onMouse)
    cv2.imshow(img_file,img)
    cv2.waitKey(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='20_pixel_info')
   
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
        pixel_info((os.path.join('media', img_file)))
    
    est_timer(start_time=t0)
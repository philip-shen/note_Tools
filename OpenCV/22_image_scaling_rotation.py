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

def img_scaling(img_file):
    img1 = cv2.imread(img_file, -1)

    nr,nc = img1.shape[:2]
    scale = eval(input("Please enter scale:"))
    nr2 = int(nr * scale)
    nc2 = int(nc * scale)

    img2 = cv2.resize(img1, (nr2,nc2), interpolation = cv2.INTER_NEAREST)
    img3 = cv2.resize(img1, (nr2,nc2), interpolation = cv2.INTER_LINEAR)
    cv2.imshow("Original", img1)
    cv2.imshow(f"cv2.INTER_NEAREST", img2)
    cv2.imshow(f"cv2.INTER_LINEAR", img3)

    cv2.waitKey()

'''
首先先定義影像中心為旋轉中心，
以角度30度逆時針旋轉，接著呼叫OpenCV的仿射轉換涵式，即可取得旋轉後的數位影像
'''
def img_rotation(img_file):
    img1 = cv2.imread(img_file, -1)

    nr2,nc2 = img1.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((nc2 / 2, nr2 / 2), 30, 1)
    img2 = cv2.warpAffine(img1, rotation_matrix,(nc2, nr2))

    cv2.imshow("Original", img1)
    cv2.imshow("After", img2)

    cv2.waitKey()

def main(img_file):
    aligned_imgs = []

    img_scaling(img_file)
    img_rotation(img_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='22_image_scaling_rotation')
   
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




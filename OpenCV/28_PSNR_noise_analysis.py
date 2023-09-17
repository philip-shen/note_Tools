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

def gaussian_noise(f, scale):
    g = f.copy()
    nr, nc = f.shape[:2]
    for x in range(nr):
        for y in range(nc):
            value = f[x, y] + normal(0, scale)
            g[x, y] = np.uint8(np.clip(value, 0, 255))
    
    return g

def PSNR(f, g):
    nr, nc = f.shape[:2]
    MSE = 0.0
    for x in range(nr):
        for y in range(nc):
            MSE += (float(f[x, y]) - float(g[x, y]))** 2
    MSE /= (nr * nc)
    PSNR = 10 * np.log10((255 * 255) / MSE)
    return PSNR

def histogram(f):
    if f.ndim != 3:
        hist = cv2.calcHist([f], [0], None, [256], [0,256])
        plt.plot(hist)
    else:
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            hist = cv2.calcHist(f, [i], None, [256], [0,256])
            plt.plot(hist, color = col)
    plt.xlim([0, 256])
    plt.xlabel("Intensity")
    plt.ylabel("#Intensities")
    plt.show()

def main(img_file):
    f = cv2.imread(img_file, 0)
    g_10 = gaussian_noise(f, 10)
    g_20 = gaussian_noise(f, 20)
    g_50 = gaussian_noise(f, 50)
    
    print("PSNR of gaussian_noise 10: {}; PSNR of gaussian_noise 20: {}; PSNR of gaussian_noise 50: {}".\
            format(PSNR(f, g_10), PSNR(f, g_20), PSNR(f, g_50)) )
    cv2.imshow("Original", f)
    cv2.imshow("Gaussian Noise: 10", g_10)
    cv2.imshow("Gaussian Noise: 20", g_20)
    cv2.imshow("Gaussian Noise: 50", g_50)

    ROI = f[55:95, 55:95]
    histogram(ROI)
    print("Sigma = ", np.std(ROI))

    cv2.waitKey()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='28_PSNR_noise_analysis')
   
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
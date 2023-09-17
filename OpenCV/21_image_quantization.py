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

def image_quantization(f, bits):
    g = f.copy()
    nr, nc = f.shape[:2]
    levels = 2**bits
    interval = 256 / levels
    gray_level_interval = 255 / (levels - 1)
    table = np.zeros(256)
    for k in range(256):
        for l in range(levels):
            if k >= l * interval and k < (l+l)*interval:
                table[k] = round(l * gray_level_interval)
    for x in range(nr):
        for y in range(nc):
            g[x,y] = np.uint8(table[f[x,y]])
    return g

def show_resize_window(title, img):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL) 
    imS = cv2.resize(img, (960, 540))   
    cv2.imshow(title, imS)

def main(img_file):
    aligned_imgs = []
    
    img1 = cv2.imread(img_file, -1)
    img2 = image_quantization(img1, 5)
    img3 = image_quantization(img1, 4)
    img4 = image_quantization(img1, 3)
    img5 = image_quantization(img1, 2)
    img6 = image_quantization(img1, 1)
    aligned_imgs.append(img2)
    aligned_imgs.append(img3)
    aligned_imgs.append(img4)
    aligned_imgs.append(img5)
    aligned_imgs.append(img6)
    '''
    cv2.imshow("Original Image", imS)
    cv2.imshow("Quant5",img2)
    cv2.imshow("Quant4",img3)
    cv2.imshow("Quant3",img4)
    cv2.imshow("Quant2",img5)
    cv2.imshow("Quant1",img6)
    '''
    show_resize_window("Original Image", img1)
    show_resize_window("Quant5", img2)
    show_resize_window("Quant4",img3)
    show_resize_window("Quant3",img4)
    show_resize_window("Quant2",img5)
    show_resize_window("Quant1",img6)
    cv2.waitKey()
    
    '''
    num_images = len(aligned_imgs)    
    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    for i in range(num_images):
        plt.subplot(1, 6, i+1)
        
        plt.imshow(cv2.cvtColor(aligned_imgs[i], cv2.COLOR_BGR2RGB))
        plt.tick_params(labelbottom=True, labelleft=False, bottom=False, left=False)  # ラベルとメモリを非表示に
    plt.show()        
    '''

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
    

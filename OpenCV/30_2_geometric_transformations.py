"""
python+opencvで画像処理の勉強5 幾何学的変換
https://qiita.com/tanaka_benkyo/items/5840a36d0e97a8498388

studymemo/8幾何学的変換.ipynb

https://github.com/tanakakao/studymemo/blob/main/8%E5%B9%BE%E4%BD%95%E5%AD%A6%E7%9A%84%E5%A4%89%E6%8F%9B.ipynb
"""
import os, sys, time
import numpy as np
from numpy.random import normal
import scipy as sp
import cv2
import argparse
import matplotlib
matplotlib.use('TkAgg')
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

def img_read(img_file):
    img_bgr = cv2.imread(img_file)
    h, w = img_bgr.shape[:2]
    scale = (640 * 427 / (w * h)) ** 0.8
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)

    return img_bgr_resize, img_rgb, img_gray

def linear(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    x1 = img_rgb.shape[1]
    x2 = img_rgb.shape[0]

    x_scale = [2,2,1,3]
    y_scale = [1,2,2,1]

    fig, ax = plt.subplots(1, 4, figsize=(11, 8))
    
    for i in range(0,4):
        dst = cv2.resize(img_rgb, (x1*x_scale[i], x2*y_scale[i]))
        ax[i].imshow(dst)
        ax[i].set_title('x_scale={} y_scale={}'.format(str(x_scale[i]), str(y_scale[i])))
        ax[i].set_xticks([])
        ax[i].set_yticks([])
    
    plt.tight_layout()    
    plt.show()

    cv2.waitKey()

def rotation(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    width, height = img_rgb.shape[1], img_rgb.shape[0]
    
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    center = (0, height)
    
    affine_trans = cv2.getRotationMatrix2D(center, -30.0, 1.0)
    dst = cv2.warpAffine(img_rgb, affine_trans, (width, height), flags=cv2.INTER_CUBIC)
    ax[0].imshow(dst);
    ax[0].set_xticks([]);
    ax[0].set_yticks([]);

    affine_trans = cv2.getRotationMatrix2D(center, 20.0, 1.0)
    dst = cv2.warpAffine(img_rgb, affine_trans, (width, height))
    ax[1].imshow(dst);
    ax[1].set_xticks([]);
    ax[1].set_yticks([]);
    
    plt.tight_layout()    
    plt.show()

    cv2.waitKey()

def flip(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    width = img_rgb.shape[1]
    height = img_rgb.shape[0]

    fig, ax = plt.subplots(1, 4, figsize=(14, 5))

    center = (int(width/2), int(height/2))
    ax[0].imshow(img_rgb)
    ax[0].set_xticks([])
    ax[0].set_yticks([])

    flip_n = [0, 1, -1]

    for i in range(1,4):
        dst = cv2.flip(img_rgb, flip_n[i-1])
        ax[i].imshow(dst)
        ax[i].set_title('flip={}'.format(str(flip_n[i-1])))
        ax[i].set_xticks([])
        ax[i].set_yticks([])
    
    plt.tight_layout()    
    plt.show()

    cv2.waitKey()

def skew(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    width = img_rgb.shape[1]
    height = img_rgb.shape[0]

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    mat = np.array([[1, 0, 0], [0.3, 1, 0]], dtype=np.float32)
    dst = cv2.warpAffine(img_rgb, mat, (width, int(height + width * 0.3)))
    ax[0].imshow(dst);
    ax[0].set_xticks([]);
    ax[0].set_yticks([]);

    mat = np.array([[1, 0.6, 0], [0, 1, 0]], dtype=np.float32)
    dst = cv2.warpAffine(img_rgb, mat, (int(width + height * 0.6), height))
    ax[1].imshow(dst);
    ax[1].set_xticks([]);
    ax[1].set_yticks([]);

    plt.tight_layout()    
    plt.show()

    cv2.waitKey()

def parllel_shift(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    width = img_rgb.shape[1]
    height = img_rgb.shape[0]

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    mat = np.array([[1, 0, 80], [0, 1, 20]], dtype=np.float32)
    dst = cv2.warpAffine(img_rgb, mat, (width, height))
    ax[0].imshow(dst);
    ax[0].set_xticks([]);
    ax[0].set_yticks([]);

    mat = np.array([[1, 0, -20], [0, 1, -50]], dtype=np.float32)
    dst = cv2.warpAffine(img_rgb, mat, (width, height))
    ax[1].imshow(dst);
    ax[1].set_xticks([]);
    ax[1].set_yticks([]);

    plt.tight_layout()    
    plt.show()

    cv2.waitKey()

def affine_transform(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    height, width = img_rgb.shape[0], img_rgb.shape[1]

    a = [1, 2, 3]
    b = [4, -2, -5]
    c = [4, 0.5, 2]
    d = [-3, 2, 0]

    tx = [10, 1400, 1000]
    ty = [30, 0, 200]

    fig, ax = plt.subplots(1, 3, figsize=(13, 5))

    for i in range(3):
        mat = np.array([[a[i], b[i], tx[i]], [c[i], d[i], ty[i]]], dtype=np.float32)
        dst = cv2.warpAffine(img_rgb, mat, (7*width, 7*height))
        ax[i].imshow(dst)
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    plt.tight_layout()    
    plt.show()

    cv2.waitKey()    

def euclidean_transform(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)
    height, width = img_rgb.shape[0], img_rgb.shape[1]

    thetas = [np.pi/6, -np.pi/3, np.pi/4]
    c = np.cos(thetas)
    s = np.sin(thetas)

    tx = [20, 70, 50]
    ty = [-100, 150, -150]

    fig, ax = plt.subplots(1, 3, figsize=(13, 5))

    for i in range(3):
        mat = np.array([[c[i], -s[i], tx[i]], [s[i], c[i], ty[i]]], dtype=np.float32)
        dst = cv2.warpAffine(img_rgb, mat, (width, height))
        ax[i].imshow(dst)
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    plt.tight_layout()    
    plt.show()

    cv2.waitKey()  

def similar_transform(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)
    height, width = img_rgb.shape[0], img_rgb.shape[1]

    thetas = [np.pi/6, -np.pi/3, np.pi/4]
    c = np.cos(thetas)
    s = np.sin(thetas)
    p = [4, 2, 3]

    tx = [20, 150, 50]
    ty = [-150, 100, -150]

    fig, ax = plt.subplots(1, 3, figsize=(13, 5))

    for i in range(3):
        mat = np.array([[p[i]*c[i], -p[i]*s[i], tx[i]], [p[i]*s[i], p[i]*c[i], ty[i]]], dtype=np.float32)
        dst = cv2.warpAffine(img_rgb, mat, (width, height))
        ax[i].imshow(dst)
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    plt.tight_layout()    
    plt.show()

    cv2.waitKey()  

def projective_transform(img_file):
    img_bgr_resize, img_rgb, img_gray = img_read(img_file)

    #x1 = img_rgb.shape[1]
    #x2 = img_rgb.shape[0]
    height, width = img_rgb.shape[0], img_rgb.shape[1]

    pts1 = np.float32([[0,0], 
                       [width,0], 
                       [0,height], 
                       [width,height]])
    
    pts2 = np.float32([[0,0], 
                       [width,50], 
                       [0,height], 
                       [width,250]])

    #M, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
    M = cv2.getPerspectiveTransform(pts1, pts2)

    dst = cv2.warpPerspective(img_rgb, M, (width, height))
    plt.imshow(dst)
    plt.xticks([]);
    plt.yticks([]);

    plt.tight_layout()    
    plt.show()

    cv2.waitKey()  

def trim_image(img_file):
    #img_bgr_resize, img_rgb, img_gray = img_read(img_file)
    img_bgr = cv2.imread(img_file)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img1 = img_rgb[0:400, 0:400]
    img2 = img_rgb[10:350, 250:700]

    #x1 = img2.shape[1]
    #x2 = img2.shape[0]
    height, width = img_rgb.shape[0], img_rgb.shape[1]

    pts1 = np.float32([[0,0], 
                       [width,0],
                       [0,height],
                       [width,height]])
    
    pts2 = np.float32([[0,0], 
                       [width,30], 
                       [0,height], 
                       [width,280]])

    #M, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
    M = cv2.getPerspectiveTransform(pts1, pts2)

    img2 = cv2.warpPerspective(img2, M, (width, height))

    fig, ax = plt.subplots(1, 1, figsize=(10, 4))

    plt.imshow(img1);
    plt.axis('off')
    #plt.set_xticks([]);
    #plt.set_yticks([]);
    # Save the frame to a file
    filename0 = f'media/30_10_mosic_0.jpg'
    #cv2.imwrite(filename, img1)
    plt.savefig(filename0, bbox_inches='tight', pad_inches = 0)
    plt.show()

    plt.imshow(img2);
    plt.axis('off')
    #ax[1].set_xticks([]);
    #ax[1].set_yticks([]);
    # Save the frame to a file
    filename1 = f'media/30_10_mosic_1.jpg'
    #cv2.imwrite(filename, img2)
    plt.savefig(filename1, bbox_inches='tight', pad_inches = 0)
    
    #plt.tight_layout()    
    plt.show()

    return filename0, filename1
    cv2.waitKey()  
"""
Can't use SURF, SIFT in OpenCV
https://stackoverflow.com/questions/18561910/cant-use-surf-sift-in-opencv

uninstall all the opencv versions

python -m pip uninstall opencv-python
python -m pip uninstall opencv-contrib-python

after that install opencv-contrib to include sift() and surf() using below given command with python(3.x)
python -m pip uninstall opencv-python==3.4.2.17
python -m pip install opencv-contrib-python==3.4.2.17

then you can use
sift = cv2.xfeatures2d.SIFT_create()
"""

"""
Python bindings for OpenCV with AttributeError: 'module' object has no attribute 'FeatureDetector_create'
https://stackoverflow.com/questions/14646692/python-bindings-for-opencv-with-attributeerror-module-object-has-no-attribute

Regarding the 3.1 version, these functions have been removed in favor of functions like

detector = cv2.TYPE_create()

detector=cv2.xfeatures2d.SURF_create()
"""

"""
Where did SIFT and SURF go in OpenCV 3?
by Adrian Rosebrock on July 16, 2015

https://pyimagesearch.com/2015/07/16/where-did-sift-and-surf-go-in-opencv-3/
"""

"""
BRIEF (Binary Robust Independent Elementary Features) 
https://docs.opencv.org/3.4/dc/d7d/tutorial_py_brief.html

"""
"""
How to install tkinter for python 3.9 on xubuntu 20.04?

https://askubuntu.com/questions/1397737/how-to-install-tkinter-for-python-3-9-on-xubuntu-20-04

step 1:
http://ftp.de.debian.org/debian/pool/main/p/python3-stdlib-extensions/python3-tk_3.7.3-1_amd64.deb

setp 2:
extract it with any Archive Manager. Continue to extract the data.tar.xz inside.
tar -xf data.tar.xz

setp 3: to copy _tkinter.cpython-37m-x86_64-linux-gnu.so that file to the correct folder of your python installation.
sudo cp ./usr/lib/python3.7/lib-dynload/_tkinter.cpython-37m-x86_64-linux-gnu.so /usr/local/lib/python3.7/lib-dynload/
"""


def image_mosaicing(img_file):
    img1_path, img2_path =trim_image(img_file)
    
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
 
    detector = cv2.xfeatures2d.SURF_create()#cv2.FeatureDetector_create("SURF") 
    # Initiate BRIEF extractor
    descriptor = cv2.xfeatures2d.BriefDescriptorExtractor_create()#cv2.DescriptorExtractor_create("BRIEF")
    
    matcher = cv2.DescriptorMatcher_create("BruteForce-Hamming")
 
    # detect keypoints
    kp1 = detector.detect(img1)
    kp2 = detector.detect(img2)
 
    # descriptors
    k1, d1 = descriptor.compute(img1, kp1)
    k2, d2 = descriptor.compute(img2, kp2)
 
    # match the keypoints
    matches = matcher.match(d1, d2)
 
    # visualize the matches
    dist = [m.distance for m in matches]

    # threshold: half the mean
    thres_dist = (sum(dist) / len(dist)) * 0.9
 
    # keep only the reasonable matches
    sel_matches = [m for m in matches if m.distance < thres_dist]
 
    point1 = [[k1[m.queryIdx].pt[0], k1[m.queryIdx].pt[1]] for m in sel_matches]
    point2 = [[k2[m.trainIdx].pt[0], k2[m.trainIdx].pt[1]] for m in sel_matches]
 
    point1 = np.array(point1)
    point2 = np.array(point2)
 
    H, Hstatus = cv2.findHomography(point2,point1,cv2.RANSAC)
 
    # 移動量を算出
    x=0
    y=0
    cnt=0
    for i,v in enumerate(Hstatus):
        if v==1:
            x += point1[i][0]-point2[i][0]
            y += point1[i][1]-point2[i][1]
            cnt += 1

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
 
    x = abs(int(round(x/cnt)))
    y = abs(int(round(y/cnt)))
 
    # sizeを取得
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
 
    dst = cv2.warpPerspective(img2,H,(w2+x,h2+y))
 
    for i in range(w1):
        for j in range(h1):
            dst[j,i] = img1[j,i]

def image_mosaicing2(img_file):
    img1_path, img2_path =trim_image(img_file)
    
    #img1 = cv2.imread(img1_path, cv2.IMREAD_COLOR)
    #img2 = cv2.imread(img2_path, cv2.IMREAD_COLOR)

    img_bgr = cv2.imread(img1_path)
    img1 = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_bgr = cv2.imread(img2_path)
    img2 = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    detector = cv2.AKAZE_create()
    matcher = cv2.DescriptorMatcher_create("BruteForce-Hamming")

    k1, d1 = detector.detectAndCompute(img1,None)
    k2, d2 = detector.detectAndCompute(img2,None)

    match = cv2.BFMatcher()
    matches = match.knnMatch(d2, d1, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.8* n.distance:
            good.append(m)

    MIN_MATCH_COUNT = 10
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([ k2[m.queryIdx].pt for m in good ])
        dst_pts = np.float32([ k1[m.trainIdx].pt for m in good ])
        H = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)[0]
    else:
        print('Not enought matches are found - {}/{}'.format(len(good), MIN_MATCH_COUNT))
        exit(1)

    img2_warped = cv2.warpPerspective(img2, H, (img1.shape[1] + img2.shape[1], img1.shape[0]))

    img_stitched = img2_warped.copy()
    img_stitched[:img1.shape[0], :img1.shape[1]] = img1

    def trim(frame):
        if np.sum(frame[0]) == 0:
            return trim(frame[1:])
        if np.sum(frame[-1]) == 0:
            return trim(frame[:-2])
        if np.sum(frame[:,0]) == 0:
            return trim(frame[:, 1:])
        if np.sum(frame[:,-1]) == 0:
            return trim(frame[:, :-2])
        return frame
    
    img_stitched_trimmed = trim(img_stitched)

    
    img_key = cv2.drawKeypoints(img2, k2, None)

    draw_params = dict(matchColor=(0,255,0),
                   singlePointColor=None,
                   flags=2)
    
    img_match = cv2.drawMatches(img1, k1, img2, k2,  good, None, **draw_params)

    plt.imshow(img_match)
    plt.show()
    
    plt.imshow(img_stitched_trimmed)

    plt.show()
    cv2.waitKey()  

def main(img_file):
    projective_transform(img_file)
    similar_transform(img_file)
    euclidean_transform(img_file)
    affine_transform(img_file)
    parllel_shift(img_file)
    skew(img_file)
    flip(img_file)
    rotation(img_file)
    linear(img_file)
    trim_image(img_file)
    '''
    '''
    
    image_mosaicing2(img_file)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='30_2_geometric_transformations')
   
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
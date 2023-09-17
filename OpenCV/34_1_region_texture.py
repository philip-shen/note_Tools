"""
python+opencvで画像処理の勉強7 領域処理

https://qiita.com/tanaka_benkyo/items/0a607c01fcbe8e0a934f

studymemo/10領域処理.ipynb
https://github.com/tanakakao/studymemo/blob/main/10%E9%A0%98%E5%9F%9F%E5%87%A6%E7%90%86.ipynb
"""
import os, sys, time
import argparse 

import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from skimage.feature import greycomatrix, greycoprops
from mpl_toolkits.mplot3d import Axes3D
from sklearn import cluster
from sklearn.cluster import estimate_bandwidth #MeanShift,
import matplotlib.cm as cm

from skimage.segmentation import active_contour
from skimage.filters import gaussian

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

def read_image(img_file, scale_value=0.8):
    img_bgr = cv2.imread(img_file)
    h, w = img_bgr.shape[:2]
    scale = (640 * 480 / (w * h)) ** scale_value#0.5
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)
    return img_rgb, img_gray

'''
2次元フーリエ変換の結果を用いて、パワースペクトル、その極座標を求める。
さらに、幅を持つ角度\thetaの扇状領域と、幅を持つ半径の同心円状領域を、以下の式により求める。 
'''
def draw_polar():
    theta = np.arange(0,2*np.pi+0.01, 0.01)

    x=np.cos(theta)
    y=np.sin(theta)

    fig, ax = plt.subplots(1, 2, figsize=(7, 3))

    ax[0].plot(x, y, '--');
    ax[0].plot([x[375], x[60]], [y[375], y[60]], 'red');
    ax[0].plot([x[395], x[80]], [y[395], y[80]], 'red');
    ax[0].plot(x[60:81], y[60:81], 'red');
    ax[0].plot(x[375:396], y[375:396], 'red');

    ax[0].plot([x[475], x[160]], [y[475], y[160]], 'red');
    ax[0].plot([x[495], x[180]], [y[495], y[180]], 'red');
    ax[0].plot(x[160:181], y[160:181], 'red');
    ax[0].plot(x[475:496], y[475:496], 'red');

    ax[1].plot(x, y, '--');

    ax[1].plot(x*10/20, y*10/20, 'red');
    ax[1].plot(x*11/20, y*11/20, 'red');
    ax[1].plot(x*12/20, y*12/20, 'red');
        
    plt.show()

    cv2.waitKey(0)
    
def make_power_sp(img):
    """パワースペクトル"""
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    return magnitude_spectrum

def make_polar_img(img):
    """極座標へのマッピング"""
    h = img.shape[0]
    w = img.shape[1]
    
    l = np.sqrt(w*w + h*h)
    m = l/np.log(l)

    center = (w/2, h/2)
    flags = cv2.INTER_LANCZOS4 + cv2.WARP_POLAR_LOG
    p_a = cv2.warpPolar(img, (w, h), center, m, flags)
    return p_a

def texture(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    img_rgb2, img_gray2 = read_image(img_files[1])
    img_rgb3, img_gray3 = read_image(img_files[2])
    
    imgs = np.array([img_gray1, img_gray2, img_gray3])

    fig,ax = plt.subplots(3, 3, figsize=(8, 8), subplot_kw=({"xticks":(), "yticks":()}))
    for i in range(3):
        ft_img = make_power_sp(imgs[i])
        p_img = make_polar_img(ft_img)
    
        ax[0][i].imshow(imgs[i], cmap = 'gray')
        ax[1][i].imshow(ft_img, cmap = 'viridis')
        ax[2][i].imshow(p_img, cmap = 'viridis')
        ax[2][i].set_xlabel('r')
        ax[2][i].set_ylabel('theta')

    plt.legend()
    plt.tight_layout()    
    plt.show()

    cv2.waitKey(0)

def gabor_filter(img_files):
    # cv2.getGaborKernel((ksize, sigma, theta, lambd, gamma, psi)
    # ksize　フィルタのサイズ
    # sigma　波の出てくる幅
    # theta　角度
    # lambd　波長
    # gamma　広がり
    # psi　位相

    thetas = [0, -22.5, -45, -67.5, -90, -112.5, -135, -157.5]

    fig, ax = plt.subplots(2, 4, figsize=(12, 6), subplot_kw=({"xticks":(), "yticks":()}))
    for i in range(8):
        gabor = cv2.getGaborKernel((20, 20), 2, np.radians(thetas[i]), 3, 0.6, 0)
        ax[i//4][i%4].imshow(gabor, 'gray')
    plt.show()

    for i in range(8):
        gabor = cv2.getGaborKernel((20, 20), 2, np.radians(thetas[i]), 2, 0.6, 0)
        ax[i//4][i%4].imshow(gabor, 'gray')    
    plt.show()

    img_rgb3, img_gray3 = read_image(img_files[2])        
    fig, ax = plt.subplots(2, 4, figsize=(16, 8), subplot_kw=({"xticks":(), "yticks":()}))
    sum_img = np.zeros(img_gray3.shape)
    for i in range(8):
        gabor = cv2.getGaborKernel((20, 20), 2, np.radians(thetas[i]), 3, 0.6, 0)
        dst = cv2.filter2D(img_gray3, -1, gabor)
        sum_img += dst
        ax[i//4][i%4].imshow(dst, 'gray')
    
    plt.show()    

    plt.imshow(sum_img, 'gray');


def make_glcm_features(input_image, feature):
    glcm_feature = np.zeros((input_image.shape[0], input_image.shape[1]))

    for i in range(input_image.shape[0] ):
        #if i % 10 == 0:
        #    print(i)import os, sys, time

        for j in range(input_image.shape[1] ):
            # 境界値処理
            if i <3 or j <3 or i > input_image.shape[0] - 4 or j > input_image.shape[1] - 4:
                glcm_feature[i,j]= 0
                continue
            # 7x7のウィンドウで画像を切り取る
            glcmWindow = input_image[i-3: i+4, j-3 : j+4]
            # 0度と90度の同時生起行列を計算する
            glcm_x = greycomatrix(glcmWindow, [1], [0], levels=256, symmetric=True)
            glcm_y = greycomatrix(glcmWindow, [1], [90], levels=256, symmetric=True)
            # テクスチャ特徴量を計算
            texture_feature_x = greycoprops(glcm_x, feature)
            texture_feature_y = greycoprops(glcm_y, feature)
            glcm_feature[i,j] = (texture_feature_x + texture_feature_y)/2
    return glcm_feature

def show_glcm(features, feature_names):
    fig, ax = plt.subplots(2, 3, figsize=(12, 8), subplot_kw=({"xticks":(), "yticks":()}))
    for i in range(6):
        ax[i//3][i%3].imshow(features[i])
        ax[i//3][i%3].set_title(feature_names[i])

    plt.show()

def glcm_features(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    feature_names = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'ASM', 'correlation']
    glcm_feature = np.array([make_glcm_features(img_gray, feature_name) for feature_name in feature_names])

    show_glcm(glcm_feature, feature_names)    

def feature_table_3D(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    rgb_img = img_rgb.copy()

    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(rgb_img)

    plt.subplot(1, 2, 2)
    ax = fig.add_subplot(122, projection='3d')
    ax.scatter3D(rgb_img[:,:,0], rgb_img[:,:,1], rgb_img[:,:,2])
    
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)

    return rgb_img

def mean_shift_k_mean(img_file):
    rgb_img = feature_table_3D(img_file)    
    
    rgb0 = rgb_img[:,:,0]
    rgb1 = rgb_img[:,:,1]
    rgb2 = rgb_img[:,:,2]
    x1 = range(0,rgb_img.shape[1])
    x2 = range(0,rgb_img.shape[0])
    x1, x2 = np.meshgrid(x1,x2)

    rgb = np.array([rgb0, rgb1, rgb2, x1, x2]).reshape(5,rgb_img.shape[0]*rgb_img.shape[1])
    df = pd.DataFrame(rgb.T)
    df.columns = ['red', 'green', 'blue', 'x1', 'x2']

    print(df.head())

    # k-means
    km=cluster.KMeans(n_clusters=5)
    z_km=km.fit(df)
    print('2nd test!!!')

    # MeanShift
    bwidth = estimate_bandwidth(df.values, quantile=0.15, n_samples=200)
    ms = cluster.MeanShift(seeds=df.values, bandwidth=bwidth)
    ms.fit(df.values)
    print('3rd test!!!')
    
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    print(cluster_centers)
    
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    '''
    ax[0].scatter(df["red"], df["blue"], c=cm.hsv(ms.labels_/len(ms.cluster_centers_)))
    ax[0].scatter(ms.cluster_centers_[:,0], ms.cluster_centers_[:,2],s=250, marker='*',c='orange')
    ax[0].set_title("Mean Shift");

    ax[1].scatter(df["red"], df["blue"], c=cm.hsv(z_km.labels_/len(z_km.cluster_centers_)))
    ax[1].scatter(z_km.cluster_centers_[:,0],z_km.cluster_centers_[:,2],s=250, marker='*',c='orange')
    ax[1].set_title("k-means");
    '''
    
    ax[0].scatter(df["red"], df["blue"], c=labels)
    for i in range(len(cluster_centers)):
        ax[0].plot(cluster_centers[i,0], cluster_centers[i,2], 
                   marker='*',c='red', markersize=14)
    ax[0].set_title("Mean Shift");

    ax[1].scatter(df["red"], df["blue"], c=z_km.labels_)
    ax[1].scatter(z_km.cluster_centers_[:,0],
                  z_km.cluster_centers_[:,2],
                  s=250, marker='*',c='red')
    ax[1].set_title("k-means");
    
    '''
    img_rgb, img_gray = read_image(img_file)
    rgb_img = img_rgb.copy()

    fig, ax = plt.subplots(1, 3, figsize=(20, 10), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0].imshow(rgb_img)
    ax[1].imshow(labels.reshape(rgb_img.shape[0],rgb_img.shape[1]),cmap='hsv')
    ax[1].set_title("Mean Shift");
    ax[2].imshow(z_km.labels_.reshape(rgb_img.shape[0],rgb_img.shape[1]),cmap='hsv')
    ax[2].set_title("k-means");
    '''

    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)

def show_activecontour(img_file):
    #img_rgb1, img_gray1 = read_image(img_files[0])
    img_rgb2, img_gray2 = read_image(img_file)

    s = np.linspace(0, 2*np.pi, 400)
    r = 280 + 120*np.sin(s)
    c = 580 + 180*np.cos(s)
    init = np.array([r, c]).T

    snake = active_contour(gaussian(img_gray2, 3, preserve_range=False), init, alpha=0.015, beta=10, gamma=0.001)

    plt.imshow(img_rgb2)
    plt.plot(snake[:,1],snake[:,0])
    plt.plot(init[:, 1], init[:, 0])

    plt.show()
    cv2.waitKey(0)

def graph_cut(img_file):
    img_rgb, img_gray = read_image(img_file, scale_value=0.9)
    img = img_rgb.copy()

    mask = np.zeros(img.shape[:2],np.uint8)
    newmask=np.zeros(img.shape[:2],np.uint8)
    newmask[150:151,150:250] = 1

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = (90,90,280,200)
    mask, bgdModel, fgdModel = cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    result = img*mask2[:,:,np.newaxis]

    cv2.rectangle(img, (90,90), (280,200), (255, 0, 0))

    fig, ax = plt.subplots(1, 2, figsize=(15, 5), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0].imshow(img);
    ax[1].imshow(mask2);    
    ax[2].imshow(result);

"""
OpenCV Python: cv2.findContours - ValueError: too many values to unpack

https://stackoverflow.com/questions/25504964/opencv-python-cv2-findcontours-valueerror-too-many-values-to-unpack

contours, hierarchy = cv2.findContours(
    skin_ycrcb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

Explanation: By using [-2:], we are basically taking the last two values from the tuple returned by cv2.findContours. 
Since in some versions, it returns (image, contours, hierarchy) and 
in other versions, it returns (contours, hierarchy), contours, hierarchy are always the last two values.
"""

def show_watershed(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    # 2値化
    ret, thresh = cv2.threshold(img_gray,170,255,cv2.THRESH_BINARY_INV)

    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    sure_bg = cv2.dilate(opening,kernel,iterations=3)

    # 距離画像
    dist_transform = cv2.distanceTransform(sure_bg,cv2.DIST_L2,3)
    # 2値化
    ret, sure_fg = cv2.threshold(dist_transform,0.28*dist_transform.max(),255,0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)

    # ラベリング
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers+1
    markers[unknown==255] = 0

    markers = cv2.watershed(img_rgb, markers)
    img_rgb[markers == -1] = [255,0,0]
    
    
    contours, hierarchy = cv2.findContours(markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    for i in range(len(contours)):
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(img_rgb, contours, i, (255, 0, 0), 1)

    fig = plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(markers)
    
    plt.subplot(1, 2, 2)
    plt.imshow(img_rgb);
    
    plt.legend()
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)

def main(img_file):
    #glcm_features(img_file)
    '''
    draw_polar()
    feature_table_3D(img_file)
    '''
    #mean_shift_k_mean(img_file)
    #show_activecontour(img_file)
    show_watershed(img_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='33_rinkaku')
   
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
    
    '''
    img_files = ['media/penguin-03_800.jpg', 
                 'media/ema_01_800.jpg', 
                 'media/hura_house_02.png']
    texture(img_files)
    '''
    
    est_timer(start_time=t0)
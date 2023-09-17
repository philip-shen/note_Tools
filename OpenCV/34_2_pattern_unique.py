"""
python+opencvで画像処理の勉強8 パターン・図形・特徴の検出とマッチング
https://qiita.com/tanaka_benkyo/items/f65ffabc32538020ba20

studymemo/11パターン・図形・特徴の検出とマッチング.ipynb
https://github.com/tanakakao/studymemo/blob/main/11%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%83%BB%E5%9B%B3%E5%BD%A2%E3%83%BB%E7%89%B9%E5%BE%B4%E3%81%AE%E6%A4%9C%E5%87%BA%E3%81%A8%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0.ipynb
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import os, sys, time
import argparse

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

def read_image(img_file, scale_value=0.5):
    
    img_bgr = cv2.imread(img_file)
    h, w = img_bgr.shape[:2]
    scale = (640 * 480  / (w * h)) ** scale_value#0.5
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)
    return img_rgb, img_gray

def template_match(img_file):
    img_rgb1, img_gray1 = read_image(img_file, scale_value=0.8)
    
    templ = img_rgb1[260:315,1100:1270]
    test = img_rgb1.copy()
    
    result = cv2.matchTemplate(test, templ, cv2.TM_CCOEFF_NORMED)
    mmr = cv2.minMaxLoc(result)
    pos = mmr[3]
    '''
    INFO: mmr: (-0.824735164642334, 0.9999995231628418, (1063, 29), (1100, 260))
    '''
    logger.info(f'mmr: {mmr}')
    
    
    dst = test.copy()
    cv2.rectangle(dst, pos, (pos[0] + templ.shape[1], pos[1] + templ.shape[0]), (0, 255, 0), 2)
    '''
    INFO: pos: (1100, 260)
    INFO: pos[0]: 1100; pos[1]: 260
    INFO: templ.shape[1]: 170; templ.shape[0]: 55
    '''
    logger.info(f'pos: {pos}')
    logger.info(f'pos[0]: {pos[0]}; pos[1]: {pos[1]}')
    logger.info(f'templ.shape[1]: {templ.shape[1]}; templ.shape[0]: {templ.shape[0]}')

    fig, ax = plt.subplots(1, 3, figsize=(10, 6), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0].imshow(templ);
    ax[1].imshow(result);
    ax[2].imshow(dst);
    
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)

def edge_info(img_file):
    img_rgb1, img_gray1 = read_image(img_file, scale_value=0.8)
    
    # 2値化処理
    ret, thresh = cv2.threshold(img_gray1, 100, 255, cv2.THRESH_BINARY)
    test = thresh.copy()
    test = cv2.bitwise_not(cv2.Sobel(test, -1, 1, 1, ksize=3))

    # 距離画像
    dist_test = cv2.distanceTransform(test,cv2.DIST_L2,3)

    # テンプレート画像の作成
    templ = thresh[275:315,1100:1270].copy()
    templ = cv2.bitwise_not(cv2.Sobel(templ, -1, 1, 1, ksize=5)).astype('float32')
    
    # テンプレートマッチング
    # 距離画像に対して、エッジ画像のテンプレートでマッチング
    result = cv2.matchTemplate(dist_test, templ, cv2.TM_CCOEFF_NORMED)
    mmr = cv2.minMaxLoc(result)
    pos = mmr[3]

    dst = img_rgb1.copy()
    cv2.rectangle(dst, pos, (pos[0] + templ.shape[1], pos[1] + templ.shape[0]), (0, 255, 0), 2)

    fig, ax = plt.subplots(2, 2, figsize=(10, 6), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0][0].imshow(templ, 'gray')
    ax[1][0].imshow(dist_test);
    ax[1][1].imshow(result);
    ax[0][1].imshow(dst);
    
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)

def calc_hists(img_rgb, n_bins, hist_range):
    img = img_rgb[:,:,0]*256**2+img_rgb[:,:,1]*256+img_rgb[:,:,2]
    img = img.reshape(img_rgb.shape[0],img_rgb.shape[1],1)
    
    hist = cv2.calcHist([img.astype('uint8')], channels=[0], mask=None, histSize=[n_bins], ranges=hist_range)
    hist = hist.squeeze(axis=-1)
    return hist

def calc_compare(hist1, hist2):
    hist_norm1 = hist1 / hist1.sum()
    hist_norm2 = hist2 / hist2.sum()
    
    print('相関: ',cv2.compareHist(hist1, hist2, method=cv2.HISTCMP_CORREL))
    print('カイ2乗: ',cv2.compareHist(hist_norm1, hist_norm2, method=cv2.HISTCMP_CHISQR))
    print('交差(ヒストグラムインタセクション): ',cv2.compareHist(hist_norm1, hist_norm2, method=cv2.HISTCMP_INTERSECT))
    print('Bhattacharyya距離: ',cv2.compareHist(hist_norm1, hist_norm2, method=cv2.HISTCMP_BHATTACHARYYA))


def make_post_lut(n):
    """
    ポスタリゼーション用のLUTを作成
    """
    x = np.arange(256)
    y = np.floor(x/n)*int(255/np.floor(255/n))
    y = y.astype('uint8')
    return y

def aa(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    img_rgb2, img_gray2 = read_image(img_files[1])
    img_rgb3, img_gray3 = read_image(img_files[2])

    y=make_post_lut(16)

    for i in range(3):
        img_rgb1[:,:,i] = img_lut = cv2.LUT(img_rgb1[:,:,i], y)
        img_rgb2[:,:,i] = img_lut = cv2.LUT(img_rgb2[:,:,i], y)
        img_rgb3[:,:,i] = img_lut = cv2.LUT(img_rgb3[:,:,i], y)

    fig, ax = plt.subplots(1, 3, figsize=(15, 6), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0].imshow(img_rgb1);
    ax[1].imshow(img_rgb2);
    ax[2].imshow(img_rgb3);

def make_color_number(img):
    return img[:,:,0]*256**2+img[:,:,1]*256+img[:,:,2]

def bb(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    img_rgb2, img_gray2 = read_image(img_files[1])

    img1 = make_color_number(img_rgb1).reshape(img_rgb1.shape[0],img_rgb1.shape[1],1)
    img2 = make_color_number(img_rgb2).reshape(img_rgb1.shape[0],img_rgb1.shape[1],1)

    n_bins = 256**3  # ビンの数
    hist_range = [0, 256**3]  # 集計範囲

    hist1 = cv2.calcHist([img1.astype('uint8')], channels=[0], mask=None, histSize=[n_bins], ranges=hist_range)
    hist_norm1 = hist1 / hist1.sum()
    hist_norm1 = hist_norm1.squeeze(axis=-1)
    hist1 = hist1.squeeze(axis=-1)

    hist2 = cv2.calcHist([img2.astype('uint8')], channels=[0], mask=None, histSize=[n_bins], ranges=hist_range)
    hist_norm2 = hist2 / hist2.sum()
    hist_norm2 = hist_norm2.squeeze(axis=-1)
    hist2 = hist2.squeeze(axis=-1)

    calc_compare(hist1, hist2)
    '''
    n_bins = 256**3  # ビンの数
    hist_range = [0, 256**3]  # 集計範囲

    hist1 = calc_hists(img_rgb1, n_bins, hist_range)
    hist2 = calc_hists(img_rgb2, n_bins, hist_range)
    hist3 = calc_hists(img_rgb3, n_bins, hist_range)
    print('img1 vs img2')
    calc_compare(hist1, hist2)
    print('\nimg1 vs img3')
    calc_compare(hist1, hist3)
    print('\nimg2 vs img3')
    calc_compare(hist2, hist3)
    '''

# FAST(Feature from Accelerated Segment Test) 
def coner_detect(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    gray = np.float32(img_gray)

    # ハリスのコーナー検出
    color1 = img_rgb.copy()
    dst = cv2.cornerHarris(gray, 7, 11, 0.05)
    dst = cv2.dilate(dst, None)
    color1[dst>0.02*dst.max()]=[0,0,255]

    # FASTによるコーナー検出
    color2 = img_rgb.copy()
    fast = cv2.FastFeatureDetector_create(threshold=25)
    kp = fast.detect(img_gray, None)
    color2 = cv2.drawKeypoints(color2, kp, None, color=(255,0,0))

    # Shi-Tomasiのコーナー検出
    color3 = img_rgb.copy()
    corners = cv2.goodFeaturesToTrack(gray,200,0.05,10)
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(color3,(x,y),3,255,-1)

    fig, ax = plt.subplots(1, 3, figsize=(15, 4), subplot_kw=({"xticks":(), "yticks":()}))

    ax[0].imshow(color1);
    ax[0].set_title('Harris')
    ax[1].imshow(color2);
    ax[1].set_title('FAST')
    ax[2].imshow(color3);
    ax[2].set_title('Shi-Tomasi')

def dog_log_doh(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    color = img_rgb.copy()
    gray = rgb2gray(img_rgb)

    # DoG
    blobs_dog = blob_dog(gray, max_sigma=30, threshold=.1)
    blobs_dog[:, 2] = blobs_dog[:, 2] * np.sqrt(2)

    # LoG
    blobs_log = blob_log(gray, max_sigma=30, num_sigma=10, threshold=.1)
    blobs_log[:, 2] = blobs_log[:, 2] * np.sqrt(2)

    # DoH
    blobs_doh = blob_doh(gray, max_sigma=30, threshold=.001)

    fig, ax = plt.subplots(1, 3, figsize=(15, 4), subplot_kw=({"xticks":(), "yticks":()}))

    titles = ['DoG','LoG','DoH']
    for i, blobs in enumerate([blobs_dog, blobs_log, blobs_doh]):
        color = img_rgb.copy()
        for blob in blobs:
            x,y,r = blob
            cv2.circle(color,(int(x),int(y)),radius=int(r),color=255, thickness=2)
        ax[i].imshow(color)
        ax[i].set_title(titles[i])
    
    plt.show()

def bb(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    color = img_rgb.copy()
    h, w = color.shape[:2]
    gray = rgb2gray(img_rgb)


    fig, ax = plt.subplots(1, 3, figsize=(16, 4), subplot_kw=({"xticks":(), "yticks":()}))

    for i, degree in enumerate([0.0,45.0,60.0]):
        affine_trans = cv2.getRotationMatrix2D((w//2,h//2), degree, 1.0)
    
        img = cv2.warpAffine(color, affine_trans, (w, h))
    
        detector = cv2.xfeatures2d.SIFT_create()
        kp = detector.detect(img, None)

        img=cv2.drawKeypoints(img,kp,gray,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        ax[i].imshow(img);

    plt.show()

def surf(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    color = img_rgb.copy()
    h, w = color.shape[:2]
    gray = rgb2gray(img_rgb)

    fig, ax = plt.subplots(1, 3, figsize=(16, 4), subplot_kw=({"xticks":(), "yticks":()}))

    for i, degree in enumerate([0.0,45.0,60.0]):
        affine_trans = cv2.getRotationMatrix2D((w//2,h//2), degree, 1.0)
    
        img = cv2.warpAffine(color, affine_trans, (w, h))
    
        detector = cv2.xfeatures2d.SURF_create()
        kp, des = detector.detect(img, None)

        img=cv2.drawKeypoints(img,kp,gray,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        ax[i].imshow(img);

    plt.show()

def kaze_akaze(img_file):
    img_rgb, img_gray = read_image(img_file)
    
    # KAZE特徴量
    kaze =cv2.KAZE_create()
    kp, des = kaze.detectAndCompute(img_rgb,None)
    img1 = cv2.drawKeypoints(img_rgb,kp,None,(255,0,0),4)

    # AKAZE特徴量
    akaze =cv2.AKAZE_create()
    kp, des = akaze.detectAndCompute(img_rgb,None)
    img2 = cv2.drawKeypoints(img_rgb,kp,None,(255,0,0),4)

    fig, ax = plt.subplots(1, 2, figsize=(10, 4), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0].imshow(img1);
    ax[0].set_title('KAZE')
    ax[1].imshow(img2);
    ax[1].set_title('AKAZE')

'''
2値特徴量

SIFT特徴量は計算に時間を要するというデメリットがあります。
そこで特徴量を2値ベクトルで表現する手法が提案されています。
BRIEFは、ランダムに選択された2点の画素値の差の符号かｒ2値特徴量を生成します。
ORBは、BRIEFの処理におけるサンプリングペアを教師なし学習で決定します。
BRISKは、BRIEFを発展させた方法で、スケール不変性と回転不変性を得ています。
'''
def cc(img_file):
    img_rgb, img_gray = read_image(img_file)

    method =[cv2.ORB_create(), cv2.BRISK_create()]
    method_names = ['ORB', 'BRISK']

    fig, ax = plt.subplots(1, 3, figsize=(16, 4), subplot_kw=({"xticks":(), "yticks":()}))

    # ORB BRISK
    for i in range(len(method)):
        color= img_rgb.copy()
    
        detector = method[i]
        kp = detector.detect(color, None)
    
        img=cv2.drawKeypoints(color, kp, color, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        ax[i].imshow(img);
        ax[i].set_title(method_names[i]);

    # BRIEF
    color= img_rgb.copy()
    star = cv2.xfeatures2d.StarDetector_create()
    brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
    kp = star.detect(color,None)
    kp, des = brief.compute(color, kp)
    img=cv2.drawKeypoints(color, kp, color, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    ax[2].imshow(img);
    ax[2].set_title('BRIEF');


    method =[cv2.SimpleBlobDetector_create(), cv2.MSER_create()]
    method_names = ['SimpleBlobDetector', 'MSER']

    fig, ax = plt.subplots(1, 2, figsize=(10, 4), subplot_kw=({"xticks":(), "yticks":()}))
    for i in range(len(method)):
        color = img_rgb.copy()
    
        detector = method[i]
        kp = detector.detect(color, None)
    
        img=cv2.drawKeypoints(color, kp, color, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        ax[i].imshow(img);
        ax[i].set_title(method_names[i]);
    
    plt.show()

def dd(img_file):
    img_rgb, img_gray = read_image(img_file)

    img = img_rgb.copy()
    templ = img_rgb[240:320, 150:300]

    # 2つの画像で特徴点の検出
    detector = cv2.KAZE_create()
    keypoints1, descriptor1 = detector.detectAndCompute(templ, None)
    keypoints2, descriptor2 = detector.detectAndCompute(img, None)

    # マッチング
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(descriptor1, descriptor2, k=2)

    # マッチング精度が高いもののみ抽出
    ratio = 0.5
    good = []
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good.append([m])

    dst = cv2.drawMatchesKnn(templ, keypoints1, img, keypoints2, good, None, flags=0)
    plt.imshow(dst, cmap="gray");
    plt.xticks([]);
    plt.yticks([]);

def line_detect(img_file):
    img_rgb, img_gray = read_image(img_file)

    img = img_rgb.copy()
    edges = cv2.Canny(img_gray,200,150,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/180,100)

    for rho,theta in lines[:,0,:]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    plt.imshow(img);
    plt.xticks([]);
    plt.yticks([]);

    '''
    確率的ハフ変換による直線検出例を示す。
    '''
    img = img_rgb.copy()
    edges = cv2.Canny(img_gray,250,150,apertureSize = 3)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength=80,maxLineGap=15)
    for x1,y1,x2,y2 in lines[:,0,:]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    
    plt.imshow(img);
    plt.xticks([]);
    plt.yticks([]);

def maru_detect(img_file):
    img_rgb, img_gray = read_image(img_file)

    img = cv2.medianBlur(img_gray,19)
    cimg = img_rgb.copy()

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,60,
                            param1=50,param2=30,
                            minRadius=30,maxRadius=130)
    
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,60,
    #                        param1=80,param2=50,
    #                        minRadius=0,maxRadius=0)
    
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
    plt.title("Circle Detection")
    plt.imshow(cimg)
    #plt.xticks([]); #plt.yticks([]);

    #plt.legend()
    plt.show()
    cv2.waitKey(0)

def static_saliency(img_file):
    img_rgb, img_gray = read_image(img_file)

    img = img_rgb.copy()
    method = [cv2.saliency.StaticSaliencySpectralResidual_create(),
              cv2.saliency.StaticSaliencyFineGrained_create()]

    method_name = ['StaticSaliencySpectralResidual',
                   'StaticSaliencyFineGrained']

    fig, ax = plt.subplots(1, 3, figsize=(15, 6), subplot_kw=({"xticks":(), "yticks":()}))
    ax[0].imshow(img_rgb)

    for i in range(2):
        saliency = method[i]

        (success, saliencyMap) = saliency.computeSaliency(img)
        saliencyMap = (saliencyMap * 255).astype("uint8")

        ax[i+1].imshow(saliencyMap, 'gray')
        ax[i+1].set_title(method_name[i])
    
    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)
    
def main(img_file):
    '''
    template_match(img_file)
    edge_info(img_file)
    
    static_saliency(img_file)
    '''
    maru_detect(img_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='34_2_pattern_unique')
   
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
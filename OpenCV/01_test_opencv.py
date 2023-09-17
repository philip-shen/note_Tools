import os, sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

strabspath=os.path.abspath(sys.argv[0])
strdirname=os.path.dirname(strabspath)
str_split=os.path.split(strdirname)
prevdirname=str_split[0]
dirnamelog=os.path.join(strdirname,"logs")

sys.path.append('./libs')

from logger_setup import *
from libs import lib_misc
from libs import lib_common

def gray_scale(path_image, opt_verbose="OFF"):
    gry_img = cv2.imread(path_image,  0) #imreadの第2引数に0を指定するとグレースケールで読み込み
 
    plt.gray() #matplotlibでグレースケールを使用する場合はグレースケールで読み込むように指定
    #plt.imshow(gry_img)
    #plt.show()

    return gry_img

def white_black(path_image, opt_verbose="OFF"):
    gry_img = cv2.imread(path_image, 0) #グレースケールで読み込み
    ret, threshold_img = cv2.threshold(gry_img, 100, 255, cv2.THRESH_OTSU) #第2,3引数は閾値、第4引数は手法のフラグ
 
    plt.gray() #matplotlibでグレースケールを使用する場合はグレースケールで読み込むように指定
    #plt.imshow(threshold_img)
    #plt.show()

    return gry_img

def trim(path_image, start_pos=None, opt_verbose="OFF"):
    img = cv2.imread(path_image)
    height = img.shape[0] #高さ
    width = img.shape[1] #幅

    if opt_verbose.lower() == 'on':
        logger.info(f'height: {height}; width: {width}; start_pos: {start_pos}')

    if start_pos != None:
        trim_img = img[start_pos:height, start_pos:width] #高さ(上)・幅(左)を100pixelずつ除く
        trim_img = cv2.cvtColor(trim_img, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
        #plt.imshow(trim_img)
        #plt.show()
        
        return trim_img
    
def resize(path_image, resize_times= None, opt_verbose="OFF"):
    img = cv2.imread(path_image)
    height = img.shape[0] #高さ
    width = img.shape[1] #幅

    if opt_verbose.lower() == 'on':
        logger.info(f'height: {height}; width: {width}')
        logger.info(f'resize_times: {resize_times}')

    
    if resize_times != None:
        resize_img = cv2.resize(img, (int(width*resize_times), int(height*resize_times))) #サイズを×0.5で縮小
 
        resize_img = cv2.cvtColor(resize_img, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
        #plt.imshow(resize_img)    
        #plt.show()

        return resize_img
    
def projective_transformation(path_image, opt_verbose="OFF"):
    img = cv2.imread(path_image)
    height, width, ch = img.shape #画像の大きさを取得
 
    #points1の座標からpoints2の座標に変換するため、座標を指定
    points1 = np.float32([[320,236],[1104,402],[12,332],[1053,640]])
    points2 = np.float32([[0,0],[1250,0],[0,500],[1250,500]])
 
    #透視変換の行列を求める
    M = cv2.getPerspectiveTransform(points1, points2)
 
    #画像を変換する
    dst = cv2.warpPerspective(img, M, (1250,500))
 
    dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
    #plt.imshow(dst)
    #plt.show()

    return dst 

def edge(path_image, opt_verbose="OFF"):
    img = cv2.imread(path_image, 0) #グレースケールで読み込み
    canny_img = cv2.Canny(img, 50, 110) #第2,3引数は閾値
 
    #plt.gray()
    #plt.imshow(canny_img)
    #plt.show()

    return canny_img

def tt(path_image, opt_verbose="OFF"):
    img = cv2.imread(path_image)
    gauss_img = cv2.GaussianBlur(img, (55,15), 0) #第2引数はカーネル、第3引数は標準偏差
 
    gauss_img = cv2.cvtColor(gauss_img, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
    #plt.imshow(gauss_img)
    #plt.show()

    return gauss_img

def mosaic(path_image, opt_verbose="OFF"):
    img = cv2.imread(path_image)
    orgsize = img.shape[:2][::-1]
 
    img = cv2.resize(img, (int(orgsize[0]/20), int(orgsize[1]/20))) #画像を1/20に縮小
    img = cv2.resize(img, orgsize) #画像を元のサイズに拡大
 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
    #plt.imshow(img)
    #plt.show()

    return img

def draw_line(path_image, opt_verbose="OFF"):
    img = cv2.imread(path_image)
    height = img.shape[0] #高さ
    width = img.shape[1] #幅
 
    img = cv2.line(img, (0,0), (width,height), (0,0,255), 5) #第2引数が始点、第3引数が終点、第4引数が色、第5引数が線の太さ
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
    #plt.imshow(img)
    #plt.show()

    return img

if __name__ == '__main__':
    path_img = './media/input-225x300.jpg'
    opt_verbose = "on"
    img = cv2.imread(path_img)
    
    logger_set(strdirname)
    
    '''
    cv2.imshow('Post',img)
    cv2.waitKey(0) #キー入力待ちにして待機(0は無期限待機)
    cv2.destroyAllWindows() #表示した画像表示ウィンドウを破棄

    plt.figure(figsize=(5, 5))  # 画像の表示サイズ
    plt.imshow(img)
    plt.show()    
    '''
    images = []

    image = gray_scale(path_img, opt_verbose)
    images.append(image)
    
    image = white_black(path_img, opt_verbose)
    images.append(image)
    
    image = trim(path_img,start_pos=50, opt_verbose=opt_verbose)
    images.append(image)
    
    image = resize(path_img,resize_times= 0.5, opt_verbose=opt_verbose)
    images.append(image)
    
    image = projective_transformation(path_img, opt_verbose)
    images.append(image)
    
    image = edge(path_img, opt_verbose)
    images.append(image)
    
    image = mosaic(path_img, opt_verbose)
    images.append(image)
    
    image = draw_line(path_img, opt_verbose)
    images.append(image)
    num_images = len(images)

    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    for i in range(num_images):
        plt.subplot(2, 4, i+1)
        #plt.imshow(np.transpose(images[i], (1, 2, 0)))  # チャンネルを一番後ろに
        #label = index2name[i]# cifar10_classes[labels[i]]
        #plt.title(label)
        plt.imshow(images[i])
        plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)  # ラベルとメモリを非表示に
    plt.show()    
import os, sys, time
import numpy as np
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

def Sobel_gradiant(f, direction = 1):
    soble_x = np.array([[1, -2, -1], [0, 0, 0], [1, 2, 1]])
    soble_y = np.array([[-1, 0, 1,], [-2, 0, 2], [-1, 0, 1]])
    if direction == 1:
        grad_x = cv2.filter2D(f, cv2.CV_32F, soble_x)
        gx = abs(grad_x)
        g = np.uint8(np.clip(gx, 0, 255))
    elif direction == 2:
        grad_y = cv2.filter2D(f, cv2.CV_32F, soble_y)
        gy = abs(grad_y)
        g = np.uint8(np.clip(gy, 0, 255))
    else:
        grad_x = cv2.filter2D(f, cv2.CV_32F, soble_x)
        grad_y = cv2.filter2D(f, cv2.CV_32F, soble_y)
        magnitude = abs(grad_x) + abs(grad_y)
        g = np.uint8(np.clip(magnitude, 0, 255))
    return g

def laplacian(f):
    temp = cv2.Laplacian(f, cv2.CV_32F) + 128
    g = np.uint8(np.clip(temp, 0, 255))
    return g

def composite_laplacian(f):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    temp = cv2.filter2D(f, cv2.CV_32F, kernel)
    g = np.uint8(np.clip(temp, 0, 255))
    return g

"""
pythonで一から画像処理 (3)エッジ検出、モルフォロジー変換
https://qiita.com/fugunoko/items/8997e3d160d8ed93eaa9

"""

def Sobel_LaplacianFilter(img_file):
    img = cv2.imread(img_file,0)

    #Laplacianフィルタ
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    #Sobelフィルタx方向
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=15)
    #Sobelフィルタy方向
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=15)

    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

def Canny(img_file):
    img = cv2.imread(img_file,0)
    minVal = 50
    maxVal = 250
    SobelSize = 10

    edges = cv2.Canny(img,minVal,maxVal,SobelSize)

    plt.subplot(251),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(252),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.show()

"""
・Erosion(収縮)
・Dilation(膨張)
・Opening(収縮⇒膨張　小さい点のようなノイズ除去)
・Closing(膨張⇒収縮　小さい箇所の穴埋め)
・勾配（膨張-収縮で輪郭を得る）
・トップハット（入力-Opening）
・ブラックハット（入力-Closing）
"""
def Mol(img_file):
    img = cv2.imread(img_file,0)
    #大津の2値化されたパンダ
    abc,two = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #白黒反転（白に適用されるため）
    two = cv2.bitwise_not(two)

    #Erositon
    kernel = np.ones((35,35),np.uint8)
    erosion = cv2.erode(two,kernel,iterations = 1)
    #Dilation
    kernel = np.ones((35,35),np.uint8)
    dilation = cv2.dilate(two,kernel,iterations = 1)
    #Opening
    kernel = np.ones((35,35),np.uint8)
    opening = cv2.morphologyEx(two, cv2.MORPH_OPEN, kernel)
    #Closing
    kernel = np.ones((35,35),np.uint8)
    closing = cv2.morphologyEx(two, cv2.MORPH_CLOSE, kernel)
    #Gradient
    kernel = np.ones((35,35),np.uint8)
    gradient = cv2.morphologyEx(two, cv2.MORPH_GRADIENT, kernel)
    #Tophat
    kernel = np.ones((35,35),np.uint8)
    tophat = cv2.morphologyEx(two, cv2.MORPH_TOPHAT, kernel)
    #Blackhat
    kernel = np.ones((35,35),np.uint8)
    blackhat = cv2.morphologyEx(two, cv2.MORPH_BLACKHAT, kernel)

    plt.subplot(251),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(252),plt.imshow(two,cmap = 'gray')
    plt.title('2value Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(253),plt.imshow(erosion,cmap = 'gray')
    plt.title('Erosion Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(254),plt.imshow(dilation,cmap = 'gray')
    plt.title('Dilation Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(255),plt.imshow(opening,cmap = 'gray')
    plt.title('Opening Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(256),plt.imshow(closing,cmap = 'gray')
    plt.title('Closing Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(257),plt.imshow(gradient,cmap = 'gray')
    plt.title('Gradient Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(258),plt.imshow(tophat,cmap = 'gray')
    plt.title('Tophat Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(259),plt.imshow(blackhat,cmap = 'gray')
    plt.title('Blackhat Image'), plt.xticks([]), plt.yticks([])

    plt.show()

def Rinkaku(img_file):
    img = cv2.imread(img_file,0)
    edges = cv2.Canny(img,50,250,10)

    #Closing
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((35,35),np.uint8)
    closing2 = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    kernel = np.ones((135,135),np.uint8)
    closing3 = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    plt.subplot(251),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(252),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(253),plt.imshow(closing,cmap = 'gray')
    plt.title('Closing Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(254),plt.imshow(closing2,cmap = 'gray')
    plt.title('Closing2 Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(255),plt.imshow(closing3,cmap = 'gray')
    plt.title('Closing3 Image'), plt.xticks([]), plt.yticks([])

    plt.show()

def main(img_file):
    #img = cv2.imread(img_file, 0)
    img = cv2.imread(img_file,-1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gx = Sobel_gradiant(img, 1)
    gy = Sobel_gradiant(img, 2)
    g = Sobel_gradiant(img, 3)
    
    plt.figure(figsize=(10, 10))  # 画像の表示サイズ
    plt.subplot(321), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(322), plt.imshow(gx), plt.title("Gradient in x")
    plt.xticks([]), plt.yticks([])
    plt.subplot(323), plt.imshow(gy), plt.title("Gradient in y")
    plt.xticks([]), plt.yticks([])
    plt.subplot(324), plt.imshow(g), plt.title("Gradient")
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    #plt.show()
    
    
    img2 = laplacian(img)
    img3 = composite_laplacian(img)
    
    plt.subplot(325), plt.imshow(img2), plt.title("Laplacian")
    plt.xticks([]), plt.yticks([])
    plt.subplot(326), plt.imshow(img3), plt.title("Composite Laplacian")
    plt.xticks([]), plt.yticks([])
    plt.show()

    Sobel_LaplacianFilter(img_file)
    Canny(img_file)
    Mol(img_file)

    cv2.waitKey()


'''
OPENCV(9)--Image Gradients(圖像梯度) 
https://arbu00.blogspot.com/2016/11/opencv9-image-gradients.html
'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='26_gradiant_laplace_Composite_laplace')
   
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
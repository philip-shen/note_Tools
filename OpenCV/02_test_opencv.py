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

def face_detection(path_image, path_cascade):
    # 画像ファイルの読込(結果表示に使用する)
    img = cv2.imread(path_image) #カラーで読込
 
    # グレースケールに変換(顔検出に使用する)
    gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #plt.imshow(gry_img)
    #plt.show()

    # カスケード検出器の特徴量を取得する
    cascade = cv2.CascadeClassifier(path_cascade)
 
    # 顔検出の実行
    facerect = cascade.detectMultiScale(gry_img, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
 
    # 矩形線の色
    rectangle_color = (0, 255, 0) #BGR
 
    # 顔を検出した場合
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)
 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #RGBからBGRに変換
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    # 分類器の読込
    # https://github.com/opencv/opencv/tree/master/data/haarcascades
    # から取得
    cascade_path = "libs/haarcascade_frontalface_default.xml"
    
    face_imgs=['media/input1-1024x682.jpg', 'media/input3-1024x682.jpg']

    for face_img in face_imgs:
        face_detection(face_img, cascade_path)
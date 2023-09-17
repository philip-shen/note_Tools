# coding:utf-8
import dlib
from imutils import face_utils
import cv2
import matplotlib.pyplot as plt

import os
# --------------------------------
# 1.顔ランドマーク検出の前準備
# --------------------------------
# 顔検出ツールの呼び出し
face_detector = dlib.get_frontal_face_detector()

# 顔のランドマーク検出ツールの呼び出し
predictor_path = 'libs/shape_predictor_68_face_landmarks.dat'
face_predictor = dlib.shape_predictor(predictor_path)


if __name__ == '__main__':
    home = os.path.expanduser("~")
    
    # 検出対象の画像の呼び込み
    img = cv2.imread(f'{home}/projects/color/Girl.bmp')
    # 処理高速化のためグレースケール化(任意)
    img_gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --------------------------------
    # 2.顔のランドマーク検出
    # --------------------------------
    # 顔検出
    # ※2番めの引数はupsampleの回数。基本的に1回で十分。
    faces = face_detector(img_gry, 1)

    # 検出した全顔に対して処理
    for face in faces:
        # 顔のランドマーク検出
        landmark = face_predictor(img_gry, face)
        # 処理高速化のためランドマーク群をNumPy配列に変換(必須)
        landmark = face_utils.shape_to_np(landmark)

        # ランドマーク描画
        for (i, (x, y)) in enumerate(landmark):
            cv2.circle(img, (x, y), 1, (255, 0, 0), -1)

    # --------------------------------
    # 3.結果表示
    # --------------------------------
    #cv2.imshow('sample', img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #RGBからBGRに変換
    plt.imshow(img)
    plt.show()
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


'''
OpenCV ObjDetect Module Face Detection (YuNet/libfacedetection) Sample
https://gist.github.com/UnaNancyOwen/3f06d4a0d04f3a75cc62563aafbac332
'''
'''
Kazuhito00/YuNet-ONNX-TFLite-Sample
https://github.com/Kazuhito00/YuNet-ONNX-TFLite-Sample/tree/main

face_detection_yunet_120x160.onnx
https://github.com/Kazuhito00/YuNet-ONNX-TFLite-Sample/blob/main/model/face_detection_yunet_120x160.onnx
'''

'''
OpenCVで顔検出する

https://qiita.com/studio_haneya/items/97560b54b8348db8de87
'''

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

def YuNet(imgfile):
    # キャプチャを開く
    directory = './media'#os.path.dirname(__file__)
    capture = cv2.VideoCapture(os.path.join(directory, imgfile)) # 画像ファイル
    #capture = cv2.VideoCapture(0) # カメラ
    if not capture.isOpened():
        exit()
    
    # モデルを読み込む
    weights = os.path.join(directory, "face_detection_yunet_120x160.onnx")
    face_detector = cv2.FaceDetectorYN_create(weights, "", (0, 0))

    while True:
        # フレームをキャプチャして画像を読み込む
        result, image = capture.read()
        if result is False:
            cv2.waitKey(0)
            break

        # 画像が3チャンネル以外の場合は3チャンネルに変換する
        channels = 1 if len(image.shape) == 2 else image.shape[2]
        if channels == 1:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        if channels == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        # 入力サイズを指定する
        height, width, _ = image.shape
        face_detector.setInputSize((width, height))

        # 顔を検出する
        _, faces = face_detector.detect(image)
        faces = faces if faces is not None else []

        # 検出した顔のバウンディングボックスとランドマークを描画する
        for face in faces:
            # バウンディングボックス
            box = list(map(int, face[:4]))
            color = (0, 255, 0)
            thickness = 1
            cv2.rectangle(image, box, color, thickness, cv2.LINE_AA)

            # ランドマーク（右目、左目、鼻、右口角、左口角）
            landmarks = list(map(int, face[4:len(face)-1]))
            landmarks = np.array_split(landmarks, len(landmarks) / 2)
            for landmark in landmarks:
                radius = 5
                thickness = -1
                cv2.circle(image, landmark, radius, color, thickness, cv2.LINE_AA)
                
            # 信頼度
            confidence = face[-1]
            confidence = "{:.2f}".format(confidence)
            position = (box[0], box[1] - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            scale = 0.5
            thickness = 2
            cv2.putText(image, confidence, position, font, scale, color, thickness, cv2.LINE_AA)

        # 画像を表示する
        cv2.imshow("face detection", image)
        key = cv2.waitKey(10)
        if key == ord('q'):
            break
    
    cv2.destroyAllWindows()
'''
6. cv2.FaceDetectorYN

https://qiita.com/studio_haneya/items/97560b54b8348db8de87#6-cv2facedetectoryn
'''
def YuNet2(imgfile):
    directory = './media'

    image = cv2.imread(os.path.join(directory, imgfile))# 画像ファイル
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

    weights = os.path.join(directory, "face_detection_yunet_120x160.onnx")
    face_detector = cv2.FaceDetectorYN.create(weights, "", (0, 0))

    # 入力サイズを指定する
    height, width, _ = image.shape
    face_detector.setInputSize((width, height))

    # 顔を検出する
    _, faces = face_detector.detect(image)
    faces = faces if faces is not None else []
    image_output = image.copy()

    for face in faces:
        x, y, w, h = list(map(int, face[:4]))
        cv2.rectangle(image_output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    plt.imshow(cv2.cvtColor(image_output, cv2.COLOR_BGR2RGB))
    plt.show()

'''
7. cv2.FaceRecognizerSFで顔認識する

https://qiita.com/studio_haneya/items/97560b54b8348db8de87#7-cv2facerecognizersf%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98%E3%81%99%E3%82%8B
'''
def generate_listed_faces(imgfile):
    # キャプチャを開く
    directory = './media'#os.path.dirname(__file__)
    
    image = cv2.imread(os.path.join(directory, imgfile))# 画像ファイル
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

    weights = os.path.join(directory, "face_detection_yunet_120x160.onnx")
    face_detector = cv2.FaceDetectorYN.create(weights, "", (0, 0))

    # 入力サイズを指定する
    height, width, _ = image.shape
    face_detector.setInputSize((width, height))

    # 顔を検出する
    _, faces = face_detector.detect(image)
    faces = faces if faces is not None else []

    # モデルを読み込む
    weights = os.path.join(directory, "face_recognizer_fast.onnx")
    face_recognizer = cv2.FaceRecognizerSF.create(weights, "")

    # 検出された顔を切り抜く
    aligned_faces = []
    for face in faces:
        aligned_face = face_recognizer.alignCrop(image, face)
        aligned_faces.append(aligned_face)

        plt.imshow(cv2.cvtColor(aligned_face, cv2.COLOR_BGR2RGB))
        plt.show()
    
    num_images = len(aligned_faces)    
    plt.figure(figsize=(8, 8))  # 画像の表示サイズ
    for i in range(num_images):
        plt.subplot(1, 6, i+1)
        #plt.imshow(np.transpose(images[i], (1, 2, 0)))  # チャンネルを一番後ろに
        #label = index2name[i]# cifar10_classes[labels[i]]
        #plt.title(label)
        plt.imshow(cv2.cvtColor(aligned_faces[i], cv2.COLOR_BGR2RGB))
        plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)  # ラベルとメモリを非表示に
    plt.show()        


    # 特徴を抽出する
    fig, ax = plt.subplots(len(faces), 1, figsize=(7, 8))

    face_features = dict()
    aligned_faces = list()
    for k, face in enumerate(faces):
        # 検出した顔画像を切り出し
        aligned_face = face_recognizer.alignCrop(image, face)
        aligned_faces.append(aligned_face)
    
        # 切り出した顔画像から特徴量を算出してdictに入れる
        face_feature = face_recognizer.feature(aligned_face)
        user_id = 'face{:03d}'.format(k) # face001.npy -> face001
        face_features[user_id] = face_feature

        ax[k].plot(face_feature[0])
    plt.show()

'''
generate_aligned_faces.py

https://gist.githubusercontent.com/UnaNancyOwen/49df508ad8b6d9520024354df0e3e740/raw/54e7dbd2f15b6137dc2b6d4ef6ce3143528c3978/generate_aligned_faces.py
'''
def generate_aligned_faces(imgfile):    
    
    directory = os.path.dirname(imgfile)
    if not directory:
        directory = './media'#directory = os.path.dirname(__file__)
        path = os.path.join(directory, imgfile)

    # 画像を開く
    image = cv2.imread(path)
    if image is None:
        exit()

    # 画像が3チャンネル以外の場合は3チャンネルに変換する
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    if channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if channels == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    # モデルを読み込む
    weights = os.path.join(directory, "face_detection_yunet_120x160.onnx")
    face_detector = cv2.FaceDetectorYN_create(weights, "", (0, 0))
    weights = os.path.join(directory, "face_recognizer_fast.onnx")
    face_recognizer = cv2.FaceRecognizerSF_create(weights, "")

    # 入力サイズを指定する
    height, width, _ = image.shape
    face_detector.setInputSize((width, height))

    # 顔を検出する
    _, faces = face_detector.detect(image)

    # 検出された顔を切り抜く
    aligned_faces = []
    if faces is not None:
        for face in faces:
            aligned_face = face_recognizer.alignCrop(image, face)
            aligned_faces.append(aligned_face)

    # 画像を表示、保存する
    for i, aligned_face in enumerate(aligned_faces):
        cv2.imshow("aligned_face {:03}".format(i + 1), aligned_face)
        cv2.imwrite(os.path.join(directory, "face{:03}.jpg".format(i + 1)), aligned_face)

    cv2.waitKey(0)
    #cv2.destroyAllWindows()

def generate_feature_dictionary(imgfile):
    # 引数から画像ファイルのパスを取得    
    directory = os.path.dirname(imgfile)
    if not directory:
        directory = './media'#directory = os.path.dirname(__file__)
        path = os.path.join(directory, imgfile)

    # 画像を開く
    image = cv2.imread(path)
    if image is None:
        exit()

    # 画像が3チャンネル以外の場合は3チャンネルに変換する
    channels = 1 if len(image.shape) == 2 else image.shape[2]
    if channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    if channels == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

    # モデルを読み込む
    weights = os.path.join(directory, "face_recognizer_fast.onnx")
    face_recognizer = cv2.FaceRecognizerSF_create(weights, "")

    # 特徴を抽出する
    face_feature = face_recognizer.feature(image)
    print(face_feature)
    print(type(face_feature))

    # 特徴を保存する
    basename = os.path.splitext(os.path.basename(path))[0]
    dictionary = os.path.join(directory, basename)
    np.save(dictionary, face_feature)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='06_face_detector')
   
    parser.add_argument('--img', type=str, default='sample.jpg', help='jpg file')
    parser.add_argument('--model', type=str, default='YuNet2', help='YuNet, YuNet2, FaceRecognizer')
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
    model = args.model
    
    if os.path.isfile(os.path.join('media', img_file)):
        if model.lower() == 'yunet':
            YuNet(img_file)
        elif model.lower() == 'yunet2':
            YuNet2(img_file)
        elif model.lower() == 'facerecognizer':
            #generate_aligned_faces(img_file)
            generate_listed_faces(img_file)
            #generate_feature_dictionary(img_file)

    est_timer(start_time=t0)
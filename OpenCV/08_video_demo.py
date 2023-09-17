from __future__ import division
import time
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2
from util import *
from darknet import Darknet
from preprocess import prep_image, inp_to_image
import pandas as pd
import random
import argparse
import pickle as pkl
 
def prep_image(img, inp_dim):
    # CNNに通すために画像を加工する
    orig_im = img
    dim = orig_im.shape[1], orig_im.shape[0]
    img = cv2.resize(orig_im, (inp_dim, inp_dim))
    img_ = img[:,:,::-1].transpose((2,0,1)).copy()
    img_ = torch.from_numpy(img_).float().div(255.0).unsqueeze(0)
    return img_, orig_im, dim
 
def write(x, img):
    # 画像に結果を描画
    c1 = tuple(x[1:3].int())
    c2 = tuple(x[3:5].int())
    cls = int(x[-1])
    label = "{0}".format(classes[cls])
    color = random.choice(colors)
    cv2.rectangle(img, c1, c2,color, 1)
    t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 1 , 1)[0]
    c2 = c1[0] + t_size[0] + 3, c1[1] + t_size[1] + 4
    cv2.rectangle(img, c1, c2,color, -1)
    cv2.putText(img, label, (c1[0], c1[1] + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225,255,255], 1);
    return img
 
def arg_parse():
    # モジュールの引数を作成
    parser = argparse.ArgumentParser(description='YOLO v3 Cam Demo') # ArgumentParserで引数を設定する
    parser.add_argument("--confidence", dest = "confidence", help = "Object Confidence to filter predictions", default = 0.25)
    # confidenceは信頼性
    parser.add_argument("--nms_thresh", dest = "nms_thresh", help = "NMS Threshhold", default = 0.4)
    # nms_threshは閾値
    
    parser.add_argument("--reso", dest = 'reso', help =
                        "Input resolution of the network. Increase to increase accuracy. Decrease to increase speed",
                        default = "160", type = str)
                        # resoはCNNの入力解像度で、増加させると精度が上がるが、速度が低下する。
    return parser.parse_args() # 引数を解析し、返す
 
if __name__ == '__main__':
    cfgfile = "cfg/yolov3.cfg" # 設定ファイル
    weightsfile = "yolov3.weights" # 重みファイル
    num_classes = 80 # クラスの数
 
    args = arg_parse() # 引数を取得
    confidence = float(args.confidence) # 信頼性の設定値を取得
    nms_thesh = float(args.nms_thresh) # 閾値を取得
    start = 0
    CUDA = torch.cuda.is_available() # CUDAが使用可能かどうか
 
    num_classes = 80 # クラスの数
    bbox_attrs = 5 + num_classes
 
    model = Darknet(cfgfile) #modelの作成
    model.load_weights(weightsfile) # modelに重みを読み込む
 
    model.net_info["height"] = args.reso
    inp_dim = int(model.net_info["height"])
 
    assert inp_dim % 32 == 0
    assert inp_dim > 32
 
    if CUDA:
        model.cuda() #CUDAが使用可能であればcudaを起動
 
    model.eval()
 
    cap = cv2.VideoCapture(0) #カメラを指定
 
    assert cap.isOpened(), 'Cannot capture source' #カメラが起動できたか確認
 
    frames = 0
    start = time.time()
    while cap.isOpened(): #カメラが起動している間
 
        ret, frame = cap.read() #キャプチャ画像を取得
        if ret:
            # 解析準備としてキャプチャ画像を加工
            img, orig_im, dim = prep_image(frame, inp_dim)
 
            if CUDA:
                im_dim = im_dim.cuda()
                img = img.cuda()
 
            output = model(Variable(img), CUDA)
            output = write_results(output, confidence, num_classes, nms = True, nms_conf = nms_thesh)
 
            # FPSの表示
            if type(output) == int:
                frames += 1
                print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
                cv2.imshow("frame", orig_im)
 
                # qキーを押すとFPS表示の終了
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    break
                continue
 
            output[:,1:5] = torch.clamp(output[:,1:5], 0.0, float(inp_dim))/inp_dim
            output[:,[1,3]] *= frame.shape[1]
            output[:,[2,4]] *= frame.shape[0]
 
            classes = load_classes('data/coco.names') # 識別クラスのリスト
            colors = pkl.load(open("pallete", "rb"))
 
            list(map(lambda x: write(x, orig_im), output))
 
            cv2.imshow("frame", orig_im)
            key = cv2.waitKey(1)
            # qキーを押すと動画表示の終了
            if key & 0xFF == ord('q'):
                break
            frames += 1
            print("FPS of the video is {:5.2f}".format( frames / (time.time() - start)))
 
        else:
            break
"""
指定した角度づつ元画像の中心を軸に回転させた画像を作成して保存する。

https://qiita.com/goodboy_max/items/2fdcf8aba457adceafd4
"""

# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys
import os
from PIL import Image,ImageSequence

def jpg_to_gif(in_img_files, out_gif_fname, ms=500):
    # Create the animation
    frame_array = []
    for filename in in_img_files:
        #filename = f'frame_{i:02d}.jpg'
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 因為 OpenCV 為 BGRA，要轉換成 RGBA
        img = Image.fromarray(img)    # 轉換成 PIL 格式
        img = img.convert('RGB')      # 轉換成 RGB ( 如果是 RGBA 會自動將黑色白色變成透明色 )
        frame_array.append(img)

    output_filename = os.path.join('media', out_gif_fname) 

    # 儲存為 gif 動畫圖檔
    frame_array[0].save(output_filename, save_all=True, append_images=frame_array[1:], 
                        duration= ms, loop=0, disposal=0)
    # frame1：gif 動畫第一個影格
    # save_all：設定 True 表示儲存全部影格，否則只有第一個
    # append_images：要添加到 frame1 影格的其他影格，串列格式，通常會用 frame[1:] 來添加除了第一個影格之後的所有影格
    # duration：每個影格之間的毫秒數，支援串列格式
    # disposal：添加模式，預設 0，如果背景透明，則設定為 2 避免影格彼此覆蓋覆蓋

args = sys.argv
print("args=",args)
print(len(args))


if len(args) == 1:

    # パラメータを指定しない場合は、data/maxgogo.jpg というファイルが存在する前提です
    img_path = "media"
    img_name_body = "eagle-04_640"
    img_name_extension = ".jpg"

    img_name = img_name_body + img_name_extension

elif len(args) == 2: # 画像ファイルが指定される前提で細かいチェックしてません。

    base_dir_pair = os.path.split(args[1])
    img_path = base_dir_pair[0]
    root_ext_pair = os.path.splitext(base_dir_pair[1])
    img_name_body = root_ext_pair[0]
    img_name_extension = root_ext_pair[1]
    img_name = img_name_body + img_name_extension

    print(base_dir_pair)
    print("img_path=",img_path)
    print(root_ext_pair)
    print("img_name_body=",img_name_body)
    print("img_name_extension=",img_name_extension)

else :
    print("error path/filename")

# パスが無い場合を考慮した処理
if len(img_path) == 0:
    # 画像読み込み
    img = cv2.imread(img_name)
else:
    # 画像読み込み
    img = cv2.imread(img_path + os.sep + img_name)

if img is None:
        print("**************************")
        print("Failed to load image file.")
        print("**************************")
        sys.exit(1)

print(type(img))
print("size:",img.size)
h, w = img.shape[:2]
size = (w, h)

########################################################
# 回転角の指定 30 だと30度ごと。適当に変更してください。
########################################################
angle = 30

# 取得数 360度を回転角で割る
range_num = 360 // angle

# 指定した角度で回転した場合の最大の幅と高さを取得する
w_max = 0
h_max = 0

# 高さ、幅の最大値を取得
# ragne は 0 から始まり、指定した数-1 まで実行する。
for  num in range(range_num):

    angle_num = angle*num

    angle_rad = angle_num/180.0*np.pi

    # 回転後の画像サイズを計算
    w_rot = int(np.round(h*np.absolute(np.sin(angle_rad))+w*np.absolute(np.cos(angle_rad))))
    h_rot = int(np.round(h*np.absolute(np.cos(angle_rad))+w*np.absolute(np.sin(angle_rad))))

    if w_rot > w_max :
        w_max = w_rot
    if h_rot > h_max :
        h_max = h_rot

list_fnames= []
# 画像書き出し
for  num in range(range_num):

    angle_num = angle*num

    angle_rad = angle_num/180.0*np.pi

    size_rot = (w_max, h_max)

    # 元画像の中心を軸に回転する
    center = (w/2, h/2)
    scale = 1.0
    rotation_matrix = cv2.getRotationMatrix2D(center, angle_num, scale)

    # 平行移動を加える (rotation + translation)
    affine_matrix = rotation_matrix.copy()
    affine_matrix[0][2] = affine_matrix[0][2] -w/2 + w_max/2
    affine_matrix[1][2] = affine_matrix[1][2] -h/2 + h_max/2

    # アフィン変換
    img_rot = cv2.warpAffine(img, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)

    # パスが無い場合を考慮した処理
    if len(img_path) == 0:
        writefile_name = img_name_body + "_" + str(num) + img_name_extension
    else:
        writefile_name = img_path + os.sep + img_name_body + "_" + str(num) + img_name_extension

    print (writefile_name)

    cv2.imshow(writefile_name, img_rot)
    cv2.imwrite(writefile_name, img_rot)

    list_fnames.append(writefile_name)

jpg_to_gif( list_fnames, '30_5_animation_roation_central_02.gif', 1000)

cv2.waitKey(0)
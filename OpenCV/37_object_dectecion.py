'''
 《第9天》OpenCV物件偵測
2022-09-24 23:46:15

https://ithelp.ithome.com.tw/articles/10297918
'''
'''
‘cv2.dnn_DetectionModel‘ object has no attribute ‘getUnconnectedOutLayersNames‘问题解决（Yolov4）

https://blog.csdn.net/weixin_51914823/article/details/120600281

Yolo v4 only opencv 4.4.0
'''
'''
成功解决TypeError: only integer scalar arrays can be converted to a scalar index
https://blog.csdn.net/qq_41185868/article/details/88104813

result': labels[classid], 'conf': float(conf)}
TypeError: only integer scalar arrays can be converted to a scalar index

np.array(labels)[classid]
'''
import numpy as np
import cv2
import pathlib
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

(major, minor, _) = cv2.__version__.split(".")
    
def est_timer(start_time):
    time_consumption, h, m, s= lib_misc.format_time(time.time() - start_time)         
    msg = 'Time Consumption: {}.'.format( time_consumption)#msg = 'Time duration: {:.2f} seconds.'
    logger.info(msg)

# 讀取中文路徑圖檔(圖片讀取為BGR)
def cv_imread(image_path):
    image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), -1)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    return image

# 顯示圖檔
def show_img(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)

# 讀取模型架構與權重
def initNet():
    # 可更換成yolov4-tiny.cfg與yolov4-tiny.weights
    CONFIG = f'Z:\weights\yolov4.cfg'
    WEIGHT = f'Z:\weights\yolov4.weights'
    net = cv2.dnn.readNet(CONFIG, WEIGHT)
    # OpenCV version >= 4 or other 
    if major == '4':
        model = cv2.dnn_DetectionModel(net)
        # 若以yolov4-tiny進行物件偵測，預設size=(416, 416)
        model.setInputParams(size=(608, 608), scale=1/255.0)
        model.setInputSwapRB(True)
        return model
    else:
        logger.info('OpenCV version must be equal or over 4.4.0.42')
    
def initNet_tiny():
    # 可更換成yolov4-tiny.cfg與yolov4-tiny.weights
    CONFIG = f'Z:\weights\yolov4-tiny.cfg'
    WEIGHT = f'Z:\weights\yolov4-tiny.weights'
    net = cv2.dnn.readNet(CONFIG, WEIGHT)
    
    # OpenCV version >= 4 or other 
    if major == '4':
        model = cv2.dnn_DetectionModel(net)
        # 若以yolov4-tiny進行物件偵測，預設size=(416, 416)
        model.setInputParams(size=(416, 416), scale=1/255.0)
        model.setInputSwapRB(True)
        return model
    else:
        logger.info('OpenCV version must be equal or over 4.4.0.42')
        
# 物件偵測
def nnProcess(image, model):
    '''
    信心水準(conf)閾值為0.3
    NMS為0.2，用來篩除重複框選同一物件的Bounding Box。
    '''
    classes, confs, boxes = model.detect(image, 0.3, 0.2)
    return classes, confs, boxes

# Output輸出格式化
def predict(classes, confs, boxes):
    # 讀取標籤類別
    with open(f'Z:\OpenCV\coco-classes.txt') as f:
        labels = f.read().split('\n')
    predit_list = []

    # 格式化推論結果
    for classid, conf, box in zip(classes, confs, boxes):
        predict = {'xmin': float(box[0]), 'ymin': float(box[1]),
                   'xmax': float(box[0])+float(box[2]), 
                   'ymax': float(box[1])+float(box[3]),
                   'result': np.array(labels)[classid], 'conf': float(conf)}
        predit_list.append(predict)
    return predit_list

# 在原圖上畫出被偵測的物件
def drawBox(image, classes, confs, boxes):
    image1 = image.copy()
    for (classid, conf, box) in zip(classes, confs, boxes):
        x, y, w, h = box
        cv2.rectangle(image1, (x, y), (x + w, y + h), (180, 0, 0), 3)
    return image1

def main(start_time, path_img, model, str_img_title='final_image'):
    image = cv_imread(os.path.join(path_img, img_file))
    classes, confs, boxes = nnProcess(image, model)

    result = predict(classes, confs, boxes)
    end = time.time()
    for i in result:
        #print(i)
        logger.info(f'\n{i}')
    #print('YOLOv4物件偵測共花費 {} 秒'.format(end - start))
    logger.info(f'\nYOLOv4物件偵測共花費 {end - start_time} 秒')
    
    est_timer(start_time=t0)
    
    final_image = drawBox(image, classes, confs, boxes)
    show_img(str_img_title, final_image)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='37_object_dectecion')
   
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
    
    if sys.platform.startswith('linux'): # 包含 linux 與 linux2 的情況
        path_infinicloud = '/home/philphoenix/infinicloud/OpenCV'
    elif sys.platform.startswith('win32'):
        path_infinicloud = 'Z:\\OpenCV'
        
    if not os.path.isfile(os.path.join(path_infinicloud, img_file)):
        logger.info(f'{os.path.join(path_infinicloud, img_file)} does not exist!')
        est_timer(start_time=t0)
        sys.exit(0)
        
    start = time.time()
    model_YOLOV4 = initNet()    
    main(start, path_infinicloud, model_YOLOV4, str_img_title='final_image_YOLOV4')
    
    start = time.time()
    model_YOLOV4 = initNet_tiny()    
    main(start, path_infinicloud, model_YOLOV4, str_img_title='final_image_YOLOV4-tiny')    
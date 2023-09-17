import torch
import torchvision 
import torchvision.transforms as transforms
from torchvision.utils import draw_bounding_boxes
import numpy as np
import matplotlib.pyplot as plt

import xml.etree.ElementTree as ET
from torch.utils.data import Dataset, DataLoader
from PIL import Image

from logger_setup import *

__all__ = [
    'dataset_VOCDetection',
    'show_boxes',
    'show_images',
    'model_train',
    'model_inference',
    'score',
    'loadchkpt_model_inference',
    'VOCDataset',
]

# インデックスを物体名に変換
index2name = [
    "person",
    "bird",
    "cat",
    "cow",
    "dog",
    "horse",
    "sheep",
    "aeroplane",
    "bicycle",
    "boat",
    "bus",
    "car",
    "motorbike",
    "train",
    "bottle",
    "chair",
    "diningtable",
    "pottedplant",
    "sofa",
    "tvmonitor",
]

# 物体名をインデックスに変換
name2index = {}
for i in range(len(index2name)):
        name2index[index2name[i]] = i
        logger.info(f"name2index[{index2name[i]}]: {name2index[index2name[i]]} ")

def arrange_target(target):
    objects = target["annotation"]["object"]
    box_dics = [obj["bndbox"] for obj in objects]
    box_keys = ["xmin", "ymin", "xmax", "ymax"]

    # バウンディングボックス
    boxes = []
    for box_dic in box_dics:
        box = [int(box_dic[key]) for key in box_keys]
        boxes.append(box)
    boxes =  torch.tensor(boxes)    

    # 物体名
    labels = [name2index[obj["name"]] for obj in objects]
    labels = torch.tensor(labels)

    dic = {"boxes": boxes, "labels": labels }

    return dic

def dataset_VOCDetection(path_dataset, str_year="2012", opt_download=False):
    dataset_train=torchvision.datasets.VOCDetection(root=path_dataset,
                                                year=str_year, image_set="train",
                                                download=opt_download,
                                                transform=transforms.ToTensor(),
                                                target_transform=transforms.Lambda(arrange_target)
                                                )

    dataset_test=torchvision.datasets.VOCDetection(root=path_dataset,
                                                year=str_year,image_set="val",
                                                download=opt_download,
                                                transform=transforms.ToTensor(),
                                                target_transform=transforms.Lambda(arrange_target)
                                                )

    return dataset_train, dataset_test

def show_boxes(image, boxes, names):
    drawn_boxes = draw_bounding_boxes(image, boxes, labels=names)

    plt.figure(figsize = (16,16))
    plt.imshow(np.transpose(drawn_boxes, (1, 2, 0)))  # チャンネルを一番後ろに
    plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)  # ラベルとメモリを非表示に
    plt.show()

def show_images(data_loader, num_images=25, opt_verbose='OFF'):
    
    dataiter = iter(data_loader)  # イテレータ
    images, target = next(dataiter)  # バッチを取り出す

    if opt_verbose.lower() == 'on':
        logger.info(f"\nlen of images:{len(images)}; images: {images}")
        logger.info(f"\nlen of target:{len(target)} ;target: {target}")

    plt.figure(figsize=(10, 10))  # 画像の表示サイズ
    for i in range(num_images):
        plt.subplot(5,5,i+1)
        plt.imshow(np.transpose(images[i], (1, 2, 0)))  # チャンネルを一番後ろに
        #label = index2name[i]# cifar10_classes[labels[i]]
        #plt.title(label)
        plt.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)  # ラベルとメモリを非表示に

    plt.show()    


def model_train(json_data, device, dataloader_train, model, opt_verbose= "OFF"):
    # 最適化アルゴリズム
    params = [p for p in model.parameters() if p.requires_grad]
    optimizer = torch.optim.SGD(params, 
                                lr=json_data["Config"][3]["learning_rate"], 
                                momentum=json_data["Config"][3]["momentum"],
                                )
    model.train() # 訓練モード
    epochs = json_data["Config"][3]["num_epochs"]
    checkpt = json_data["Config"][3]["checkpoint_path"]

    best_loss_value = float('inf')
    for epoch in range(epochs):
        for i, (image, target) in enumerate(dataloader_train):
            image = image.to(device)  # GPU対応

            boxes = target["boxes"][0].to(device)#target["boxes"][0].cuda()
            labels = target["labels"][0].to(device)#target["labels"][0].cuda()
            target = [{"boxes":boxes, "labels":labels}]  # ターゲットは辞書を要素に持つリスト

            loss_dic = model(image, target)
            losses = sum(loss for loss in loss_dic.values())  # 誤差の合計を計算
            loss_value = losses.item()

            optimizer.zero_grad()
            losses.backward()
            optimizer.step()

            if i%100 == 0:  # 100回ごとに経過を表示
                #print("epoch:", epoch:,  "iteration:", i,  "loss:", loss.item()) 
                logger.info(f"epoch: {epoch+1}, iteration: {i}, loss: {loss_value}")

            if loss_value < best_loss_value:
                best_loss_value = loss_value
                torch.save(model.state_dict(), checkpt)
                #torch.save(model, json_data["Config"][2]["checkpoint_path"])
                logger.info(f"\nloss_value: {loss_value} < best_loss_value: {best_loss_value}; save checkpoint: {checkpt}" )     

def model_inference(device, dataloader_test, model):
    dataiter = iter(dataloader_test)  # イテレータ
    image, target = next(dataiter)  # バッチを取り出す

    image = image.to(device) #image.cuda()  # GPU対応

    model.eval()
    predictions = model(image)
    #print(predictions)
    logger.info(f"predictions: {predictions}")

    image = (image[0]*255).to(torch.uint8).cpu() # draw_bounding_boxes関数の入力は0-255
    boxes = predictions[0]["boxes"].cpu()
    labels = predictions[0]["labels"].cpu().detach().numpy()
    labels = np.where(labels>=len(index2name), 0, labels)  # ラベルが範囲外の場合は0に
    names = [index2name[label.item()] for label in labels]

    #print(names)
    logger.info(f"names: {names}")
    show_boxes(image, boxes, names)    

    return image, boxes, names, predictions

def score(image, predictions, criteria= 0.5):
    
    #print(predictions)
    logger.info(f"predictions: {predictions}")
    
    boxes = []
    names = []
    for i, box in enumerate(predictions[0]["boxes"]):
        score = predictions[0]["scores"][i].cpu().detach().numpy()
        if score > criteria:  # スコアが0.5より大きいものを抜き出す
            boxes.append(box.cpu().tolist())
            label = predictions[0]["labels"][i].item()
            if label >= len(index2name):  # ラベルが範囲外の場合は0に
                label = 0
            name = index2name[label]
            names.append(name)
    
    boxes = torch.tensor(boxes)

    show_boxes(image, boxes, names)

def loadchkpt_model_inference(device, model, chkpt, dataloader_test):    
    model.load_state_dict(torch.load(chkpt))

    dataiter = iter(dataloader_test)  # イテレータ
    image, target = next(dataiter)  # バッチを取り出す

    image = image.to(device) #image.cuda()  # GPU対応

    model.eval()
    predictions = model(image)
    #print(predictions)
    logger.info(f"predictions: {predictions}")

    image = (image[0]*255).to(torch.uint8).cpu() # draw_bounding_boxes関数の入力は0-255
    boxes = predictions[0]["boxes"].cpu()
    labels = predictions[0]["labels"].cpu().detach().numpy()
    labels = np.where(labels>=len(index2name), 0, labels)  # ラベルが範囲外の場合は0に
    names = [index2name[label.item()] for label in labels]

    #print(names)
    logger.info(f"names: {names}")
    show_boxes(image, boxes, names)    

    return image, boxes, names, predictions

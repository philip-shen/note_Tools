"""
python+opencvで画像処理の勉強9 パターン認識

https://qiita.com/tanaka_benkyo/items/43ef63f54f3dc191e64b

studymemo/12パターン認識.ipynb
https://github.com/tanakakao/studymemo/blob/main/12%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E8%AA%8D%E8%AD%98.ipynb
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.neighbors import KNeighborsClassifier, KDTree
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import scipy.spatial as ss 
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import AdaBoostRegressor, AdaBoostClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pandas as pd
from scipy.stats import multivariate_normal

from sklearn.neighbors import KDTree
import scipy.stats as stats

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

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
    scale = (640 * 480 / (w * h)) ** scale_value#0.5
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)
    return img_rgb, img_gray
    
def read_fruits_img(img_files):
    #path = path + name
 
    #list1 = os.listdir(path)
    tmp = np.array([read_image(s) for s in img_files])
    tmp_gray = np.array([cv2.cvtColor(s, cv2.COLOR_RGB2GRAY) for s in tmp])
    return tmp, tmp_gray

def make_mask(rgb):
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    kernel = np.ones((3, 3), np.uint8)
    ret, thresh = cv2.threshold(gray,250,255,cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, kernel, iterations = 6)
    thresh = cv2.erode(thresh, kernel, iterations = 2)
    mask = cv2.bitwise_not(thresh)
    return mask

def calc_roundness(rgb):
    thresh = make_mask(rgb)
    
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt,True)
    roundness = 4*np.pi*area / perimeter**2
    return roundness

def mean_col(rgb):
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    mask = make_mask(rgb)
    
    r = np.sum(rgb[:,:,0]*mask)/np.sum(mask==255)
    g = np.sum(rgb[:,:,1]*mask)/np.sum(mask==255)
    b = np.sum(rgb[:,:,2]*mask)/np.sum(mask==255)
    
    return np.array([r, g, b])

def calc_rgb_mean_roundness(img_file):
    imgs = read_image(img_file)
    
    rgb_mean = np.array([mean_col(s) for s in imgs])
    roundness = np.array([calc_roundness(s) for s in imgs])

    return rgb_mean, roundness

def aa(img_files):
    '''
    imgs1 = read_image(img_files[0])
    imgs2 = read_image(img_files[1])
    imgs3 = read_image(img_files[2])

    rgb_mean1 = np.array([mean_col(s) for s in imgs1])
    roundness1 = np.array([calc_roundness(s) for s in imgs1])

    rgb_mean2 = np.array([mean_col(s) for s in imgs2])
    roundness2 = np.array([calc_roundness(s) for s in imgs2])

    rgb_mean3 = np.array([mean_col(s) for s in imgs3])
    roundness3 = np.array([calc_roundness(s) for s in imgs3])
    '''
    rgb_mean1, roundness1 = calc_rgb_mean_roundness(img_files[0])
    rgb_mean2, roundness2 = calc_rgb_mean_roundness(img_files[1])
    rgb_mean3, roundness3 = calc_rgb_mean_roundness(img_files[2])

    fig, ax = plt.subplots(2, 2, figsize=(10, 10), subplot_kw=({"xticks":(), "yticks":()}))

    ax[0][0].imshow(imgs1[0]);
    ax[0][1].imshow(imgs2[0]);
    ax[1][0].imshow(imgs3[0]);

    ax[1][1].plot(rgb_mean1[:,0], roundness1, 'o', color='red')
    ax[1][1].plot(rgb_mean2[:,0], roundness2, 'o', color='yellow')
    ax[1][1].plot(rgb_mean3[:,0], roundness3, 'o', color='orange')
    ax[1][1].plot(rgb_mean1[:,0].mean(), roundness1.mean(), 'x', color='blue');
    ax[1][1].plot(rgb_mean2[:,0].mean(), roundness2.mean(), 'x', color='blue');
    ax[1][1].plot(rgb_mean3[:,0].mean(), roundness3.mean(), 'x', color='blue');

    ax[1][1].set_xlabel("Red");
    ax[1][1].set_ylabel("Roundness");

    ax[1][2].axis('off');

def show_result(X, y, model):
    xrange = np.arange(X[:,0].min()*1.2,X[:,0].max()*1.2,0.01)
    yrange = np.arange(X[:,1].min()*1.2,X[:,1].max()*1.2,0.01)
    xx, yy = np.meshgrid(xrange, yrange)
    result = model.predict(np.array([xx.reshape(-1),yy.reshape(-1)]).T).reshape(len(yrange), len(xrange))

    plt.contourf(xx,yy,result, alpha=.4)
    plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y)

    

def stand_kmean(img_files):
    '''
    imgs1 = read_image(img_files[0])
    imgs2 = read_image(img_files[1])
    imgs3 = read_image(img_files[2])

    rgb_mean1 = np.array([mean_col(s) for s in imgs1])
    roundness1 = np.array([calc_roundness(s) for s in imgs1])

    rgb_mean2 = np.array([mean_col(s) for s in imgs2])
    roundness2 = np.array([calc_roundness(s) for s in imgs2])

    rgb_mean3 = np.array([mean_col(s) for s in imgs3])
    roundness3 = np.array([calc_roundness(s) for s in imgs3])
    '''
    rgb_mean1, roundness1 = calc_rgb_mean_roundness(img_files[0])
    rgb_mean2, roundness2 = calc_rgb_mean_roundness(img_files[1])
    rgb_mean3, roundness3 = calc_rgb_mean_roundness(img_files[2])

    X = pd.DataFrame({'Red':np.concatenate([rgb_mean1[:,0],rgb_mean2[:,0],rgb_mean3[:,0]]),
                   'Blue':np.concatenate([rgb_mean1[:,1],rgb_mean2[:,1],rgb_mean3[:,1]])})
    y = np.array([0]*len(rgb_mean1)+[1]*len(rgb_mean2)+[2]*len(rgb_mean3))

    # 標準化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # K近傍法
    neighbor = KNeighborsClassifier(1)
    neighbor.fit(X_scaled, y)

    show_result(X_scaled, y, neighbor)

    ''''''''''''''
    X1 = X_scaled[:len(rgb_mean1),:]
    X2 = X_scaled[len(rgb_mean1):(len(rgb_mean1)+len(rgb_mean2)),:]
    X3 = X_scaled[(len(rgb_mean1)+len(rgb_mean2)):,:]

    # 平均ベクトル
    M1 = X1.mean(axis=0)
    M2 = X2.mean(axis=0)
    M3 = X3.mean(axis=0)

    # 分散共分散行列
    S1 = (X1-M1).T@(X1-M1) / len(X1)
    S2 = (X2-M2).T@(X2-M2) / len(X2)
    S3 = (X3-M3).T@(X3-M3) / len(X3)

    # ラベル
    labels=y

    # 色の設定
    cmaps = ['Purples', 'Blues', 'Reds', 'Greens']

    xrange = np.arange(X_scaled[:,0].min()*1.2,X_scaled[:,0].max()*1.2,0.01)
    yrange = np.arange(X_scaled[:,1].min()*1.2,X_scaled[:,1].max()*1.2,0.01)

    xx, yy = np.meshgrid(xrange, yrange)
    xy_sample = np.vstack([xx.ravel(), yy.ravel()]).T

    # 各ガウス分布における等高線の表示
    mp = np.zeros((len(yrange),len(xrange),3))
    for i, (m, c) in enumerate(zip([M1,M2,M3], [S1,S2,S3])):
        mp[:,:,i] = multivariate_normal(m, c).pdf(xy_sample).reshape(len(yrange),len(xrange))
        plt.contour(xx, yy, mp[:,:,i], levels=3, cmap=cmaps[i])

    # マハラノビス距離が大きいインデックスを分類結果とする
    plt.contourf(xx, yy, mp.argmax(axis=2), levels=3, alpha=.1)
    plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y, alpha=.5)

    #NN法とkNN法
    neighbor = KNeighborsClassifier(6)
    neighbor.fit(X_scaled, y)

    show_result(X_scaled, y, neighbor)
    
    # kd-tree法
    neighbor = KNeighborsClassifier(6, algorithm='kd_tree')
    neighbor.fit(X_scaled, y)

    show_result(X_scaled, y, neighbor)

    # scikit-learnのKDTree
    tree = KDTree(X_scaled, leaf_size=3)
    dist, ind = tree.query(np.array([xx.reshape(-1),yy.reshape(-1)]).T, k=5)

    result = np.array([stats.mode([y[i] for i in idx])[0][0] for idx in ind]).reshape(len(yrange), len(xrange))

    plt.contourf(xx,yy,result, alpha=.4)
    plt.scatter(X_scaled[:,0], X_scaled[:,1], c=y)



    X = pd.DataFrame({'Red':np.concatenate([rgb_mean1[:,0],rgb_mean2[:,0],rgb_mean3[:,0]]),
                  'Blue':np.concatenate([rgb_mean1[:,1],rgb_mean2[:,1],rgb_mean3[:,1]]),
                  'Green':np.concatenate([rgb_mean1[:,2],rgb_mean2[:,2],rgb_mean3[:,2]])})
    y = np.array([0]*len(rgb_mean1)+[1]*len(rgb_mean2)+[2]*len(rgb_mean3))

    # 標準化を行う
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # LDA
    lda = LinearDiscriminantAnalysis(n_components=2)
    X_lda = lda.fit(X_scaled, y).transform(X_scaled)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i in range(3):
        ax[0].plot(X_scaled[y==i,0], X_scaled[y==i,1], 'o')
        ax[1].plot(X_lda[y==i,0], X_lda[y==i,1], 'o')

    # SELFIC法
    pca = PCA(n_components=2)
    X_pca = pca.fit(X_scaled).transform(X_scaled)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i in range(3):
        ax[0].plot(X_scaled[y==i,0], X_scaled[y==i,1], 'o')
        ax[1].plot(X_pca[y==i,0], X_pca[y==i,1], 'o')

def k_means(img_files):
    rgb_mean1, roundness1 = calc_rgb_mean_roundness(img_files[0])
    rgb_mean2, roundness2 = calc_rgb_mean_roundness(img_files[1])
    rgb_mean3, roundness3 = calc_rgb_mean_roundness(img_files[2])

    X = pd.DataFrame({'Red':np.concatenate([rgb_mean1[:,0],rgb_mean2[:,0],rgb_mean3[:,0]]),
                   'Blue':np.concatenate([rgb_mean1[:,1],rgb_mean2[:,1],rgb_mean3[:,1]])})
    y = np.array([0]*len(rgb_mean1)+[1]*len(rgb_mean2)+[2]*len(rgb_mean3))

    # 標準化を行う
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # k-means
    km = KMeans(n_clusters=3)
    km.fit(X_scaled, y)

    show_result(X_scaled, y, km)

def pca(img):
    endo, endo_gray = read_fruits_img('endo', path='C:/Users/tanak/image/face/')
    ikuta, ikuta_gray = read_fruits_img('ikuta', path='C:/Users/tanak/image/face/')
    saito, saito_gray = read_fruits_img('saito', path='C:/Users/tanak/image/face/')
    yamashita, yamashita_gray = read_fruits_img('yamashita', path='C:/Users/tanak/image/face/')

    X = np.concatenate([endo_gray, ikuta_gray, saito_gray, yamashita_gray])
    X_flat = X.flatten().reshape(len(X),64**2)/255.

    endo = np.repeat(1, len(endo_gray))
    ikuta = np.repeat(2, len(ikuta_gray))
    saito = np.repeat(3, len(saito_gray))
    yamashita = np.repeat(4, len(yamashita_gray))
    y = np.concatenate([endo, ikuta, saito, yamashita])

    pca = PCA(n_components=50, whiten=True).fit(X_flat)
    X_pca = pca.transform(X_flat)

    fix, axes = plt.subplots(3, 5, figsize=(15, 8), subplot_kw={'xticks': (), 'yticks': ()})
    for i, (component, ax) in enumerate(zip(pca.components_[:15], axes.ravel())):
        ax.imshow(component.reshape(64,64), cmap='viridis')
        ax.set_title("{}. component".format((i+1)))

    return X_pca, y

def ML_method(img_files):
    X_pca, y = pca(img_files)
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y)
    ada = AdaBoostClassifier(DecisionTreeClassifier(), learning_rate=0.002, n_estimators=300)
    ada.fit(X_train, y_train)
    print(ada.score(X_train, y_train))
    print(ada.score(X_test, y_test))    

    svc = LinearSVC(C=0.01)
    svc.fit(X_train, y_train)
    print(svc.score(X_train, y_train))
    print(svc.score(X_test, y_test))

    svm = SVC(kernel='rbf', C=0.9, gamma=0.01)
    svm.fit(X_train, y_train)
    print(svm.score(X_train, y_train))
    print(svm.score(X_test, y_test))

    rf = RandomForestClassifier(n_estimators=60, max_features=40, max_leaf_nodes=60)
    rf.fit(X_train, y_train)
    print(rf.score(X_train, y_train))
    print(rf.score(X_test, y_test))


face_cascade = cv2.CascadeClassifier('libs/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('libs/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('libs/haarcascade_mcs_mouth.xml')
noise_cascade = cv2.CascadeClassifier('libs/haarcascade_mcs_nose.xml')

# イメージファイルの読み込み

def detect_face(img):
    img = img.copy()

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #gray = cv2.medianBlur(gray, 5) 
    
    # 顔を検知
    faces = face_cascade.detectMultiScale(gray)
    logger.info(f'faces: \n{faces}')

    for (x,y,w,h) in faces:
        # 検知した顔を矩形で囲む
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # 顔画像（グレースケール）
        roi_gray = gray[y:y+h, x:x+w]
        # 顔画像（カラースケール）
        roi_color = img[y:y+h, x:x+w]
        # 顔の中から目を検知
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            # 検知した目を矩形で囲む
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img

def face_detection(img_file):
    #read_img('C:/Users/akihiro.tanaka.CORP/Downloads/pictures/', 'yonsentoshin.jpg')
    
    img1, img_gray = read_image(img_file, scale_value=1)

    fig, ax = plt.subplots(1, 1, figsize=(12, 5))
    #ax[0].imshow(detect_face(nishino[7]))
    #ax[0].set_xticks([]);
    #ax[0].set_yticks([]);

    #ax[0].imshow(detect_face(img1))
    #ax[0].set_xticks([]);
    #ax[0].set_yticks([]);

    plt.imshow(detect_face(img1))
    plt.title('Face Detection')
    plt.show()
    cv2.waitKey(0)

def dd(img1):
    X = np.concatenate([img1])
    X_flat = X.flatten().reshape(len(X),64**2)/255.

    X_train, X_test, y_train, y_test = train_test_split(X_flat, y)
    X_train = X_train.reshape(len(X_train), 64, 64)
    X_test = X_test.reshape(len(X_test), 64, 64)

    recognizer = cv2.face.LBPHFaceRecognizer_create() 
    recognizer.train(X_train, np.array(y_train))

    fig, ax = plt.subplots(3, 5, figsize=(16, 8))
    for i in range(15):
        id, confidence = recognizer.predict(X_test[i])
        ax[i//5][i%5].imshow(X_test[i])
        ax[i//5][i%5].set_xticks([])
        ax[i//5][i%5].set_yticks([])
        ax[i//5][i%5].set_title('pred:{}, ans:{}, {}'.format(id, y_test[i], round(100-confidence, 1)))

'''
人検出では、情報をヒストグラム化した**HOG特徴量**が利用されている。
'''
def human_detection(img_file):
    img_rgb, _ = read_image(img_file, scale_value=0.8)
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for i in range(2):
        img = img_rgb.copy()

        if i == 0:
            hog = cv2.HOGDescriptor()
            hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        else:
            hog = cv2.HOGDescriptor((48,96), (16,16), (8,8), (8,8), 9)
            hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

        hogParams = {'winStride': (8, 8), 'padding': (4, 4), 'scale': 1.05}

        human, r = hog.detectMultiScale(img, **hogParams)

        for (x, y, w, h) in human:
            cv2.rectangle(img, (x, y),(x+w, y+h),(0,50,255), 4)

        ax[i].imshow(img);
        #ax[i].set_xticks([]);
        #ax[i].set_yticks([]);

    plt.tight_layout()
    plt.show()
    cv2.waitKey(0)

def bovw():
    X = np.concatenate([endo_gray, ikuta_gray, saito_gray, yamashita_gray])
    X_flat = X.flatten().reshape(len(X),64**2)

    shira = np.repeat(1, len(endo_gray))
    nishi = np.repeat(2, len(ikuta_gray))
    aki = np.repeat(3, len(saito_gray))
    iku = np.repeat(4, len(yamashita_gray))
    y = np.concatenate([shira, nishi, aki, iku])

    X_test = X_flat.reshape(len(X_flat), 64,64)

    matcher = cv2.BFMatcher()
    extractor = cv2.BOWImgDescriptorExtractor(detector, matcher)
    extractor.setVocabulary(centroids)
    probs_test = []

    for file in X:
        descriptor = None
        image = file.copy()
        if image is not None:
            keypoints = detector.detect(image, None)
            if keypoints is not None:
                descriptor = extractor.compute(image, keypoints)[0]
        probs_test.append(descriptor)

    prob = np.zeros([len(probs_test), len(probs_train)])

    rank = []
    for i, p1 in enumerate(probs_test):
        tmp = []
        for j, p2 in enumerate(probs_train):
            tmp.append([j,sum(map(lambda x: min(x[0], x[1]), zip(p1, p2)))])
        rank.append(sorted(tmp, key = lambda x: - x[1])[:5])
    rank = np.array(rank)

    fig, ax = plt.subplots(5, 6, figsize=(18, 12), subplot_kw={'xticks': (), 'yticks': ()})
    for i in range(55):
        ax[i//5][0].imshow(X[i//5])
        ax[i//5][i%5+1].imshow(X[int(rank[i//5,i%5,0])])
        ax[i//5][i%5+1].set_title('prob:{}'.format(round(rank[i//5,i%5,1]*100, 2)))

"""
OpenCV 3で犬と猫を分類できるように学習してみる（BOW: Bag Of Visual Words, KNN: k-Nearest Neighbour, k-meansクラスタリング, KAZE）

https://qiita.com/hitomatagi/items/883770046de5746a5deb
"""
## 画像データのクラスIDとパスを取得
#
# @param dir_path 検索ディレクトリ
# @return data_sets [クラスID, 画像データのパス]のリスト
def getDataSet(dir_path):
    data_sets = []    

    sub_dirs = os.listdir(dir_path)
    for classId in sub_dirs:
        sub_dir_path = dir_path + '/' + classId
        img_files = os.listdir(sub_dir_path)
        for f in img_files:
            data_sets.append([classId, sub_dir_path + '/' + f])

    return data_sets

def bovw_2():
    """main"""
    # 定数定義
    GRAYSCALE = 0
    # KAZE特徴量抽出器
    detector = cv2.KAZE_create()

    """train"""
    print("train start")
    # 訓練データのパスを取得
    train_set = getDataSet('train_img')
    # 辞書サイズ
    dictionarySize = 2
    # Bag Of Visual Words分類器
    bowTrainer = cv2.BOWKMeansTrainer(dictionarySize)

    # 各画像を分析
    for i, (classId, data_path) in enumerate(train_set):
        # 進捗表示
        sys.stdout.write(".")
        # グレースケールで画像読み込み
        gray = cv2.imread(data_path, GRAYSCALE)
        # 特徴点とその特徴を計算
        keypoints, descriptors= detector.detectAndCompute(gray, None)
        # intからfloat32に変換
        descriptors = descriptors.astype(np.float32)
        # 特徴ベクトルをBag Of Visual Words分類器にセット
        bowTrainer.add(descriptors)

    # Bag Of Visual Words分類器で特徴ベクトルを分類
    codebook = bowTrainer.cluster()
    # 訓練完了
    print("train finish")

    """test"""
    print("test start")
    # テストデータのパス取得
    test_set = getDataSet("test_img")

    # KNNを使って総当たりでマッチング
    matcher = cv2.BFMatcher()

    # Bag Of Visual Words抽出器
    bowExtractor = cv2.BOWImgDescriptorExtractor(detector, matcher)
    # トレーニング結果をセット
    bowExtractor.setVocabulary(codebook)

    # 正しく学習できたか検証する
    for i, (classId, data_path) in enumerate(test_set):
        # グレースケールで読み込み
        gray = cv2.imread(data_path, GRAYSCALE)
        # 特徴点と特徴ベクトルを計算
        keypoints, descriptors= detector.detectAndCompute(gray, None)
        # intからfloat32に変換
        descriptors = descriptors.astype(np.float32)
        # Bag Of Visual Wordsの計算
        bowDescriptors = bowExtractor.compute(gray, keypoints)

        # 結果表示
        className = {"0": "cat",
                     "1": "dog"}

        actual = "???"    
        if bowDescriptors[0][0] > bowDescriptors[0][1]:
            actual = className["0"]
        elif bowDescriptors[0][0] < bowDescriptors[0][1]:
            actual = className["1"]

        result = ""
        if actual == "???":
            result = " => unknown."
        elif className[classId] == actual:
            result = " => success!!"
        else:
            result = " => fail"

        print("expected: ", className[classId], ", actual: ", actual, result)

def main(img_file):
    '''
    face_detection(img_file)
    '''
    human_detection(img_file)

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
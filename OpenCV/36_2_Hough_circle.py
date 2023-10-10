'''
【画像処理】くっついている硬貨(コイン)を検出してみよう
Last updated at 2022-03-24Posted at 2022-03-22

https://qiita.com/spc_ehara/items/afba011e15392c7851f6
'''

import argparse
import math
import numpy as np
import statistics
import os, sys, time
import cv2
from matplotlib import pyplot as plt

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

def binalize(src_img):
    gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
    gaus = cv2.GaussianBlur(gray, (15, 15), 5)
    bin = cv2.adaptiveThreshold(gaus, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 4)
    bin = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=3)
    return bin


def filter_object(bin_img, thresh_w, thresh_h, thresh_area):
    nlabels, labels_img, stats, centroids = cv2.connectedComponentsWithStats(bin_img.astype(np.uint8))
    obj_stats_idx = np.where(
        (stats[1:, cv2.CC_STAT_WIDTH] > thresh_w[0])
        & (stats[1:, cv2.CC_STAT_WIDTH] < thresh_w[1])
        & (stats[1:, cv2.CC_STAT_HEIGHT] > thresh_h[0])
        & (stats[1:, cv2.CC_STAT_HEIGHT] < thresh_h[1])
        & (stats[1:, cv2.CC_STAT_AREA] > thresh_area[0])
        & (stats[1:, cv2.CC_STAT_AREA] < thresh_area[1])
    )
    return np.where(np.isin(labels_img - 1, obj_stats_idx), 255, 0).astype(np.uint8)


def find_circle_contours(contours, thresh_area):
    new_cnt = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if thresh_area[0] > area or area > thresh_area[1]:
            continue
        (center_x, center_y), radius = cv2.minEnclosingCircle(cnt)
        circle_area = int(radius * radius * np.pi)
        if circle_area <= 0:
            continue
        area_diff = circle_area / area
        if 0.9 > area_diff or area_diff > 1.1:
            continue
        new_cnt.append(cnt)

    return new_cnt


def find_hole_contours(contours, hierarchy):
    hole_cnt = []
    for cnt_idx, cnt in enumerate(contours):
        for hier_idx, info in enumerate(hierarchy[0]):
            if info[3] == cnt_idx:
                hole_area = cv2.contourArea(contours[hier_idx])
                parent_area = cv2.contourArea(cnt)
                if hole_area < (parent_area * 0.03128) or hole_area > (parent_area * 0.05665):
                    continue
                (center_x, center_y), radius = cv2.minEnclosingCircle(contours[hier_idx])
                circle_area = int(radius * radius * np.pi)
                if circle_area <= 0:
                    continue
                area_diff = circle_area / hole_area
                if 0.8 > area_diff or area_diff > 1.3:
                    continue
                hole_cnt.append(contours[hier_idx])

    return hole_cnt


def _get_moments(cnt):
    M = cv2.moments(cnt)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return (cx, cy)


def _isinclude_cnt(cnt_1, cnt_2):
    cntM_2 = _get_moments(cnt_2)
    flag = cv2.pointPolygonTest(cnt_1, cntM_2, False)
    if flag >= 0:
        return True
    else:
        return False


def extract_feature(src_img, coin_contours, hole_contours):
    if src_img.shape[2] != 3:
        return
    bgr_img = cv2.split(src_img)
    coins_color = []
    hole_features = []
    coins_area = []
    for i, cnt in enumerate(coin_contours):
        blank_img = np.zeros_like(bgr_img[0])
        coin_img = cv2.drawContours(blank_img, [cnt], -1, 255, -1)
        hole_flag = False
        for hcnt in hole_contours:
            if _isinclude_cnt(cnt, hcnt):
                coin_img = cv2.drawContours(coin_img, [hcnt], -1, 0, -1)
                hole_flag = True

        coin_pixels = np.where(coin_img == 255)

        blue = []
        green = []
        red = []
        for p in zip(coin_pixels[0], coin_pixels[1]):
            blue.append(bgr_img[0][p[0]][p[1]])
            green.append(bgr_img[1][p[0]][p[1]])
            red.append(bgr_img[2][p[0]][p[1]])

        coins_color.append([blue, green, red])
        hole_features.append(hole_flag)
        coins_area.append(math.ceil(cv2.contourArea(cnt)))

    return (coins_color, hole_features, coins_area)


def determine_coin_type(coins_color, hole_features):
    coin_type = []
    for (cc, hf) in zip(coins_color, hole_features):
        b_ave = math.ceil(np.average(cc[0]))
        g_ave = math.ceil(np.average(cc[1]))
        r_ave = math.ceil(np.average(cc[2]))
        b_mode = math.ceil(statistics.mode(cc[0]))
        g_mode = math.ceil(statistics.mode(cc[1]))
        r_mode = math.ceil(statistics.mode(cc[2]))
        rb_ave_diff = r_ave - b_ave
        rg_ave_diff = r_ave - g_ave
        gb_ave_diff = g_ave - b_ave
        rb_mode_diff = r_mode - b_mode
        rg_mode_diff = r_mode - g_mode
        gb_mode_diff = g_mode - b_mode

        guess_type = 0
        if hf is True:
            if (b_ave / r_ave) < 0.6 and (b_ave / r_ave) > 0.4:
                guess_type = 5
            else:
                guess_type = 50
        else:
            if (b_ave / r_ave) < 0.6 and (b_ave / r_ave) > 0.4:
                guess_type = 10
            elif (rb_ave_diff + rg_ave_diff + gb_ave_diff) < 50:
                guess_type = 1
            elif (rb_mode_diff + rg_mode_diff + gb_mode_diff) < 135 or (rg_mode_diff - gb_mode_diff) > 70:
                guess_type = 100
            else:
                guess_type = 500

        coin_type.append(guess_type)

    return coin_type


def render(dst_img, coin_contours, hole_contours, coin_type):
    for h in hole_contours:
        cv2.drawContours(dst_img, [h], -1, (255, 0, 0), 12)

    for (cnt, type) in zip(coin_contours, coin_type):
        cv2.drawContours(dst_img, [cnt], -1, (0, 0, 255), 6)
        cv2.putText(dst_img, str(type), _get_moments(cnt), cv2.FONT_HERSHEY_PLAIN, 8, (0, 0, 255), 8, cv2.LINE_AA)


# 今回追加したところ
def circle_separator(bin_img):
    fill_bin = np.zeros_like(bin_img)
    
    # OpenCV version == 3 or other 
    if major == '3':
        image ,contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(fill_bin, contours, -1, 255, -1)
    circles = cv2.HoughCircles(
        fill_bin, cv2.HOUGH_GRADIENT, dp=1, minDist=180, param1=20, param2=10, minRadius=100, maxRadius=250
    )
    if circles is None:
        return bin_img
    circles = np.uint16(np.around(circles))
    separated_img = bin_img.copy()
    for i in circles[0, :]:
        cv2.circle(separated_img, (i[0], i[1]), i[2], 0, 2)
    return separated_img


def parse_args() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("IN_IMG", help="Input file")
    parser.add_argument("OUT_IMG", help="Output file")
    args = parser.parse_args()

    return (args.IN_IMG, args.OUT_IMG)

'''
too many values to unpack calling cv2.findContours
https://stackoverflow.com/questions/43960257/too-many-values-to-unpack-calling-cv2-findcontours

OpenCV 3.x:
>>> import cv2
>>> help(cv2.findContours)
Help on built-in function findContours:

findContours(...)
    findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> image, contours, hierarchy

This means that in your script the correct way to call findContours when using OpenCV 3.x would be something like

(_, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)    
'''
def main(in_img) -> None:
    #(in_img, out_img) = parse_args()

    src_img = cv2.imread(in_img)
    if src_img is None:
        return
    height, width = src_img.shape[:2]
    bin_img = binalize(src_img)

    max_area = math.ceil((width * height) / 2)
    min_area = math.ceil((width * height) / 100)
    bin_img = filter_object(bin_img, (0, (width / 1.5)), (0, (height / 1.5)), (min_area, max_area))

    bin_img = cv2.morphologyEx(
        bin_img, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=5
    )

    separated_img = circle_separator(bin_img)

    if major == '3':
        image, contours, hierarchy = cv2.findContours(separated_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv2.findContours(separated_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    coin_contours = find_circle_contours(contours, (min_area, max_area))

    dst_img = src_img.copy()
    for cnt in coin_contours:
        (center_x, center_y), radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(dst_img, (int(center_x), int(center_y)), int(radius), (0, 0, 255), 15)

    cv2.imwrite("media/35_2_hough_circle.jpg", dst_img)
    
    cv2.imshow('Circle Detector', dst_img)
    c = cv2.waitKey()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='35_2_Hough_circle')
   
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
    path_infinicloud = '/home/philphoenix/infinicloud/OpenCV'
    if os.path.isfile(os.path.join(path_infinicloud, img_file)):
        main((os.path.join(path_infinicloud, img_file)))           

    
    est_timer(start_time=t0)

    


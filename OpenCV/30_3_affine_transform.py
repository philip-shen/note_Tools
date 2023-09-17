"""
完全に理解するアフィン変換
https://qiita.com/koshian2/items/c133e2e10c261b8646bf
"""
import os, sys, time
import numpy as np
from numpy.random import normal
import scipy as sp
import cv2
import argparse
from matplotlib import pyplot as plt
from PIL import Image,ImageSequence

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


def identity(img_file):
    image = cv2.imread(img_file)[:,:,::-1]
    
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],
                    [0.0, 1.0],
                    [1.0, 0.0]], np.float32)
    
    affine = cv2.getAffineTransform(src, src)
    converted = cv2.warpAffine(image, affine, (w, h))
    
    plt.imshow(converted)
    plt.title("Identity")
    plt.show()

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

def shift_x(image, shift):
    h, w = image.shape[:2]
    '''
    This line creates a NumPy array called src representing the source points for the affine transformation. 
    These points are defined in normalized coordinates (ranging from 0.0 to 1.0). 
    The three points are the top-left corner, top-right corner, and bottom-left corner of the original image.
    '''    
    src = np.array([[0.0, 0.0],
                    [0.0, 1.0],
                    [1.0, 0.0]], np.float32)
    
    dest = src.copy()
    '''
    This line applies the horizontal shift to the dest array by adding the shift value to 
    the x-coordinates of all the points. 
    This will cause the image to be shifted horizontally by the specified amount.
    '''
    dest[:,0] += shift # シフトするピクセル値
    """
    shift:0,
    dest: [[0. 0.]
            [0. 1.]
            [1. 0.]]

    shift:180,
    dest: [[180.   0.]
            [180.   1.]
            [181.   0.]]
    """
    logger.info(f'\nshift:{shift},\n dest: {dest}')

    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (w, h))

'''
處理 gif 動畫
https://steam.oxxostudio.tw/category/python/ai/opencv-gif.html
'''
def horizontal_x(img_file):
    image = cv2.imread(img_file)
    
    '''
    idx = 0
    fig, ax = plt.subplots(1, 10, figsize=(16, 5))
    for shift in range(0, 200, 20):
        converted = shift_x(image, shift)
        ax[idx].imshow(converted)
        
        ax[idx].set_title(f"Shift_X:{shift}")
        ax[idx].set_xticks([])
        ax[idx].set_yticks([])

        idx += 1
        
    plt.tight_layout()    
    plt.show()

    cv2.waitKey()
    '''
    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = shift_x(image, i*20)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220+i*20,30),(440+i*20,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Shift_X_{i*20:03d}'
        org = (230+i*20,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_horizontal_x.gif')

def shift_y(image, shift):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src.copy()
    '''
    This line applies the horizontal shift to the dest array by adding the shift value to 
    the y-coordinates of all the points. 
    This will cause the image to be shifted horizontally by the specified amount.
    '''
    dest[:,1] += shift # シフトするピクセル値
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (w, h))

def vertical_y(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = shift_y(image, i*20)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30+i*20),(440,90+i*20),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Shift_Y_{i*20:03d}'
        org = (230,70+i*20)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_vertical_y.gif')

def shift_x_y(image, shifts):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    
    #dest = src + shifts.reshape(1,-1).astype(np.float32)
    dest = shifts
    
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (w, h))

def random_shift(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_shifts = [[-11, 80], [10,-23], [-30,-50], [10, 24], [-24, -10],
                   [11,-80], [-10,23], [33,55], [-60, -74], [24, 10]]
    list_fnames= []
    for i in range(num_frames):
        src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
        shifts = src.copy()
        '''
        This line applies the horizontal shift to the dest array by adding the shift value to 
        the x-coordinates of all the points. 
        This will cause the image to be shifted horizontally by the specified amount.
        '''
        shifts[:,0] += list_shifts[i][0] # シフトするピクセル値

        logger.info(f'\nshifts[:,0]:{shifts}')
        '''
        This line applies the horizontal shift to the dest array by adding the shift value to 
        the y-coordinates of all the points. 
        This will cause the image to be shifted horizontally by the specified amount.
        '''
        shifts[:,1] += list_shifts[i][1] # シフトするピクセル値
        logger.info(f'\nshifts[:,1]:{shifts}')
        
        converted = shift_x_y(image, shifts)

        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(100,30),(550,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Random_Shift: ({list_shifts[i][0]}, {list_shifts[i][1]})'
        org = (120,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_random_shift.gif')

def expand(image, ratio):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src * ratio
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (2*w, 2*h), cv2.INTER_LANCZOS4) # 補間法も指定できる

def scale(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = expand(image, 0.2*(i+1))
        
        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_scale.gif')

def convert_shear_X(image, shear):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src.copy()
    dest[:,0] += (shear / h * (h - src[:,1])).astype(np.float32)
    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (w, h))

def convert_shear_Y(image, shear, opt_startpt='upper_right'):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src.copy()

    if opt_startpt.lower() == 'upper_right':
        dest[:,1] += (shear / w * (w - src[:,0])).astype(np.float32)
    elif opt_startpt.lower() == 'upper_left':
        dest[:,1] += (shear / w * src[:,0]).astype(np.float32)

    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (w, h))

def shear_X(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = convert_shear_X(image, -200+40*i)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30),(455,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Shear_X:{(-200+40*i):03d}'
        org = (230,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_shear_x.gif')

def shear_Y(img_file, opt_start_pt='upper_right'):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = convert_shear_Y(image, -200+40*i, opt_start_pt)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30),(455,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Shear_Y:{(-200+40*i):03d}'
        org = (230,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    if opt_start_pt.lower() == 'upper_right':
        jpg_to_gif( list_fnames, '30_5_animation_shear_y_upper_right.gif')
    elif opt_start_pt.lower() == 'upper_left':
        jpg_to_gif( list_fnames, '30_5_animation_shear_y_upper_left.gif')

def convert_flip(image, opt):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src.copy()

    if opt.lower() == 'horizontal':
        dest[:,0] = w - src[:,0] 
    if opt.lower() == 'vertical':
        dest[:,1] = h - src[:,1] 

    affine = cv2.getAffineTransform(src, dest)
    return cv2.warpAffine(image, affine, (w, h))

def flip(img_file, opt_direction):
    image = cv2.imread(img_file)
    
    # Draw the animation frames
    list_fnames = []
    converted = convert_flip(image, opt_direction)
    # Save the frame to a file
    filename = f'frame_0.jpg'
    cv2.imwrite(filename, converted)
    list_fnames.append(filename)

    jpg_to_gif( list_fnames, f'30_5_animation_{opt_direction}_flip.gif')
    
    logger.info(f'30_5_animation_{opt_direction}_flip.gif generated.')

def affine_rotate(image, angle):
    h, w = image.shape[:2]

    # 三角関数を使った書き方（π/3=60度回転させる場合）
    src = np.array([[0.0, 0.0],
                    [0.0, 1.0],
                    [1.0, 0.0]], np.float32)
    
    dest = np.array([[0.0, 0.0], 
                     [np.sin(angle),np.cos(angle)], #[np.sin(np.pi/3),np.cos(np.pi/3)], 
                     [np.cos(angle),-np.sin(angle)]], #[np.cos(np.pi/3),-np.sin(np.pi/3)]], 
                     np.float32)
    
    affine = cv2.getAffineTransform(src, dest)
    print(affine)
    return cv2.warpAffine(image, affine, (w, h))

def convert_rotate(image, angle):
    h, w = image.shape[:2]
    affine = cv2.getRotationMatrix2D((0,0), angle, 1.0)
    return cv2.warpAffine(image, affine, (w, h))

def rotate(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = convert_rotate(image, 90-18*i)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30),(400,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Rotat:{(-90+18*i):02d}'
        org = (230,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_rotate.gif')

def convert_rotate_center(image, angle):
    h, w = image.shape[:2]
    affine = cv2.getRotationMatrix2D((w/2.0, h/2.0), angle, 1.0)
    return cv2.warpAffine(image, affine, (w, h))

def rotate_center(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 10
    list_fnames = []
    for i in range(num_frames):
        converted = convert_rotate_center(image, -90+18*i)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30),(400,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Rotat:{(-90+18*i):02d}'
        org = (230,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_rotate_center.gif')

def covert_rotate_fit(image, angle):
    h, w = image.shape[:2]
    # 回転後のサイズ
    radian = np.radians(angle)
    sine = np.abs(np.sin(radian))
    cosine = np.abs(np.cos(radian))
    tri_mat = np.array([[cosine, sine],[sine, cosine]], np.float32)
    old_size = np.array([w,h], np.float32)
    new_size = np.ravel(np.dot(tri_mat, old_size.reshape(-1,1)))
    # 回転アフィン
    affine = cv2.getRotationMatrix2D((w/2.0, h/2.0), angle, 1.0)
    # 平行移動
    affine[:2,2] += (new_size-old_size)/2.0
    # リサイズ
    affine[:2,:] *= (old_size / new_size).reshape(-1,1)
    return cv2.warpAffine(image, affine, (w, h))

def rotate_fit(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 36
    list_fnames = []
    for i in range(num_frames):
        converted = covert_rotate_fit(image, 0+10*i)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30),(400,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Rotat:{(0+10*i):02d}'
        org = (230,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_rotate_fit.gif', ms=1000)

def draw_region(image, bounding_box):
    canvas= image.copy()
    canvas = cv2.line(canvas, tuple(bounding_box[0,0]), tuple(bounding_box[0,1]), (0,255,0), 5)
    canvas = cv2.line(canvas, tuple(bounding_box[0,1]), tuple(bounding_box[0,2]), (0,255,0), 5)
    canvas = cv2.line(canvas, tuple(bounding_box[0,2]), tuple(bounding_box[0,3]), (0,255,0), 5)
    canvas = cv2.line(canvas, tuple(bounding_box[0,3]), tuple(bounding_box[0,0]), (0,255,0), 5)
    return canvas

def converted_rotate_fit_with_region(image, angle):
    h, w = image.shape[:2]

    # 画像の変換
    # 回転後のサイズ
    radian = np.radians(angle)
    sine = np.abs(np.sin(radian))
    cosine = np.abs(np.cos(radian))
    tri_mat = np.array([[cosine, sine],[sine, cosine]], np.float32)
    
    old_size = np.array([w,h], np.float32)
    new_size = np.ravel(np.dot(tri_mat, old_size.reshape(-1,1)))
    # 回転アフィン
    affine = cv2.getRotationMatrix2D((w/2.0, h/2.0), angle, 1.0)
    # 平行移動
    affine[:2,2] += (new_size-old_size)/2.0
    # リサイズ
    affine[:2,:] *= (old_size / new_size).reshape(-1,1)
    converted_image = cv2.warpAffine(image, affine, (w, h))

    # アノテーションの変換
    # 元の画像の顔の領域(Bounding Boxが複数ある場合にそなえて3階で定義)
    '''
    bbox = np.array([[[165,185],
                      [320,185],
                      [165,365],
                      [320,365]]], np.float32)
    '''
    bbox = np.array([[[60,323],
                      [518,9],
                      [618,95],
                      [158,408]]], np.float32)
    
    bbox_matrix = np.concatenate([bbox, np.ones((bbox.shape[0],bbox.shape[1],1), np.float32)], axis=-1)
    # 変換後の顔の領域
    converted_bbox = np.tensordot(affine, bbox_matrix.T, 1).T
    return draw_region(converted_image, converted_bbox.astype(np.int32))

def rotate_fit_with_region(img_file):
    image = cv2.imread(img_file)

    # Draw the animation frames
    num_frames = 36
    list_fnames = []
    for i in range(num_frames):
        converted = converted_rotate_fit_with_region(image, 0+10*i)
        
        # 在圖形中間繪製黑色方塊
        cv2.rectangle(converted,(220,30),(400,90),(0,0,0),-1)

        # 在黑色方塊上方加入文字
        text = f'Rotat:{(0+10*i):02d}'
        org = (230,70)
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (255,255,255)
        thickness = 2
        lineType = cv2.LINE_AA
        cv2.putText(converted, text, org, fontFace, fontScale, color, thickness, lineType)

        # Save the frame to a file
        filename = f'frame_{i:02d}.jpg'
        cv2.imwrite(filename, converted)
        list_fnames.append(filename)

    logger.info(f'{num_frames} frames generated.')

    jpg_to_gif( list_fnames, '30_5_animation_rotate_fit_with_region.gif', ms=1000)

def main(img_file):
    '''
    vertical_y(img_file)
    horizontal_x(img_file)
    random_shift(img_file)
    scale(img_file)
    shear_X(img_file)
    shear_Y(img_file, opt_start_pt='upper_right')
    shear_Y(img_file, opt_start_pt='upper_left')
    flip(img_file, opt_direction='horizontal')
    flip(img_file, opt_direction='vertical')
    rotate(img_file)
    rotate_center(img_file)
    rotate_fit(img_file)    
    '''
    
    '''
    image = cv2.imread(img_file)[:,:,::-1]
    bbox = np.array([[[60,323],
                      [518,9],
                      [618,95],
                      [158,408]]], np.float32)
    image = draw_region(image, bbox)
    plt.imshow(image)
    plt.show()
    '''

    rotate_fit_with_region(img_file)
    identity(img_file)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='30_3_affine_transform')
   
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
    
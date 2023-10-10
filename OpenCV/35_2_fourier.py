"""
python+opencvで画像処理の勉強4 周波数領域におけるフィルタリング
https://qiita.com/tanaka_benkyo/items/bfa35e7f08faa7b7a985
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def read_image(img_file):
    #img_bgr = cv2.imread("C:/Users/akihiro.tanaka.CORP/Downloads/pictures/"+img_name+".jpg")
    img_bgr = cv2.imread(img_file)
    h, w = img_bgr.shape[:2]
    scale = (640 * 480 / (w * h)) ** 0.5
    img_bgr_resize = cv2.resize(img_bgr, dsize=None, fx=scale, fy=scale)
    img_rgb = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr_resize, cv2.COLOR_BGR2GRAY)
    return img_rgb, img_gray

def fouier(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    img_rgb2, img_gray2 = read_image(img_files[1])
    img_rgb3, img_gray3 = read_image(img_files[2])
    img_rgb4, img_gray4 = read_image(img_files[3])
    
    imgs = [img_gray1, img_gray2, img_gray3, img_gray4]

    fig, ax = plt.subplots(2, 4, figsize=(18, 5))
    for i in range(4):
        dft = cv2.dft(np.float32(imgs[i]), flags = cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))
        """
        numpyによるフーリエ変換
        f = np.fft.fft2(imgs[i])
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        """
        ax[0][i].imshow(imgs[i], 'gray')
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(magnitude_spectrum, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])

    plt.show()

def make_mask(img, R, inv=False):
    height = img.shape[0]
    width  = img.shape[1]

    center_w = height//2
    center_h = width//2
    
    if inv:
        n = 0
        filter_matrix = np.ones([height, width])
    else:
        n = 1
        filter_matrix = np.zeros([height, width])

    for i in range(0, height):
         for j in range(0, width):
                if (i-center_w)*(i-center_w) + (j-center_h)*(j-center_h) < R*R:
                               filter_matrix[i][j] = n
    
    return filter_matrix

def masked_fft(img, mask):
    dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)*mask

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    f_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
    
    dft2 = cv2.dft(np.float32(img_back),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift2 = np.fft.fftshift(dft2)

    magnitude_spectrum2 = 20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))
    
    return magnitude_spectrum, img_back, magnitude_spectrum2

def make_Gauss_mask(x):
    X = np.matrix(x).T
    x_mu = X - mu

    w1 = np.matmul(inv_sig, x_mu)
    w2 = -0.5 * np.matmul(x_mu.T, w1)

    N = 1/(np.sqrt(((2*np.pi)**2) * np.abs(det))) * np.exp(w2)
    return N[0,0]

def gauss_mask(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    x1_range = img_gray1.shape[1] // 2
    x2_range = img_gray1.shape[0] // 2

    x1 = np.arange(-x1_range, x1_range+1)
    x2 = np.arange(-x2_range, x2_range)

    sigmas = [100, 900, 1600]
    M=[0, 0]
    mu = np.matrix(M).T

    g_masks = []

    for i in range(3):
        S=[[sigmas[i],0],[0,sigmas[i]]]
        sigma = np.matrix(S)
        inv_sig = np.linalg.inv(sigma)
        det = np.linalg.det(sigma)
    
        g2 = np.array([[make_Gauss_mask([i, j]) for i in x1] for j in x2])
        g2 *= 1/g2.max()
        g2 = np.array([g2, g2]).transpose(1, 2, 0)
    
        g_masks.append(g2)
    
    return g_masks

def lowpass(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    masks = np.array([np.array([make_mask(img_gray1, r), 
                                make_mask(img_gray1, r)]).transpose(1, 2, 0) for r in [30, 80, 160]])

    plt.imshow(img_gray1, 'gray');
    plt.xticks([]);
    plt.yticks([]);

    fig, ax = plt.subplots(3, 3, figsize=(16, 9))
    for i in range(3):
        spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray1, masks[i])
        ax[0][i].imshow(spectrum_img1, 'gray')
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(img_ifft, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
    
        ax[2][i].imshow(spectrum_img2, 'gray')
        ax[2][i].set_xticks([])
        ax[2][i].set_yticks([])

    plt.show()

def lowpass_Gauss(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    plt.imshow(img_gray1, 'gray')
    g_masks=gauss_mask(img_files[0])

    fig, ax = plt.subplots(3, 3, figsize=(16, 9))
    for i in range(3):
        spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray1, g_masks[i])
        ax[0][i].imshow(spectrum_img1, 'gray', vmin=0, vmax=300)
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(img_ifft, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
    
        ax[2][i].imshow(spectrum_img2, 'gray')
        ax[2][i].set_xticks([])
        ax[2][i].set_yticks([])

    plt.show()

def highpass(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    masks = np.array([np.array([make_mask(img_gray1, r, True), 
                                make_mask(img_gray1, r, True)]).transpose(1, 2, 0) for r in [30, 80, 160]])

    plt.imshow(img_gray1, 'gray')

    fig, ax = plt.subplots(3, 3, figsize=(16, 9))
    for i in range(3):
        spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray1, masks[i])
        ax[0][i].imshow(spectrum_img1, 'gray')
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(img_ifft, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
    
        ax[2][i].imshow(spectrum_img2, 'gray')
        ax[2][i].set_xticks([])
        ax[2][i].set_yticks([])

def highpass_Gauss(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    plt.imshow(img_gray1, 'gray')
    g_masks=gauss_mask(img_files[0])

    fig, ax = plt.subplots(3, 3, figsize=(16, 9))
    for i in range(3):
        spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray1, 1-g_masks[i])
        ax[0][i].imshow(spectrum_img1, 'gray')
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(img_ifft, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
    
        ax[2][i].imshow(spectrum_img2, 'gray')
        ax[2][i].set_xticks([])
        ax[2][i].set_yticks([])

def band_pass_filter(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    masks_1 = np.array([np.array([make_mask(img_gray1, r), 
                                  make_mask(img_gray1, r)]).transpose(1, 2, 0) for r in [30, 50, 100]])
    masks_2 = np.array([np.array([make_mask(img_gray1, r), 
                                  make_mask(img_gray1, r)]).transpose(1, 2, 0) for r in [50, 100, 180]])
    mask_diff = masks_2 - masks_1

    plt.imshow(img_gray1, 'gray')

    fig, ax = plt.subplots(3, 3, figsize=(16, 9))
    for i in range(3):
        spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray1, mask_diff[i])
        ax[0][i].imshow(spectrum_img1, 'gray')
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(img_ifft, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
    
        ax[2][i].imshow(spectrum_img2, 'gray')
        ax[2][i].set_xticks([])
        ax[2][i].set_yticks([])

def pre_emphasis_filter(img_files):
    img_rgb1, img_gray1 = read_image(img_files[0])
    
    plt.imshow(img_gray1, 'gray')
    g_masks=gauss_mask(img_files[0])

    K = [1, 2, 3]

    fig, ax = plt.subplots(3, 3, figsize=(16, 9))
    for i in range(3):
        spectrum_img1, img_ifft, spectrum_img2 = masked_fft(img_gray1, K[i]+1-K[i]*g_masks[1])
        ax[0][i].imshow(spectrum_img1, 'gray')
        ax[0][i].set_xticks([])
        ax[0][i].set_yticks([])
    
        ax[1][i].imshow(img_ifft, 'gray')
        ax[1][i].set_xticks([])
        ax[1][i].set_yticks([])
    
        ax[2][i].imshow(spectrum_img2, 'gray')
        ax[2][i].set_xticks([])
        ax[2][i].set_yticks([])

if __name__ == '__main__':
    fouier()

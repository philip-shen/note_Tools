/*
【Day9】OpenCV影像強度轉換：調整亮度和對比度 

https://ithelp.ithome.com.tw/articles/10323028
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "math.h"
#include "opencv2/intensity_transform.hpp"
#include "opencv2/core/utils/logger.hpp"

#define USE_OPENCV 0

using namespace std;

// 設置滑動條的回調函數
//void trackbar_thresholding_callback(int position, void*);
//void trackbar_gamma_correction_callback(int position, void*);

cv::Mat grayImage;

// Gamma校正的滑動條回調函數
void trackbar_gamma_correction_callback(int position, void*)
{
    double gamma = position / 10.0;
    cv::Mat dst;

#if USE_OPENCV
    cv::intensity_transform::gammaCorrection(gray52_grayscaleImage, dst, gamma);
#else
    dst = cv::Mat::zeros(grayImage.rows, grayImage.cols, CV_8UC1);

    for (int y = 0; y < grayImage.rows; y++)
    {
        for (int x = 0; x < grayImage.cols; x++)
        {
            uchar value = grayImage.at<uchar>(y, x);
            float input = value / 255.0f;
            dst.at<uchar>(y, x) = (uchar)255 * std::pow(input, gamma);
        }
    }
#endif

    cv::imshow("Gamma Correction", dst);
}

// 二值化的滑動條回調函數
void trackbar_thresholding_callback(int position, void*)
{
    double thresholdValue = position;
    cv::Mat binaryImage;

#if USE_OPENCV
    cv::threshold(grayImage, binaryImage, thresholdValue, 255, CV_8UC1);
#else
    binaryImage = cv::Mat::zeros(grayImage.rows, grayImage.cols, CV_8UC1);
    
    for (int y = 0; y < grayImage.rows; y++)
    {
        for (int x = 0; x < grayImage.cols; x++)
        {
            uchar value = grayImage.at<uchar>(y, x);
            if (value >= thresholdValue)
            {
                binaryImage.at<uchar>(y, x) = 255;
            }
        }
    }
#endif
    cv::imshow("Binary Image", binaryImage);
}

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT);

    // 讀取影像
    grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_GRAYSCALE);

    // 建立二值化影像視窗和滑動條
    cv::namedWindow("Binary Image", cv::WindowFlags::WINDOW_NORMAL);
    cv::resizeWindow("Binary Image", 512.0f * ((float)grayImage.cols / grayImage.rows), 512);
    cv::createTrackbar("Threshold", "Binary Image", NULL, 255, trackbar_thresholding_callback);
    cv::imshow("Binary Image", grayImage);

    // 建立Gamma校正視窗和滑動條
    cv::namedWindow("Gamma Correction", cv::WindowFlags::WINDOW_NORMAL);
    cv::resizeWindow("Gamma Correction", 512.0f * ((float)grayImage.cols / grayImage.rows), 512);
    cv::createTrackbar("Gamma", "Gamma Correction", NULL, 100, trackbar_gamma_correction_callback);
    cv::imshow("Gamma Correction", grayImage);

    // 顯示底片影像
    cv::imshow("Negative Transformation", 255 - grayImage);

    cv::waitKey(0);
    return 0;
}
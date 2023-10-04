/*
【Day13】使用OpenCV實現OTSU大津演算法 

https://ithelp.ithome.com.tw/articles/10323537
*/

#include <iostream>
#include <inttypes.h>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/logger.hpp>
#include "boost/timer/timer.hpp"

#define USE_OPENCV 0

using namespace std;

// 函數原型
uchar otsu(cv::Mat hist);
cv::Mat calcHist(cv::Mat image);

// 計算灰度影像的直方圖
cv::Mat calcHist(cv::Mat image)
{
    cv::Mat hist = cv::Mat::zeros(cv::Size(1, 256), CV_32SC1);

    for (int y = 0; y < image.rows; y++)
    {
        for (int x = 0; x < image.cols; x++)
        {
            uchar value = image.at<uchar>(y, x);
            hist.at<int>(value)++;
        }
    }
    return hist;
}

// 使用OTSU方法計算閾值
uchar otsu(cv::Mat hist)
{
    cv::Mat hist_pmf;
    hist.convertTo(hist_pmf, CV_32F);
    hist_pmf /= cv::sum(hist)[0];

    float u = 0.0f;
    for (int i = 0; i < 256; i++)
    {
        u += i * hist_pmf.at<float>(i);
    }

    float w1 = 0.0f;
    float sum1 = 0.0f;
    float max_sigma_b_2 = -1.0f;
    uchar threshold = 0;

    for (int t = 0; t < 256; t++)
    {
        //累加背景權重
        w1 += hist_pmf.at<float>(t);
        if (w1 == 0.0f)
            continue;

        //累加前景權重
        float w2 = 1.0f - w1;
        if (w2 == 0.0f)
            continue;
        sum1 += t * hist_pmf.at<float>(t);

        //計算背景平均值
        float u1 = sum1 / w1;

        float sum2 = u - sum1;

        //計算前景平均值
        float u2 = sum2 / w2;

        //計算類間變異數
        float sigma_b_2 = w1 * w2 * (u1 - u2) * (u1 - u2);

        if (sigma_b_2 > max_sigma_b_2)
        {
            max_sigma_b_2 = sigma_b_2;
            threshold = t;
        }
    }

    return threshold;
}

int main()
{
    //boost::timer::cpu_timer timer;

    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);

    // 讀取灰度影像
    cv::Mat grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_GRAYSCALE);
    cv::Mat binaryImage;

#if USE_OPENCV
    // 使用OpenCV的OTSU閾值化
    double threshold = cv::threshold(grayImage, binaryImage, 0, 255, cv::THRESH_OTSU);
    printf("OTSU threshold:%d", (int)threshold);
#else
    // 計算影像的直方圖
    cv::Mat hist = calcHist(grayImage);

    // 使用OTSU方法計算閾值
    uchar threshold = otsu(hist);
    printf("OTSU threshold:%d", threshold);

    // 根據計算得到的閾值進行二值化
    cv::threshold(grayImage, binaryImage, threshold, 255, cv::THRESH_BINARY);
#endif

    // 顯示二值化影像
    cv::imshow("Binary Image", binaryImage);
    cv::waitKey(0);

    //std::string result = timer.format(3,"処理時間:%w秒"); // 結果文字列を取得する
    //std::cout << result << std::endl;
    
    return 0;
}
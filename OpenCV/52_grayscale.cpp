/*
【Day7】使用OpenCV將彩色圖片灰階化 
https://ithelp.ithome.com.tw/articles/10319572
*/

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/logger.hpp>

#define USE_OPENCV 0

int main() {
    cv::utils::logging::setLogLevel(cv::utils::logging::LogLevel::LOG_LEVEL_SILENT);

    // 讀取圖片
    cv::Mat colorImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_UNCHANGED);

    // 創建灰階影像
    cv::Mat grayImage;
#if USE_OPENCV
	// 使用OpenCV轉換彩色影像為灰階
    cv::cvtColor(colorImage, grayImage, cv::COLOR_BGR2GRAY); 
#else
    int width = colorImage.cols;
    int height = colorImage.rows;
    grayImage = cv::Mat(height, width, CV_8UC1); 
    // 遍歷每個像素，手動計算灰階值
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
			// 獲取彩色影像中的像素值
            cv::Vec3b pixel = colorImage.at<cv::Vec3b>(y, x); 
			// 計算灰階值
            uchar grayValue = 0.299 * pixel[2] + 0.587 * pixel[1] + 0.114 * pixel[0];
            // 將灰階值設置到對應位置
            grayImage.at<uchar>(y, x) = grayValue; 
        }
    }
#endif

    // 顯示原始彩色圖和轉換後的灰階圖
    cv::imshow("Color Image", colorImage); 
    cv::imshow("Gray Image", grayImage); 
    cv::waitKey(0); 
    return 0;
}
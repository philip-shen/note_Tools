/*
【Day12】OpenCV 自適應二值化(Adaptive Thresholding)：降低亮度干擾 

https://ithelp.ithome.com.tw/articles/10323561
*/
#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"
#include <boost/timer/timer.hpp>

#define USE_OPENCV 0

//using namespace std;
using namespace boost::timer;

// 存儲灰階影像的變數
cv::Mat grayImage; 

void trackbar_callback(int position, void*) {
	// 讀取"Offset"滑動條的當前值
	int offset = cv::getTrackbarPos("Offset", "Binary Image"); 
	// 讀取"Size"滑動條的當前值
	int size = cv::getTrackbarPos("Size", "Binary Image");
	if (size % 2 == 0) {
		// 確保"Size"是奇數，因為自適應二值化需要奇數的核函數大小
		size++; 
	}
	if (size == 1)
		return;

	// 存儲自適應二值化的結果影像
	cv::Mat binaryImage; 

#if USE_OPENCV
	// 使用OpenCV的自適應二值化函數
	cv::adaptiveThreshold(grayImage, binaryImage, 255, cv::ADAPTIVE_THRESH_MEAN_C, cv::THRESH_BINARY, size, offset); 
#else
	// 創建一個初始值為0的二值影像
	binaryImage = cv::Mat::zeros(grayImage.rows, grayImage.cols, CV_8UC1);
	cv::Mat integralImage;
	// 計算灰階影像的積分圖
	cv::integral(grayImage, integralImage); 
	for (int y = 0; y < binaryImage.rows; y++) {
		for (int x = 0; x < binaryImage.cols; x++) {
			int startX = std::max(x - size / 2, 0);
			int startY = std::max(y - size / 2, 0);
			int endX = std::min(x + size / 2, grayImage.cols - 1);
			int endY = std::min(y + size / 2, grayImage.rows - 1);

			//求出Kernal內的加總
			int blockSum = integralImage.at<int>(endY + 1, endX + 1) - integralImage.at<int>(endY + 1, startX) - integralImage.at<int>(startY, endX + 1) + integralImage.at<int>(startY, startX);
			//求出Kernal內的像素總數
			int blockSizePixels = (endY - startY + 1) * (endX - startX + 1);
			//求出Kernal內的平均值
			double mean = static_cast<double>(blockSum) / blockSizePixels;

			//求出二值化的閥值
			double threshold = mean - offset;

			if (grayImage.at<uchar>(y, x) > threshold) {
				// 設置二值影像的像素值
				binaryImage.at<uchar>(y, x) = 255; 
			}
		}
	}
#endif

	cv::imshow("Binary Image", binaryImage); // 顯示自適應二值化的結果影像
}


int main()
{
	// 設定OpenCV日誌級別為SILENT，禁止輸出日誌
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT); 
	grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/adaptive_thresholding.jpg", cv::IMREAD_GRAYSCALE);

    cv::namedWindow("Binary Image", cv::WindowFlags::WINDOW_NORMAL); 
    cv::resizeWindow("Binary Image", 512.0f * ((float)grayImage.cols / grayImage.rows), 512);

	// 創建名為"Offset"的滑動條，範圍為0到255
    cv::createTrackbar("Offset", "Binary Image", NULL, 255, trackbar_callback); 
	// 創建名為"Size"的滑動條，範圍為0到1023
    cv::createTrackbar("Size", "Binary Image", NULL, 1023, trackbar_callback);
	// 初始化"Size"滑動條的值為3
	cv::setTrackbarPos("Size", "Binary Image", 3); 

	//std::string result = boost::timer.format(3,"処理時間:%w秒"); // 結果文字列を取得する
	//std::cout << result << std::endl;

	// 等待使用者操作，直到按下任意按鍵結束程式
	cv::waitKey(0); 
	return 0;
}
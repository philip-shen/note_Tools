/*
【Day15】探索OpenCV中的影像平滑化：模糊、降噪 

https://ithelp.ithome.com.tw/articles/10325234
*/

#include "opencv2/opencv.hpp"
#define USE_OPENCV 0
using namespace std;

cv::Mat grayImage;

// 回調函數，用於平均濾波
void mean_filter_trackbar_callback(int size, void*) {
	if (size % 2 == 0)
		size++;
	cv::Mat dst;
#if USE_OPENCV
	// 使用OpenCV函數執行平均濾波
	cv::boxFilter(grayImage, dst, grayImage.depth(), cv::Size(size, size));
#else
    // 使用自訂的均值濾波內核進行影像處理
    cv::Mat kernel = cv::Mat::ones(size, size, CV_32F);
	kernel /= cv::sum(kernel);
    cv::filter2D(grayImage, dst, grayImage.depth(), kernel);
#endif
	cv::imshow("Mean Filter", dst);
}

// 回調函數，用於高斯濾波
void gaussian_filter_trackbar_callback(int position, void*) {
	int size = cv::getTrackbarPos("Size", "Gaussian Filter");
	if (size % 2 == 0)
		size++;
	int sigma = cv::getTrackbarPos("Sigma", "Gaussian Filter");
	cv::Mat dst;
#if USE_OPENCV
	// 使用OpenCV函數執行高斯濾波
	cv::GaussianBlur(grayImage, dst, cv::Size(size, size), sigma, sigma);
#else
	// 使用自訂的高斯核進行摺積
	cv::Mat kernel_x = cv::getGaussianKernel(size, sigma, CV_32F);
	cv::Mat kernel_y = cv::getGaussianKernel(size, sigma, CV_32F);
	cv::transpose(kernel_x, kernel_x);
	cv::Mat kernel = kernel_y * kernel_x;
    cv::filter2D(grayImage, dst, grayImage.depth(), kernel);
#endif

	cv::imshow("Gaussian Filter", dst);
}

// 回調函數，用於中值濾波
void median_filter_trackbar_callback(int position, void*) {
	int size = cv::getTrackbarPos("Size", "Median Filter");
	if (size % 2 == 0)
		size++;
	cv::Mat dst;
	cv::medianBlur(grayImage, dst, size);
	cv::imshow("Median Filter", dst);
}

// 回調函數，用於雙邊濾波
void bilateral_filter_trackbar_callback(int position, void*) {
	int sigmaColor = cv::getTrackbarPos("SigmaColor", "Bilateral Filter");
	int sigmaSpace = cv::getTrackbarPos("SigmaSpace", "Bilateral Filter");
	cv::Mat dst;
	cv::bilateralFilter(grayImage, dst, 9, sigmaColor, sigmaSpace);
	cv::imshow("Bilateral Filter", dst);
}

int main() {
	grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_GRAYSCALE);
	cv::imshow("original", grayImage);

	cv::namedWindow("Mean Filter", cv::WINDOW_NORMAL);
	cv::resizeWindow("Mean Filter", cv::Size(412, 500));
	cv::createTrackbar("Size", "Mean Filter", NULL, 255, mean_filter_trackbar_callback);

	cv::namedWindow("Gaussian Filter", cv::WINDOW_NORMAL);
	cv::resizeWindow("Gaussian Filter", cv::Size(412, 500));
	cv::createTrackbar("Size", "Gaussian Filter", NULL, 255, gaussian_filter_trackbar_callback);
	cv::createTrackbar("Sigma", "Gaussian Filter", NULL, 255, gaussian_filter_trackbar_callback);

	cv::namedWindow("Median Filter", cv::WINDOW_NORMAL);
	cv::resizeWindow("Median Filter", cv::Size(412, 500));
	cv::createTrackbar("Size", "Median Filter", NULL, 255, median_filter_trackbar_callback);

	cv::namedWindow("Bilateral Filter", cv::WINDOW_NORMAL);
	cv::resizeWindow("Bilateral Filter", cv::Size(412, 500));
	cv::createTrackbar("SigmaColor", "Bilateral Filter", NULL, 255, bilateral_filter_trackbar_callback);
	cv::createTrackbar("SigmaSpace", "Bilateral Filter", NULL, 255, bilateral_filter_trackbar_callback);

	cv::waitKey(0);
	return 0;
}

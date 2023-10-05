/*
【Day19】使用OpenCV進行形態學運算(Morphology) 

https://ithelp.ithome.com.tw/articles/10331195
*/

#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/core/utils/logger.hpp"

using namespace std;

cv::Mat binary_image;

void onErode(int kernel_size, void*) {
	if (kernel_size % 2 == 0)
		kernel_size++;

	cv::Mat dst;
	cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(kernel_size,kernel_size));
	cv::erode(binary_image,dst,kernel);
	cv::imshow("Erode", dst);
}

void onDilate(int kernel_size, void*) {
	if (kernel_size % 2 == 0)
		kernel_size++;

	cv::Mat dst;
	cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(kernel_size,kernel_size));
	cv::dilate(binary_image,dst,kernel);
	cv::imshow("Dilate", dst);
	
}

void onOpening(int kernel_size, void*) {
	if (kernel_size % 2 == 0)
		kernel_size++;

	cv::Mat dst;
	cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(kernel_size,kernel_size));

	cv::erode(binary_image,dst,kernel);
	cv::dilate(dst,dst,kernel);
	cv::imshow("Opening", dst);
	
}
void onClosing(int kernel_size, void*) {
	if (kernel_size % 2 == 0)
		kernel_size++;

	cv::Mat dst;
	cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(kernel_size,kernel_size));

	cv::dilate(binary_image,dst,kernel);
	cv::erode(dst,dst,kernel);
	cv::imshow("Closing", dst);

}

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);
	cv::Mat image = cv::imread("/home/philphoenix/infinicloud/OpenCV/62_hello-world.jpg",cv::IMREAD_GRAYSCALE);
	cv::threshold(255- image, binary_image, 0, 255, cv::THRESH_OTSU);


	cv::namedWindow("Original", cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Original",cv::Size(512*(float)image.cols/image.rows,512));
	cv::imshow("Original",binary_image);

	cv::namedWindow("Dilate", cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Dilate",cv::Size(512*(float)image.cols/image.rows,512));

	cv::imshow("Dilate",binary_image);
	cv::createTrackbar("Kernel Size", "Dilate", NULL, 100,onDilate);

	cv::namedWindow("Erode", cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Erode",cv::Size(512*(float)image.cols/image.rows,512));
	cv::imshow("Erode",binary_image);
	cv::createTrackbar("Kernel Size", "Erode", NULL, 100,onErode);

	cv::namedWindow("Opening", cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Opening",cv::Size(512*(float)image.cols/image.rows,512));
	cv::imshow("Opening",binary_image);
	cv::createTrackbar("Kernel Size", "Opening", NULL, 100,onOpening);


	cv::namedWindow("Closing", cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Closing",cv::Size(512*(float)image.cols/image.rows,512));
	cv::imshow("Closing",binary_image);
	cv::createTrackbar("Kernel Size", "Closing", NULL, 100,onClosing);


	cv::waitKey(0);
	return 0;
}

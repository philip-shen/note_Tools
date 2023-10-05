/*
【Day18】​OpenCV HSV色彩空間轉換：手掌前景提取 

https://ithelp.ithome.com.tw/articles/10327115
*/

#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/core/utils/logger.hpp"
#define USE_OPENCV 0
using namespace std;

//cv::Mat bgr2hsv(cv::Mat original);
cv::Mat hsv_image;
cv::Mat image;
int h_range;
int s_range;
int v_range;

void onClick(int event, int x, int y, int flags, void* param)
{
    if (event & cv::EVENT_LBUTTONDOWN)
    {
		cv::Vec3b vec = hsv_image.at<cv::Vec3b>(y, x);
		uint8_t h = vec[0];
		uint8_t s = vec[1];
		uint8_t v = vec[2];
		printf("f(%d,%d) = [%.2f* %.2f%% %.2f%%]\n", x,y,360.0 * (vec[0] / 255.0),100*vec[1]/255.0,100*vec[2]/255.0);
		cv::Mat mask,dst;
		
		uint8_t h_norm = 255.0 * (h_range / 100.0);
		uint8_t s_norm = 255.0 * (s_range / 100.0);
		uint8_t v_norm = 255.0 * (v_range / 100.0);

		cv::inRange(hsv_image,
			cv::Scalar(max(h-h_norm,0),max(s-s_norm,0),max(v-v_norm,0)),
			cv::Scalar(min(h+h_norm,255),min(s+s_norm,255),min(v+v_norm,255)),
			mask);
		cv::imshow("Mask",mask);
		cv::bitwise_and(image,image, dst, mask);
		cv::imshow("Output",dst);
    }
}

cv::Mat bgr2hsv(cv::Mat original) {
	cv::Mat hsv_img=cv::Mat::zeros(cv::Size(original.cols,original.rows),CV_8UC3);
	for (int y = 0;y < hsv_img.rows;y++) {
		for (int x = 0;x < hsv_img.cols;x++) {
			cv::Vec3b vec = original.at<cv::Vec3b>(y, x);
			float b = vec[0]/255.0f;
			float g = vec[1]/255.0f;
			float r = vec[2]/255.0f;
			float max = std::max(std::max(b, g),r);
			float min = std::min(std::min(b, g),r);

			float h;
			if (max == min)
				h = 0;
			else if (max == r && g >= b)
				h = 60.0f * (g - b) / (max - min);
			else if (max == r && g < b)
				h = 60.0f * (g - b) / (max - min) + 360.0f;
			else if (max == g)
				h = 60.0f * (b - r) / (max - min) + 120.0f;
			else if (max == b)
				h = 60.0f * (r-g) / (max - min) + 240.0f;
			h-= 360. * std::floor(h* (1. / 360.));

			float s;
			if (max == 0)
				s = 0.0f;
			else
				s = 1.0f - (float)min / max;
			
			float v = max;

			hsv_img.at<cv::Vec3b>(y,x)[0]=(uint8_t) 255.0f*(h/360.0f);
			hsv_img.at<cv::Vec3b>(y,x)[1]=(uint8_t) 255.0f*s;
			hsv_img.at<cv::Vec3b>(y,x)[2]=(uint8_t) 255.0f*v;
		}
	}
	return hsv_img;
}

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);
	image = cv::imread("/home/philphoenix/infinicloud/OpenCV/61_palm.jpg",cv::IMREAD_COLOR);

#if USE_OPENCV
	cv::cvtColor(image, hsv_image, cv::COLOR_BGR2HSV);
#else
	hsv_image = bgr2hsv(image);
#endif // USE_OPENCV

	cv::namedWindow("Original",cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Original", cv::Size(512.0 * ((float)image.cols / image.rows), 512));

	cv::namedWindow("Output",cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Output", cv::Size(512.0 * ((float)image.cols / image.rows), 512));

	cv::namedWindow("Mask",cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Mask", cv::Size(512.0 * ((float)image.cols / image.rows), 512));

	cv::imshow("Original",image);
	cv::setMouseCallback("Original", onClick);
	cv::createTrackbar("H Range", "Original", &h_range, 100,NULL);
	cv::createTrackbar("S Range", "Original", &s_range, 100,NULL);
	cv::createTrackbar("V Range", "Original", &v_range, 100,NULL);

	cv::setTrackbarPos("H Range", "Original",5);
	cv::setTrackbarPos("S Range", "Original", 49);
	cv::setTrackbarPos("V Range", "Original", 100);
	cv::waitKey(0);
	return 0;
}
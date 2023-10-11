/*
Day27】使用OpenCV進行霍夫圓轉換(Hough Circle Transform)
https://ithelp.ithome.com.tw/articles/10329090
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

void on_circle_change(int position, void*);
int min_r;
// 存儲灰階影像的變數
cv::Mat grayImage; 
vector<cv::Vec2f> lines;

int main()
{
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT); 
	grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/67_hough_line_68_hough_circle_transform.jpg", 
							cv::IMREAD_GRAYSCALE); // 讀取灰階影像

    cv::namedWindow("Circle", cv::WindowFlags::WINDOW_NORMAL); // 建立一個視窗用於顯示圓檢測結果
    cv::resizeWindow("Circle", 512.0f * ((float)grayImage.cols / grayImage.rows), 512);

	cv::createTrackbar("Min R", "Circle", &min_r, 100, on_circle_change); // 建立一個滑動條用於調整最小半徑
	cv::waitKey(0); 
	return 0;
}

// 當滑動條"Min R"的值發生變化時調用的函數
void on_circle_change(int position, void*) {
	if (min_r == 0)
		return;
	cv::Mat output;
	cv::cvtColor(grayImage, output, cv::COLOR_GRAY2BGR);

	vector<cv::Vec3f> circles;
	cv::HoughCircles(grayImage, circles, cv::HOUGH_GRADIENT, 1, 200, 100, 30,min_r); // 使用霍夫轉換來檢測圓

	 for( size_t i = 0; i < circles.size(); i++ )
	 {
		 cv::Vec3i c = circles[i];
		 cv::Point center = cv::Point(c[0], c[1]);
		 cv::circle( output, center,5, cv::Scalar(0,0,255),-1, cv::LINE_AA);
		 int radius = c[2];
		 cv::circle(output, center, radius, cv::Scalar(255, 0, 255), 3, cv::LINE_AA);
	 }
	cv::imshow("Circle", output);
}
/*
【Day26】使用OpenCV進行霍夫線轉換(Hough Line Transform)
2023-10-07 01:33:46

https://ithelp.ithome.com.tw/articles/10329089
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

void on_line_index_change(int position, void*);
// 存儲灰度影像的變數
cv::Mat grayImage; 
vector<cv::Vec2f> lines;

// 當滑動條"Index"的值發生變化時調用的函數
void on_line_index_change(int position, void*) {
	cv::Mat output;
	cv::cvtColor(grayImage, output, cv::COLOR_GRAY2BGR);

	float rho = lines[position][0];
	float theta = lines[position][1];
	cv::Point pt1, pt2;

	//(r,theta)轉到X-Y平面的點(xi,yi)
	double x0 = rho * cos(theta);
	double y0 = rho * sin(theta);

	pt1.x = cvRound(x0 + 1000 * (-sin(theta)));
	pt1.y = cvRound(y0 + 1000 * (cos(theta)));
	pt2.x = cvRound(x0 - 1000 * (-sin(theta)));
	pt2.y = cvRound(y0 - 1000 * (cos(theta)));
	cv::line(output, pt1, pt2, cv::Scalar(0, 0, 255), 1, cv::LINE_AA);
	printf("index:%d\tr:%.2f\ttheta:%.2f\tx0:%.2f\ty0:%.2f\n", position, rho, 180 * theta / CV_PI, x0, y0);
	cv::imshow("Line", output);
}

int main()
{
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT); 
	grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/67_hough_line_transform3.jpg", cv::IMREAD_GRAYSCALE); // 讀取灰度圖像

    cv::namedWindow("Line", cv::WindowFlags::WINDOW_NORMAL); // 建立一個視窗用於顯示線的詳細信息
    cv::resizeWindow("Line", 512.0f * ((float)grayImage.cols / grayImage.rows), 512);

	cv::Mat edge_image;
	cv::Canny(grayImage, edge_image, 28, 16); // 使用Canny邊緣檢測

	cv::HoughLines(edge_image, lines, 1, CV_PI / 180, 150); // 應用霍夫變換來檢測線段
	cv::createTrackbar("Index", "Line", NULL, 0, on_line_index_change); // 建立一個滑動條用於選擇線的索引
	cv::setTrackbarMax("Index", "Line", lines.size() - 1); // 設定滑動條的最大值
	cv::waitKey(0); 

	return 0;
}

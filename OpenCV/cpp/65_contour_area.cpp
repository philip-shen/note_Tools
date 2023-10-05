/*
【Day23】使用OpenCV進行輪廓的幾何運算 
2023-10-04 00:19:34
https://ithelp.ithome.com.tw/articles/10329083
*/

#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/core/utils/logger.hpp"

using namespace std;

vector<vector<cv::Point>> contours;
void onClick(int event, int x, int y, int flags, void* param)
{
    if (event & cv::EVENT_LBUTTONDOWN)
    {
		for (int i = 0;i < contours.size();i++) {
			double dist = cv::pointPolygonTest(contours[i],cv::Point2f(x,y),false);
			if (dist == 0.0) {
				printf("f(%d,%d)在輪廓%d邊緣上\n",x,y,i);
			}
			else if(dist == -1.0){
				printf("f(%d,%d)在輪廓%d外\n",x,y,i);
			}
			else if (dist == 1.0) {
				printf("f(%d,%d)在輪廓%d內\n",x,y,i);
			}
		}

		printf("--------------------\n");
    }
}

int main()
{
	
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);
	cv::Mat image = cv::imread("/home/philphoenix/infinicloud/OpenCV/65_contour_area.jpg",cv::IMREAD_GRAYSCALE);

	cv::namedWindow("Output",cv::WindowFlags::WINDOW_NORMAL);
	cv::resizeWindow("Output", cv::Size(512.0 * ((float)image.cols / image.rows), 512));
	cv::setMouseCallback("Output", onClick);

	cv::Mat dst;
	cv::threshold(image, dst,0,255,cv::THRESH_OTSU);
	cv::findContours(dst, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);
	cv::Mat output=cv::Mat::zeros(cv::Size(image.cols,image.rows),CV_8UC3);
	cv::drawContours(output, contours, -1, cv::Scalar(0, 255, 0));
	for (int i = 0;i < contours.size();i++) {
		vector<cv::Point> convex_hull_contours;
		cv::convexHull(contours[i], convex_hull_contours);

		cv::Rect bounding_rect=cv::boundingRect(contours[i]);
		cv::RotatedRect min_area_rect = cv::minAreaRect(contours[i]);

		cv::Point2f center;
		float radius;
		cv::minEnclosingCircle(contours[i],center,radius);
		cv::circle(output, center,radius,cv::Scalar(0, 255, 255));

		cv::polylines(output, convex_hull_contours, true, cv::Scalar(0, 0, 255));
		cv::rectangle(output, bounding_rect, cv::Scalar(255, 0, 0));
		cv::putText(output, to_string(i), cv::Point(bounding_rect.x, bounding_rect.y - 5),cv::FONT_HERSHEY_COMPLEX,0.5,cv::Scalar(0,255,0));
		
		printf("%d -> angle:%.2f\n", i, min_area_rect.angle);
	}
	cv::imshow("Output",output);
	cv::imwrite("65_contour_area.jpg", output);
	cv::waitKey(0);
	return 0;
}
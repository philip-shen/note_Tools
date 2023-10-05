/*
【Day22】OpenCV 邊緣檢測後處理：尋找輪廓 

https://ithelp.ithome.com.tw/articles/10329079
*/

#include <iostream> 
#include <vector> 
#include <opencv2/opencv.hpp> 
#include "opencv2/core/utils/logger.hpp"
using namespace std;

int main()
{
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);
	cv::Mat grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/64_contour2.jpg",cv::IMREAD_GRAYSCALE);
	
	cv::namedWindow("Original", cv::WINDOW_NORMAL);
	cv::resizeWindow("Original", cv::Size( 512*((float)grayImage.cols)/grayImage.rows, 512));
	cv::imshow("Original",grayImage);

	cv::namedWindow("Output", cv::WINDOW_NORMAL);
	cv::resizeWindow("Output", cv::Size(512*((float)grayImage.cols)/grayImage.rows, 512));

	cv::Mat binary_img;
	cv::threshold(grayImage, binary_img, 0, 255, cv::THRESH_OTSU);
	
	vector<vector<cv::Point>> contours;
	vector<cv::Vec4i> hierarchy;
	cv::findContours(binary_img, contours, hierarchy,
					cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE);

	printf("counters found:%d\n",(int)contours.size());
	printf("\n");
	
	cv::Mat output_img=cv::Mat::zeros(cv::Size(binary_img.cols,binary_img.rows),CV_8UC3);

	
	for (int i = 0;i < hierarchy.size();i++) {
		cv::Vec4i vec=hierarchy[i];
		cv::Mat v;
		cv::transpose(vec, v);
		printf("%d ->",i);
		print(v);
		printf(" points:%d\n",(int)contours[i].size());

		cv::Rect rect=cv::boundingRect(contours.at(i));
		cv::rectangle(output_img, rect, cv::Scalar(0,255,0),1);
		cv::putText(output_img, std::to_string(i),
					cv::Point(rect.x, rect.y-10), cv::FONT_HERSHEY_COMPLEX, 
					0.4, cv::Scalar(0, 255,0),1);
		cv::drawContours(output_img, contours,i, 
						cv::Scalar(0,0,255), 1,cv::LINE_AA);
	}

	cv::imshow("Output",output_img);
	cv::imwrite("output.jpg", output_img);
	cv::waitKey(0);
	return 0;
}
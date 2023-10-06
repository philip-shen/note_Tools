/*
【Day24】使用OpenCV求出輪廓矩(Moments) 

https://ithelp.ithome.com.tw/articles/10329086
*/

#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/core/utils/logger.hpp"
using namespace std;

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);
	cv::Mat image = cv::imread("/home/philphoenix/infinicloud/OpenCV/img_Hu-moments.jpg",cv::IMREAD_GRAYSCALE);
	cv::Mat binary;
	cv::threshold(image, binary, 0, 255, cv::THRESH_OTSU);//二值化影像

	cv::Mat contours_image=cv::Mat::zeros(cv::Size(binary.cols,binary.rows),CV_8UC3);//空白影像輪廓和
	cv::Mat moments_image=cv::Mat::zeros(cv::Size(binary.cols,binary.rows),CV_8UC3);//空白輪廓的重心
	vector<vector<cv::Point>> contours;
	cv::findContours(binary, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_TC89_KCOS);//使用cv::findContours函式找到了影像中的外部輪廓，這些輪廓存儲在contours向量中
	/*
        使用for迴圈遍歷所有找到的輪廓。        
        對於每個輪廓，計算其包圍矩形、標記輪廓索引號、繪製輪廓以及計算輪廓的Hu不變矩。
        輪廓索引號和Hu不變矩的信息被輸出到控制台上。
    */
    for (int i = 0;i < contours.size();i++) {
		cv::Rect bounding_rect=cv::boundingRect(contours[i]);
		cv::putText(contours_image, to_string(i), cv::Point(bounding_rect.x, bounding_rect.y - 5),
                    cv::FONT_HERSHEY_COMPLEX,0.5,cv::Scalar(0,255,0));
		cv::drawContours(contours_image, contours, i, cv::Scalar(0,255,0));


		cv::Moments moments=cv::moments(contours[i]);
		cv::Point center=cv::Point(moments.m10/moments.m00, moments.m01/moments.m00);
		cv::circle(contours_image, center, 3, cv::Scalar(0, 255, 255), -1);

		double hu[7];
		cv::HuMoments(moments,hu);
		printf("|%d|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f|%.2f|\n",i,hu[0],hu[1],hu[2],hu[3],hu[4],hu[5],hu[6]);
	}
	
    cv::imshow("Contours",contours_image);
	cv::waitKey(0);
	return 0;
}   
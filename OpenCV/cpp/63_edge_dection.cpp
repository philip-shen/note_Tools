/*
【Day21】使用OpenCV進行邊緣檢測 

https://ithelp.ithome.com.tw/articles/10329071
*/
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

cv::Mat sobel(cv::Mat origin,int threshold);
cv::Mat roberts(cv::Mat origin,int threshold);
cv::Mat scharr(cv::Mat origin,int threshold);
cv::Mat prewitt(cv::Mat origin,int threshold);
cv::Mat laplacian(cv::Mat origin,int threshold);
cv::Mat grayImage;
 
void onSobel(int threshold, void*) {
	cv::Mat dst = sobel(grayImage,threshold);
	cv::imshow("Sobel", dst);
}

void onRoberts(int threshold, void*) {
	cv::Mat dst = roberts(grayImage,threshold);
	cv::imshow("Roberts", dst);
}
void onScharr(int threshold, void*) {
	cv::Mat dst = scharr(grayImage,threshold);
	cv::imshow("Scharr", dst);
}
void onPrewitt(int threshold, void*) {
	cv::Mat dst = prewitt(grayImage,threshold);
	cv::imshow("Prewitt", dst);

}
void onLaplacian(int threshold, void*) {
	cv::Mat dst = laplacian(grayImage,threshold);
	cv::imshow("Laplacian", dst);
}


cv::Mat sobel(cv::Mat origin,int threshold) {
	cv::Mat sobel_dst_x;
	cv::Mat sobel_dst_y;
	cv::Mat sobel_dst;

	float kernel_data_x[9] = {-1,0,1,-2,0,2,-1,0,1};
	float kernel_data_y[9] = {-1,-2,-1,0,0,0,1,2,1};

	cv::Mat kernel_x = cv::Mat(3,3, CV_32F, kernel_data_x);
	cv::Mat kernel_y = cv::Mat(3,3, CV_32F,kernel_data_y);

	cv::filter2D(origin,sobel_dst_x,CV_32F,kernel_x);
	cv::convertScaleAbs(sobel_dst_x,sobel_dst_x);
	cv::filter2D(origin,sobel_dst_y,CV_32F,kernel_y);
	cv::convertScaleAbs(sobel_dst_y,sobel_dst_y);
	cv::addWeighted(sobel_dst_x, 0.5, sobel_dst_y, 0.5, 0, sobel_dst);
	
	cv::normalize(sobel_dst, sobel_dst,0, 255, cv::NormTypes::NORM_MINMAX);
	cv::Mat dst;
	cv::threshold(sobel_dst, dst, threshold, 255, cv::THRESH_BINARY);
	return dst;
}

cv::Mat roberts(cv::Mat origin,int threshold) {
	cv::Mat roberts_dst_x;
	cv::Mat roberts_dst_y;
	cv::Mat roberts_dst;

	float kernel_data_x[4] = {1,0,0,-1};
	float kernel_data_y[4] = {0,1,-1,0};
	cv::Mat kernel_x = cv::Mat(2,2, CV_32F, kernel_data_x);
	cv::Mat kernel_y = cv::Mat(2,2, CV_32F,kernel_data_y);

	cv::filter2D(origin,roberts_dst_x,CV_32F,kernel_x);
	cv::convertScaleAbs(roberts_dst_x,roberts_dst_x);

	cv::filter2D(origin,roberts_dst_y,CV_32F,kernel_y);
	cv::convertScaleAbs(roberts_dst_y,roberts_dst_y);

	cv::addWeighted(roberts_dst_x, 0.5, roberts_dst_y, 0.5, 0, roberts_dst);

	cv::normalize(roberts_dst_x, roberts_dst_x,0, 255, cv::NormTypes::NORM_MINMAX);
	cv::Mat dst;
	cv::threshold(roberts_dst, dst, threshold, 255, cv::THRESH_BINARY);
	return dst;
}

cv::Mat scharr(cv::Mat origin,int threshold) {
	cv::Mat scharr_dst_x;
	cv::Mat scharr_dst_y;
	cv::Mat scharr_dst;

	float kernel_data_x[9] = {-3,0,3,-10,0,10,-3,0,3};
	float kernel_data_y[9] = {-3,-10,-3,0,0,0,3,10,3};
	cv::Mat kernel_x = cv::Mat(3,3, CV_32F, kernel_data_x);
	cv::Mat kernel_y = cv::Mat(3,3, CV_32F,kernel_data_y);

	cv::filter2D(origin,scharr_dst_x,CV_32F,kernel_x);
	cv::convertScaleAbs(scharr_dst_x,scharr_dst_x);

	cv::filter2D(origin,scharr_dst_y,CV_32F,kernel_y);
	cv::convertScaleAbs(scharr_dst_y,scharr_dst_y);

	cv::addWeighted(scharr_dst_x, 0.5, scharr_dst_y, 0.5, 0, scharr_dst);

	cv::normalize(scharr_dst, scharr_dst,0, 255, cv::NormTypes::NORM_MINMAX);

	cv::Mat dst;
	cv::threshold(scharr_dst, dst, threshold, 255, cv::THRESH_BINARY);
	return dst;

}

cv::Mat prewitt(cv::Mat origin,int threshold) {
	cv::Mat prewitt_dst_x;
	cv::Mat prewitt_dst_y;
	cv::Mat prewitt_dst;

	float kernel_data_x[9] = {-1,0,1,-1,0,1,-1,0,1};
	float kernel_data_y[9] = {1,1,1,0,0,0,-1,-1,-1};
	cv::Mat kernel_x = cv::Mat(3,3, CV_32F, kernel_data_x);
	cv::Mat kernel_y = cv::Mat(3,3, CV_32F,kernel_data_y);

	cv::filter2D(origin,prewitt_dst_x,CV_32F,kernel_x);
	cv::convertScaleAbs(prewitt_dst_x,prewitt_dst_x);

	cv::filter2D(origin,prewitt_dst_y,CV_32F,kernel_y);
	cv::convertScaleAbs(prewitt_dst_y,prewitt_dst_y);

	cv::addWeighted(prewitt_dst_x, 0.5, prewitt_dst_y, 0.5, 0, prewitt_dst);

	cv::normalize(prewitt_dst, prewitt_dst,0, 255, cv::NormTypes::NORM_MINMAX);

	cv::Mat dst;
	cv::threshold(prewitt_dst, dst, threshold, 255, cv::THRESH_BINARY);
	return dst;

}

cv::Mat laplacian(cv::Mat origin,int threshold) {
	cv::Mat laplacian_dst;

	float kernel_data[9] = {0,-1,0,-1,4,-1,0,-1,0};
	cv::Mat kernel = cv::Mat(3,3, CV_32F, kernel_data);

	cv::filter2D(origin,laplacian_dst,CV_32F,kernel);
	cv::convertScaleAbs(laplacian_dst,laplacian_dst);

	cv::normalize(laplacian_dst, laplacian_dst,0, 255, cv::NormTypes::NORM_MINMAX);
	cv::Mat dst;
	cv::threshold(laplacian_dst, dst, threshold, 255, cv::THRESH_BINARY);
	return dst;

}

int main()
{
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);

	grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/63_puzzle.jpg",cv::IMREAD_GRAYSCALE);


	cv::namedWindow("Origin", cv::WINDOW_NORMAL);
	cv::resizeWindow("Origin", cv::Size(512,512*grayImage.rows/(float)grayImage.cols));

	cv::namedWindow("Sobel", cv::WINDOW_NORMAL);
	cv::resizeWindow("Sobel", cv::Size(512,512*grayImage.rows/(float)grayImage.cols));
	cv::createTrackbar("Threshold","Sobel", NULL, 255, onSobel);

	cv::namedWindow("Roberts", cv::WINDOW_NORMAL);
	cv::resizeWindow("Roberts", cv::Size(512,512*grayImage.rows/(float)grayImage.cols));
	cv::createTrackbar("Threshold","Roberts", NULL, 255,onRoberts);


	cv::namedWindow("Scharr", cv::WINDOW_NORMAL);
	cv::resizeWindow("Scharr", cv::Size(512,512*grayImage.rows/(float)grayImage.cols));
	cv::createTrackbar("Threshold","Scharr", NULL, 255,onScharr);

	cv::namedWindow("Prewitt", cv::WINDOW_NORMAL);
	cv::resizeWindow("Prewitt", cv::Size(512,512*grayImage.rows/(float)grayImage.cols));
	cv::createTrackbar("Threshold","Prewitt", NULL, 255,onPrewitt);

	cv::namedWindow("Laplacian", cv::WINDOW_NORMAL);
	cv::resizeWindow("Laplacian", cv::Size(512,512*grayImage.rows/(float)grayImage.cols));
	cv::createTrackbar("Threshold","Laplacian", NULL, 255,onLaplacian);
	cv::imshow("Origin", grayImage);

	cv::waitKey(0);
	return 0;
}
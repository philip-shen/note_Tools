/*
 【Day30】使用CUDA加速OpenCV
2023-10-11 00:31:05

https://ithelp.ithome.com.tw/articles/10329093
*/

#include <iostream>
#include <chrono>
#include "opencv2/opencv.hpp"
#include "opencv2/cudaarithm.hpp"
#include "opencv2/cudafilters.hpp"
#include "opencv2/cudaimgproc.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;
cv::Mat img;
cv::cuda::GpuMat gpu_img;

void threshold_test() {
	auto t1 = std::chrono::high_resolution_clock::now();
	cv::Mat dst;
	cv::threshold(img,dst,128,255,cv::THRESH_BINARY);
	cv::imshow("CPU Threshold", dst);
	auto t2 = std::chrono::high_resolution_clock::now();
	auto int_us = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1);
	printf("CPU Threshold:%dus\n",int_us);


	auto t3 = std::chrono::high_resolution_clock::now();
	cv::cuda::GpuMat gpu_dst;
	cv::cuda::threshold(gpu_img,gpu_dst,128,255,cv::THRESH_BINARY);
	gpu_dst.download(dst);
	cv::imshow("GPU Threshold", dst);
	auto t4 = std::chrono::high_resolution_clock::now();
	auto int_us2 = std::chrono::duration_cast<std::chrono::microseconds>(t4 - t3);
	printf("GPU Threshold:%dus\n",int_us2);
	printf("-----------------\n");
}
void filter_test() {

	auto t1 = std::chrono::high_resolution_clock::now();
	cv::Mat dst;
	cv::GaussianBlur(img, dst, cv::Size(3, 3), 1.2, 1.2);
	cv::imshow("CPU Gaussian", dst);
	auto t2 = std::chrono::high_resolution_clock::now();
	auto int_us = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1);
	printf("CPU Gaussian:%dus\n",int_us);


	auto t3 = std::chrono::high_resolution_clock::now();
	cv::cuda::GpuMat gpu_dst;
	cv::Ptr<cv::cuda::Filter> filter=cv::cuda::createGaussianFilter(CV_8UC3, CV_8UC3, cv::Size(3, 3), 1.2, 1.2);
	filter.get()->apply(gpu_img, gpu_dst);
	gpu_dst.download(dst);
	cv::imshow("GPU Gaussian", dst);
	auto t4 = std::chrono::high_resolution_clock::now();
	auto int_us2 = std::chrono::duration_cast<std::chrono::microseconds>(t4 - t3);
	printf("GPU Gaussian:%dus\n",int_us2);
	printf("-----------------\n");

}

void color_conversion_test() {
	auto t1 = std::chrono::high_resolution_clock::now();
	cv::Mat dst;
	cv::cvtColor(img, dst, cv::COLOR_BGR2HSV);
	cv::imshow("CPU Color Convert", dst);
	auto t2 = std::chrono::high_resolution_clock::now();
	auto int_us = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1);
	printf("CPU Color Convert:%dus\n",int_us);


	auto t3 = std::chrono::high_resolution_clock::now();
	cv::cuda::GpuMat gpu_dst;
	cv::cuda::cvtColor(gpu_img, gpu_dst, cv::COLOR_BGR2HSV);
	gpu_dst.download(dst);
	cv::imshow("GPU Color Convert", dst);
	auto t4 = std::chrono::high_resolution_clock::now();
	auto int_us2 = std::chrono::duration_cast<std::chrono::microseconds>(t4 - t3);
	printf("GPU Color Convert:%dus\n",int_us2);
	printf("-----------------\n");
	
}

int main()
{
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT); 
	img= cv::imread("C:\\Users\\vince\\Downloads\\Lenna.png", cv::IMREAD_COLOR);
	gpu_img.upload(img);
	threshold_test();
	filter_test();
	color_conversion_test();
	
	cv::waitKey(0);
	return 0;
}
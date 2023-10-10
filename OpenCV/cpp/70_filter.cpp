/*
 【Day29】​OpenCV實踐頻率濾波器：提高影像處理效率
2023-10-10 00:01:47
https://ithelp.ithome.com.tw/articles/10333423
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include <chrono>
#include "opencv2/core/utils/logger.hpp"
#define FILTER_MEAM 0
#define FILTER_GAUSSIAN 1
#define FILTER FILTER_MEAM

using namespace std;
cv::Mat kernel;
cv::Mat dft_kernel;
int dft_rows;
int dft_cols;

cv::Mat convolute_on_frequency_domain(cv::Mat image){
    cv::Mat dft_image = cv::Mat::zeros(dft_rows,dft_cols,CV_32F);
    cv::Mat dft_image_part = dft_image(cv::Rect(0, 0, image.cols, image.rows));
    
    image.convertTo(dft_image_part, dft_image_part.type(), 1,-cv::mean(image)[0]);

    cv::dft(dft_image, dft_image,0,image.rows);

    cv::mulSpectrums(dft_image, dft_kernel, dft_image, 0, true);
    cv::idft(dft_image, dft_image, cv::DFT_SCALE, image.rows + kernel.rows - 1);
    cv::Mat corr = dft_image(cv::Rect(0, 0, image.cols + kernel.cols - 1, image.rows + kernel.rows - 1));
    return corr;
}

void init_kernel(cv::Size image_size,cv::Mat kernel) {
    dft_rows = cv::getOptimalDFTSize(image_size.height + kernel.rows - 1);
    dft_cols = cv::getOptimalDFTSize(image_size.width  + kernel.cols - 1);
	dft_kernel = cv::Mat::zeros(dft_rows,dft_cols,CV_32F);
    cv::Mat dft_kernel_part = dft_kernel(cv::Rect(0, 0, kernel.cols, kernel.rows));
    kernel.convertTo(dft_kernel_part, dft_kernel_part.type(), 1, 0);
    cv::dft(dft_kernel, dft_kernel,0, kernel.rows);
}
int main() {
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT);

    // 讀取灰度影像
    cv::Mat image = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_GRAYSCALE);

    cv::Mat kernel;
#if FILTER==FILTER_MEAM 
    kernel = cv::Mat::ones(cv::Size(21, 21), CV_32FC1);
    kernel /= kernel.rows*kernel.cols;
    printf("Filter: FILTER_MEAM\n");
#endif

#if FILTER==FILTER_GAUSSIAN
    cv::Mat x_kernel=cv::getGaussianKernel(21, 4);
    cv::Mat y_kernel=cv::getGaussianKernel(21, 4);
    cv::transpose(y_kernel, y_kernel);
    kernel = x_kernel * y_kernel;
    printf("Filter: FILTER_GAUSSIAN\n");
#endif

    init_kernel(image.size(),kernel);

	auto t1 = std::chrono::high_resolution_clock::now();

    cv::Mat dft_result=convolute_on_frequency_domain(image);

	auto t2 = std::chrono::high_resolution_clock::now();
	auto int_us = std::chrono::duration_cast<std::chrono::microseconds>(t2 - t1);
    cv::normalize(dft_result,dft_result, 0, 1, cv::NORM_MINMAX);
    printf("Time cost(DFT):%dus\n", int_us);

    cv::Mat space_result;

	auto t3 = std::chrono::high_resolution_clock::now();
    cv::filter2D(image,space_result, CV_8U, kernel);
	auto t4 = std::chrono::high_resolution_clock::now();

	auto int_us2 = std::chrono::duration_cast<std::chrono::microseconds>(t4 - t3);

    printf("Time cost(Space):%dus\n", int_us2);
    
    cv::imshow("Image", image);
    cv::imshow("DFT Output",dft_result);
    cv::imshow("Space Output",space_result);
    
    cv::waitKey(0);
    return 0;
}
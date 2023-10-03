/*【Day10】OpenCV 直方圖均衡化：增強影像對比度 

https://ithelp.ithome.com.tw/articles/10323301
*/

#include <iostream>
#include "math.h"
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

#define USE_OPENCV 0
using namespace std;

void showHistogramWindow(const char* windowName, cv::Mat hist) {
	int hist_w = 720, hist_h = 512;
	int bin_w = cvRound( (double) hist_w/hist.rows);
	cv::Mat histImage=cv::Mat::zeros(hist_h, hist_w, CV_8UC1);
    cv::normalize(hist, hist, 0, histImage.rows, cv::NORM_MINMAX);
	for( int i = 1; i < hist.rows; i++ )
	{
		cv::line(histImage,
            cv::Point(bin_w*(i-1), hist_h -cvRound(hist.at<float>(i-1)) ),
			cv::Point(bin_w*(i), hist_h - cvRound(hist.at<float>(i)) ),
			cv::Scalar( 255, 255, 255));
	}
    cv::imshow(windowName, histImage);
}

cv::Mat calcHist(cv::Mat grayImage) {
	cv::Mat hist;
	int histSize = 256;
	float range[] = { 0, 256 };
	const float* histRange[] = { range };
	cv::calcHist(&grayImage, 1, 0, cv::Mat(), hist,1, &histSize, histRange, true, true);
    return hist;
}

int main()
{
    
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT);

	cv::Mat grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png",cv::IMREAD_GRAYSCALE);
    cv::Mat equalizedImage;
	cv::Mat original_hist;
	cv::Mat dst_hist;
#if USE_OPENCV
    original_hist = calcHist(grayImage);
    cv::equalizeHist(grayImage, equalizedImage);
#else
    equalizedImage = cv::Mat(grayImage.rows, grayImage.cols, grayImage.type());
    original_hist= cv::Mat::zeros(256,1,CV_32F);
    for (int y = 0;y < grayImage.rows;y++) {
		for (int x = 0;x < grayImage.cols;x++) {
            uchar level=grayImage.at<uchar>(y, x);
            original_hist.at<float>(level) += 1;
		}
    }

    float total_pixels = grayImage.rows * grayImage.cols;
    cv::Mat pmf = original_hist / total_pixels;
    cv::Mat cdf =cv::Mat::zeros(256,1,CV_32F);

    float cdf_min=0.0f;
    float cdf_max=1.0f;
    for (int i = 0;i < pmf.rows;i++){
        cdf.at<float>(i) = pmf.at<float>(i) + cdf.at<float>(max(i - 1, 0));
        if (cdf_min == 0.0f&&cdf.at<float>(i) > 0.0f) {
            cdf_min = cdf.at<float>(i);
        }
        if (cdf.at<float>(i) > cdf_max) {
            cdf_max = cdf.at<float>(i);
        }
    }
    int L = 256;
    for (int y = 0;y < grayImage.rows;y++) {
		for (int x = 0;x < grayImage.cols;x++) {
            uchar level=grayImage.at<uchar>(y, x);
            float cdf_y = cdf.at<float>(level);
            equalizedImage.at<uchar>(y, x) =((uchar)(L-1) * (cdf_y - cdf_min)/(cdf_max-cdf_min));
		}
    }
#endif

    showHistogramWindow("Original Histogram",original_hist);

	dst_hist = calcHist(equalizedImage);

    showHistogramWindow("Equalized Histogram",dst_hist);

    cv::namedWindow("Original Image", cv::WINDOW_AUTOSIZE);
    cv::imshow("Original Image", grayImage);

    cv::namedWindow("Equalized Image", cv::WINDOW_AUTOSIZE);
    cv::imshow("Equalized Image", equalizedImage);

    cv::waitKey(0);

	return 0;
}
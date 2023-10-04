/*
【Day16】​OpenCV 影像金字塔：不同尺度下的影像 

https://ithelp.ithome.com.tw/articles/10327108
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

int main()
{
	// 設置 OpenCV 的日誌級別為無日誌輸出
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT); 
	
	// 讀取一張灰階影像（以灰階模式讀取）
	cv::Mat grayImage = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_GRAYSCALE);
	
	// 定義一個 5x5 的高斯核
	float data[] = {
		1, 4, 6, 4, 1,
		4, 16, 24, 16, 4,
		6, 24, 36, 24, 6,
		4, 16, 24, 16, 4,
		1, 4, 6, 4, 1,
	};
	cv::Mat gaussian_kernel = cv::Mat(5, 5, CV_32FC1, data);
	
	// 正規化高斯核
	gaussian_kernel /= 256;
	
	// 定義 Gaussian 金字塔和 Laplacian 金字塔的向量
	vector<cv::Mat> gaussian_pyramid, laplacian_pyramid;
	int max_level = 6; // 金字塔的最大層數
	
	// 建立 Gaussian 金字塔
	cv::buildPyramid(grayImage, gaussian_pyramid, max_level);
	
	// 生成 Laplacian 金字塔
	for (int i = 0; i < max_level + 1; i++) {
		if (i == max_level)
			continue;
			
		cv::Mat m;
		cv::pyrUp(gaussian_pyramid[i + 1], m);
		cv::filter2D(m, m, CV_8U, gaussian_kernel);
		laplacian_pyramid.push_back(gaussian_pyramid[i] - m);
	}
	
	// 迭代還原影像
	cv::Mat iterate_image = gaussian_pyramid[gaussian_pyramid.size() - 1];
	for (int i = laplacian_pyramid.size() - 1; i >= 0; i--) {
		cv::Mat m;
		cv::pyrUp(iterate_image, m);
		cv::filter2D(m, m, CV_8U, gaussian_kernel);
		iterate_image = m + laplacian_pyramid[i];
	}
	
	// 顯示最終還原的G(0)影像
	cv::imshow("Output", iterate_image);
	
	cv::waitKey(0); 
	return 0;
}
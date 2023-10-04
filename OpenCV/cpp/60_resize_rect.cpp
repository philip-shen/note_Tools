/*
【Day17】​使用OpenCV進行影像縮放、拼貼、剪裁 

https://ithelp.ithome.com.tw/articles/10329066
*/

#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

int main()
{
	// 設定OpenCV的日誌級別為SILENT，以禁用日誌輸出
	cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT); 

	// 讀取名為"Lenna.png"的彩色圖像
	cv::Mat img = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_COLOR);

	// 建立一個空的Mat物件small_img來存儲調整大小後的圖像
	cv::Mat small_img;

	// 建立一個空的Mat物件resize_img來存儲輸出結果，並初始化為全黑彩色圖像
	cv::Mat resize_img = cv::Mat::zeros(img.size(), CV_8UC3);

	// 調整圖像大小為256x256像素
	cv::resize(img, small_img, cv::Size(256, 256));

	// 計算ROI（Region of Interest），以便將small_img複製到resize_img的中央位置
	cv::Rect roi = cv::Rect(
		resize_img.cols / 2 - small_img.cols / 2, resize_img.rows / 2 - small_img.rows / 2,
		small_img.cols, small_img.rows);

	// 將small_img複製到resize_img的ROI區域
	small_img.copyTo(resize_img(roi));

	// 建立一個新的Mat物件cropImage，用於存儲resize_img中的ROI區域
	cv::Mat cropImage = resize_img(roi);

	// 顯示整個resize_img
	cv::imshow("Output", resize_img);

	// 顯示cropImage，即resize_img中的ROI區域
	cv::imshow("Crop Image", cropImage);

	// 等待按鍵輸入，直到使用者按下鍵盤上的任意按鍵
	cv::waitKey(0);

	return 0;
}
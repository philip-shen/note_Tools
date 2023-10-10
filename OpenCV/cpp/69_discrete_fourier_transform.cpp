/*
 【Day28】影像離散傅立葉轉換(Discrete Fourier Transform)
2023-10-09 02:50:11
https://ithelp.ithome.com.tw/articles/10329091
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

int main()
{
    // 設定 OpenCV 日誌等級為 SILENT，以抑制除錯訊息
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_SILENT);

    // 讀取灰階影像 Lenna.png，如果無法讀取則輸出錯誤並退出
    cv::Mat I = cv::imread("/home/philphoenix/infinicloud/OpenCV/Lenna.png", cv::IMREAD_GRAYSCALE);
    if (I.empty()) {
        cout << "Error opening image" << endl;
        return EXIT_FAILURE;
    }
	cv::Mat padded; 
    // 將輸入影像擴展至最佳大小
    int n = cv::getOptimalDFTSize(I.rows);
    int m = cv::getOptimalDFTSize(I.cols);
    // 在邊界上添加零值，以確保影像大小為偶數
    copyMakeBorder(I, padded, 0, n - I.rows, 0, m - I.cols, cv::BORDER_CONSTANT, cv::Scalar::all(0));

    // 將影像轉換為複數格式，用於DFT計算
    cv::Mat input_channels[] = {cv::Mat_<float>(padded), cv::Mat::zeros(padded.size(), CV_32F)};
    cv::Mat input;
    cv::merge(input_channels, 2, input); // 將兩個平面合併成一個複數影像

    // 執行離散傅立葉變換（DFT）
    cv::Mat complexI;
    cv::dft(input, complexI);

    // 計算傅立葉變換的振幅，並轉換為對數尺度
    cv::Mat dft_result[2];
    cv::Mat magnitude;
    // 分離複數影像的實部和虛部
    cv::split(complexI, dft_result); 
    //使用實部和虛部計算大小
    cv::magnitude(dft_result[0], dft_result[1], magnitude);

    // 轉換為對數尺度
    cv::Mat magI = magnitude + cv::Scalar::all(1);
    cv::log(magI, magI);

    // 裁剪頻譜以適應偶數大小
    magI = magI(cv::Rect(0, 0, magI.cols & -2, magI.rows & -2));

    // 重新排列傅立葉變換的象限，使原點位於影像中心
    int cx = magI.cols / 2;
    int cy = magI.rows / 2;
    cv::Mat q0(magI, cv::Rect(0, 0, cx, cy)); // 左上 - 建立象限區域
    cv::Mat q1(magI, cv::Rect(cx, 0, cx, cy)); // 右上
    cv::Mat q2(magI, cv::Rect(0, cy, cx, cy)); // 左下
    cv::Mat q3(magI, cv::Rect(cx, cy, cx, cy)); // 右下
    cv::Mat tmp; // 交換象限（左上和右下）
    q0.copyTo(tmp);
    q3.copyTo(q0);
    tmp.copyTo(q3);
    q1.copyTo(tmp); // 交換象限（右上和左下）
    q2.copyTo(q1);
    tmp.copyTo(q2);

    // 正規化至 [0, 1]
    normalize(magI, magI, 0, 1, cv::NORM_MINMAX);

    // 顯示原始灰階影像
    cv::imshow("Input Image", I);

    // 如果輸入影像為浮點數，影像會自動乘以 255 並顯示
    cv::imshow("Spectrum Magnitude", magI);
    cv::waitKey();
    return EXIT_SUCCESS;
}
/*
【Day11】OpenCV 積分圖：影像處理的加速神器 

https://ithelp.ithome.com.tw/articles/10323555
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

int main()
{
    // 定義一個7x7大小的灰階影像數據
    uint8_t data[] = {
        2, 1, 0, 0, 3, 0, 0,
        0, 1, 0, 3, 2, 0, 3,
        0, 0, 0, 0, 1, 2, 0,
        3, 3, 2, 0, 1, 3, 0,
        3, 2, 3, 0, 2, 3, 0,
        0, 3, 0, 2, 0, 0, 0,
        1, 0, 3, 3, 2, 0, 3};
    
    // 創建一個7x7的灰階影像
    cv::Mat raw = cv::Mat(7, 7, CV_8UC1, data);
    
    // 創建一個空的Mat來存儲積分影像
    cv::Mat integral;
    
    // 計算積分圖
    cv::integral(raw, integral,CV_8U);
    
    // 輸出原始影像
    printf("f(x,y)=\n");
    print(raw);
    
    printf("\n----------\n");
    
    // 輸出積分圖
    printf("I(x,y)=\n");
    print(integral);
    
    printf("\n----------\n");
    
    return 0;
}
/*

*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

cv::Mat image; // 存儲讀取的影像
vector<vector<cv::Point>> contours; // 存儲影像輪廓
int selected_index = -1; // 選定的輪廓索引
int threshold; // 閾值，用於形狀相似度比較

// 函式聲明
int findSelectedContourIndex(int x, int y); // 在滑鼠點擊位置尋找選定的輪廓索引
void onClick(int event, int x, int y, int flags, void* param); // 滑鼠點擊事件處理函式
void onTrackbarSlide(int position, void*); // 滑動條值變化事件處理函式

// 函式定義

// 在滑鼠點擊位置尋找選定的輪廓索引
int findSelectedContourIndex(int x, int y) {
    for (int i = 0; i < contours.size(); i++) {
        cv::Rect rect = cv::boundingRect(contours[i]);
        if (rect.contains(cv::Point(x, y))) {
            return i;
        }
    }
    return -1;
}

// 滑鼠點擊事件處理函式
void onClick(int event, int x, int y, int flags, void* param)
{
    if (event & cv::EVENT_LBUTTONDOWN)
    {
        if (x != -1 && y != -1) {
            selected_index = findSelectedContourIndex(x, y);
        }

        if (selected_index == -1)
            return;

        // 建立一個影像，用於顯示選定的輪廓
        cv::Mat output = cv::Mat::zeros(cv::Size(image.cols, image.rows), CV_8UC3);
        cv::Rect target = cv::boundingRect(contours[selected_index]);
        cv::rectangle(output, target, cv::Scalar(0, 255, 255));
        cv::putText(output, to_string(selected_index), cv::Point(target.x, target.y - 5), cv::FONT_HERSHEY_COMPLEX, 0.5, cv::Scalar(0, 255, 255));

        // 在影像上繪製所有輪廓
        cv::drawContours(output, contours, -1, cv::Scalar(0, 255, 0));

        // 比較選定的輪廓與其他輪廓的形狀相似度
        for (int i = 0; i < contours.size(); i++) {
            if (selected_index == i)
                continue;
            cv::Rect rect = cv::boundingRect(contours[i]);
            cv::putText(output, to_string(i), cv::Point(rect.x, rect.y - 5), cv::FONT_HERSHEY_COMPLEX, 0.5, cv::Scalar(0, 255, 0));
            double delta_1 = cv::matchShapes(contours[selected_index], contours[i], cv::CONTOURS_MATCH_I1, 0);
            double delta_2 = cv::matchShapes(contours[selected_index], contours[i], cv::CONTOURS_MATCH_I2, 0);
            double delta_3 = cv::matchShapes(contours[selected_index], contours[i], cv::CONTOURS_MATCH_I3, 0);
            if (delta_3 < threshold / 10.0) {
                cv::rectangle(output, rect, cv::Scalar(0, 0, 255));
            }
        }

        // 顯示更新後的影像
        cv::imshow("Output", output);
        return;
    }
}

// 滑動條值變化事件處理函式
void onTrackbarSlide(int position, void*) {
    onClick(cv::EVENT_LBUTTONDOWN, -1, -1, -1, NULL);
}

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_ERROR);

    // 讀取灰階影像
    image = cv::imread("/home/philphoenix/infinicloud/OpenCV/img_Hu-moments.jpg", cv::IMREAD_GRAYSCALE);
    //image = cv::imread("/home/philphoenix/infinicloud/OpenCV/img_Hu-moments2_src.jpg", cv::IMREAD_GRAYSCALE);

    // 建立一個視窗用於顯示影像和輪廓
    cv::namedWindow("Output", cv::WindowFlags::WINDOW_NORMAL);
    cv::resizeWindow("Output", cv::Size(512.0 * ((float)image.cols / image.rows), 512));

    // 設定滑鼠點擊事件處理函式
    cv::setMouseCallback("Output", onClick);

    // 建立一個用於設定形狀相似度閾值的滑動條
    cv::createTrackbar("threshold", "Output", &threshold, 1000, onTrackbarSlide);

    // 將影像二值化
    cv::Mat binary;
    cv::threshold(image, binary, 0, 255, cv::THRESH_OTSU);

    // 建立一個用於顯示輪廓的影像
    cv::Mat output = cv::Mat::zeros(cv::Size(binary.cols, binary.rows), CV_8UC3);

    // 查找影像中的輪廓
    cv::findContours(binary, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_TC89_KCOS);

    // 對每個輪廓進行處理
    for (int i = 0; i < contours.size(); i++) {
        cv::Rect bounding_rect = cv::boundingRect(contours[i]);
        cv::putText(output, to_string(i), cv::Point(bounding_rect.x, bounding_rect.y - 5), cv::FONT_HERSHEY_COMPLEX, 0.5, cv::Scalar(0, 255, 0));
        cv::drawContours(output, contours, i, cv::Scalar(0, 255, 0));
    }

    // 顯示帶有輪廓的影像
    cv::imshow("Output", output);

    // 等待使用者操作
    cv::waitKey(0);
    return 0;
}
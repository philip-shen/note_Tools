#include <opencv2/opencv.hpp>

int main()
{
    cv::Mat img = cv::imread("/home/philphoenix/infinicloud/janken_dataset/choki/IMG_0770.JPG"); // IMG_0770.JPGをimgに代入.
    cv::imshow("img", img); // imgの表示.
    cv::waitKey(0); // キーが押されるまで待機.
    return 0;
}
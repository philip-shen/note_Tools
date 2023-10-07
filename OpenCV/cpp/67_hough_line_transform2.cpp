/*
OpenCVでギターをトラッキング
Last updated at 2020-07-12Posted at 2020-01-09

https://qiita.com/MxShun/items/4246145236606a234133
*/

#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/core/utils/logger.hpp"

using namespace std;

// 各フレーム行列
cv::Mat src;
// Hough変換入力行列
cv::Mat hough_src;
// Hough変換で検出された直線配列
std::vector<cv::Vec4i> lines;
// Hough変換で直線を検出した回数
int l_counter = 0;
// 移動平均範囲
int l_max = 10;
// 移動平均検出直線
int lines_[10][4];

// グレースケール化
cv::cvtColor(src, hough_src, CV_BGR2GRAY);
// エッジ検出
Canny(hough_src, hough_src, 100, 200, 3);
// Hough変換
cv::HoughLinesP(hough_src, lines, 1, CV_PI / 200, 50, 400, 20);
/*
 * 検出した線分の描画【テスト用】
 * cv::Vec4i l;
 * std::vector<cv::Vec4i>::iterator it = lines.begin();
 * for (; it != lines.end(); ++it)
 * {
 *  l = *it;
 *  cv::line(dst, cv::Point(l[0], l[1]), cv::Point(l[2], l[3]), cv::Scalar(0, 0, 255), 2, CV_AA);
 * }
 */

// 直線を1本以上検出
if (!lines.empty())
{
    // 古い直線情報の削除
    if (l_counter >= l_max)
    {
        for (int i = 0; i < 4; i++)
        {
            sum[i] -= lines_[l_counter % l_max][i];
        }
    }

    // 直線を3本以上検出
    if (lines.size() > 2)
    {
        // 中央値までのみ選択ソート
        for (int i = 0; i < ((lines.size() - 1) / 2); i++)
        {
            for (int j = i + 1; j < lines.size(); j++)
            {
                if (lines[i][1] > lines[j][1])
                {
                    for (int k = 0; k < 4; k++)
                    {
                        std::swap(lines[i][k], lines[j][k]);
                    }
                }
            }
        }
        // 中央値を代表値として採用
        for (int i = 0; i < 4; i++)
        {
            lines_[l_counter % l_max][i] = lines[(lines.size() - 1) / 2][i];
        }
    }
    else
    {
        // 先頭要素を代表値として採用
        for (int i = 0; i < 4; i++)
        {
            lines_[l_counter % l_max][i] = lines[0][i];
        }
    }

    // 新しい直線情報の追加
    for (int i = 0; i < 4; i++)
    {
        sum[i] += lines_[l_counter % l_max][i];
    }
    l_counter++;
    if (l_counter <= l_max)
    {
        for (int i = 0; i < 4; i++)
        {
            ave[i] = sum[i] / l_counter;
        }
    }
    else
    {
        for (int i = 0; i < 4; i++)
        {
            ave[i] = sum[i] / l_max;
        }
    }
    /*
     * 中央線（緑）の描画【テスト用】
     * cv::line(dst, cv::Point(ave[0], ave[1]), cv::Point(ave[2], ave[3]), cv::Scalar(0, 255, 0), 2, CV_AA);
     */
}

// 直線を1回以上検出
if(l_counter != 0)
{
    // 座標間情報を算出
    int width = ave[2] - ave[0];
    int height = ave[3] - ave[1];
    double theta = (std::atan2(height, width)) * (180 / CV_PI);
    cv::RotatedRect rect;
    if (ave[1] < ave[3]) // theta >= 0
    {
        rect = cv::RotatedRect(cv::Point(ave[0] + (width / 2),
                       ave[1] + (std::abs(height) / 2)), 
                       cv::Size(std::sqrt(width * width + height * height),
                       std::sqrt(width * width + height * height) * 0.2),
                       (float)theta);
    }
    else // theta < 0
    {
        rect = cv::RotatedRect(cv::Point(ave[0] + (width / 2),
                       ave[1] - (std::abs(height) / 2)),
                       cv::Size(std::sqrt(width * width + height * height),
                       std::sqrt(width * width + height * height) * 0.2),
                       (float)theta);
    }
    float angle = rect.angle;
    cv::Size rect_size = rect.size;
    if (rect.angle < -45.0)
    {
        angle += 90.0;
        std::swap(rect_size.width, rect_size.height);
    }
    // 回転矩形の角度から回転行列を算出
    cv::Mat M = cv::getRotationMatrix2D(rect.center, angle, 1.0);
    // 画像を回転
    cv::warpAffine(src, src, M, rgb.size(), cv::INTER_CUBIC);
    // 回転した画像から回転矩形切り出し
    cv::getRectSubPix(src, rect_size, rect.center, dst);
    /*
     * 回転矩形領域（青）の描画【テスト用】
     * cv::Point2f vertices2f[4];
     * rect.points(vertices2f);
     * std::vector<cv::Point> vertices;
     * for (int i = 0; i < 4; i++)
     * {
     *  vertices.push_back(vertices2f[i]);
     * }
     * const cv::Point* pts = (const cv::Point*) cv::Mat(vertices).data;
     * int npts = cv::Mat(vertices).rows;
     * cv::polylines(dst, &pts, &npts, 1, true, cv::Scalar(255, 0, 0), 3);
     */
}

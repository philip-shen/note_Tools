#include <npp.h>
#include <opencv2/imgcodecs.hpp>

#include <stdio.h>

int main() {
  // 変換する画像
  cv::Mat src = cv::imread("turing_white.png");
  // 変換された画像が入る変数
  cv::Mat dst;

  std::chrono::system_clock::time_point start, end;
  double elapsed;

  // GPU上のメモリ確保
  uint8_t *cudaSrc, *cudaDst;
  cudaMalloc((void **)&cudaSrc, src.rows * src.cols * 3);
  cudaMalloc((void **)&cudaDst, src.rows * src.cols * 3);

  // 画像をGPUにメモリコピー
  cudaMemcpy(cudaSrc, src.datastart, src.rows * src.step,
             cudaMemcpyHostToDevice);

  // 関数の引数の宣言
  NppiSize imSize; // 画像のサイズ
  imSize.width = src.cols;
  imSize.height = src.rows;
  // Roi: Reagion of Interestの略。画像サイズと同じでよい。
  NppiRect SrcRoi = {0, 0, src.cols, src.rows};
  NppiRect DstRoi = {0, 0, src.cols, src.rows};

  // 変換行列の宣言
  double matrix[3][3] = {{9.45135927e-01, -4.92482404e-02, -9.16291224e+01},
                         {1.86556287e-02, 9.08238651e-01, 1.29333648e+01},
                         {1.78247084e-05, -4.62799593e-05, 9.97536602e-01}};

  start = std::chrono::system_clock::now();
  for (int i = 0; i < 100; i++) {
    nppiWarpPerspective_8u_C3R(cudaSrc, imSize, src.step, SrcRoi, cudaDst,
                               src.step, DstRoi, matrix, NPPI_INTER_LINEAR);
  }
  end = std::chrono::system_clock::now();
  elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(end - start)
                .count();
  printf("npp 100 loop: %lf \n", elapsed);

  return 0;
}

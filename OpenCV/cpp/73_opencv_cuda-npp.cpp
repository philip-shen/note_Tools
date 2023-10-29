/*
图像旋转–利用opencv，cuda-npp的实现。
https://www.codenong.com/cs109689962/
*/

FIBITMAP* LoadImg(const char* szFile)
{
    FREE_IMAGE_FORMAT nFif;

    if (szFile == NULL || *szFile == 0)
    {
        return NULL;
    }

    if ((nFif = FreeImage_GetFileType(szFile, 0)) == FIF_UNKNOWN)
    {
        if ((nFif = FreeImage_GetFIFFromFilename(szFile)) == FIF_UNKNOWN)
        {
            return NULL;
        }
    }

    if (!FreeImage_FIFSupportsReading(nFif))
    {
        return NULL;
    }

    return FreeImage_Load(nFif, szFile);
}

void  NppbyFreeImage() {
    cudaError_t cuRet;
    NppStatus nppRet;
    BOOL fiRet = false;
    FIBITMAP* pSrcBmp = NULL;
    FIBITMAP* pDstBmp = NULL;
    unsigned char* pSrcData = NULL;
    unsigned char* pDstData = NULL;
    Npp8u* pSrcDataCUDA = NULL;
    Npp8u* pDstDataCUDA = NULL;
    NppiSize oSrcSize = { 0 };
    NppiSize oDstSize = { 0 };
    NppiRect oSrcROI = { 0 };
    NppiRect oDstROI = { 0 };
    int nImgBpp = 0;
    int nSrcPitch = 0;
    int nDstPitch = 0;
    int nSrcPitchCUDA = 0;
    int nDstPitchCUDA = 0;
    double aBoundingBox[2][2] = { 0 };
    double nAngle = 0;

    FreeImage_Initialise(0);

    /* 载入文件 */
    pSrcBmp = LoadImg("./bird.jpg");
    assert(pSrcBmp != NULL);

    //获取图像深度
    nImgBpp = (FreeImage_GetBPP(pSrcBmp) >> 3);
    cout << "freeImg nImgBpp :" << nImgBpp << endl;
    //获取数据
    pSrcData = FreeImage_GetBits(pSrcBmp);

    oSrcSize.width = (int)FreeImage_GetWidth(pSrcBmp);
    cout << "freeImg oSrcSize.width :" << oSrcSize.width << endl;
    oSrcSize.height = (int)FreeImage_GetHeight(pSrcBmp);
    cout << "freeImg oSrcSize.height :" << oSrcSize.height << endl;
    nSrcPitch = (int)FreeImage_GetPitch(pSrcBmp);
    cout << "freeImg nSrcPitch :" << nSrcPitch << endl;

    oSrcROI.x = oSrcROI.y = 0;
    oSrcROI.width = oSrcSize.width;
    oSrcROI.height = oSrcSize.height;

    nAngle = atof("90");

    /* 设置显卡,构建上下文 */
    cuRet = cudaSetDevice(0);
    assert(cuRet == cudaSuccess);

    /* 分配显存 */
    int type = 0;
    switch (nImgBpp)
    {
    case 1:
        pSrcDataCUDA = nppiMalloc_8u_C1(oSrcSize.width, oSrcSize.height, &nSrcPitchCUDA);
        break;
    case 3:
        pSrcDataCUDA = nppiMalloc_8u_C3(oSrcSize.width, oSrcSize.height, &nSrcPitchCUDA);
        break;
    case 4:
        pSrcDataCUDA = nppiMalloc_8u_C4(oSrcSize.width, oSrcSize.height, &nSrcPitchCUDA);
        break;
    default:
        assert(0);
        break;
    }
    assert(pSrcDataCUDA != NULL);

    /* 将原图传入显存 */
    cudaMemcpy2D(pSrcDataCUDA, nSrcPitchCUDA, pSrcData, nSrcPitch, oSrcSize.width * nImgBpp, oSrcSize.height, cudaMemcpyHostToDevice);

    /* 计算旋转后长宽 */
    nppiGetRotateBound(oSrcROI, aBoundingBox, nAngle, 0, 0);
    oDstSize.width = (int)ceil(fabs(aBoundingBox[1][0] - aBoundingBox[0][0]));
    oDstSize.height = (int)ceil(fabs(aBoundingBox[1][1] - aBoundingBox[0][1]));

    /* 建目标图 */
    pDstBmp = FreeImage_Allocate(oDstSize.width, oDstSize.height, nImgBpp << 3);
    assert(pDstBmp != NULL);

    pDstData = FreeImage_GetBits(pDstBmp);

    nDstPitch = (int)FreeImage_GetPitch(pDstBmp);
    cout << "freeImg nDstPitch :" << nDstPitch << endl;
    oDstROI.x = oDstROI.y = 0;
    oDstROI.width = oDstSize.width;
    cout << "freeImg  oDstSize.width :" << oDstSize.width << endl;
    oDstROI.height = oDstSize.height;
    cout << "freeImg oDstSize.height :" << oDstSize.height << endl;

    /* 分配显存 */
    switch (nImgBpp)
    {
    case 1:
        pDstDataCUDA = nppiMalloc_8u_C1(oDstSize.width, oDstSize.height, &nDstPitchCUDA);
        break;
    case 3:
        pDstDataCUDA = nppiMalloc_8u_C3(oDstSize.width, oDstSize.height, &nDstPitchCUDA);
        break;
    case 4:
        pDstDataCUDA = nppiMalloc_8u_C4(oDstSize.width, oDstSize.height, &nDstPitchCUDA);
        break;
    }
    assert(pDstDataCUDA != NULL);
    cudaMemset2D(pDstDataCUDA, nDstPitchCUDA, 0, oDstSize.width * nImgBpp, oDstSize.height);

    /* 处理 */
    switch (nImgBpp)
    {
    case 1:
        nppRet = nppiRotate_8u_C1R(pSrcDataCUDA, oSrcSize, nSrcPitchCUDA, oSrcROI,
            pDstDataCUDA, nDstPitchCUDA, oDstROI,
            nAngle, -aBoundingBox[0][0], -aBoundingBox[0][1], NPPI_INTER_CUBIC);
        break;
    case 3:
        nppRet = nppiRotate_8u_C3R(pSrcDataCUDA, oSrcSize, nSrcPitchCUDA, oSrcROI,
            pDstDataCUDA, nDstPitchCUDA, oDstROI,
            nAngle, -aBoundingBox[0][0], -aBoundingBox[0][1], NPPI_INTER_CUBIC);
        break;
    case 4:
        nppRet = nppiRotate_8u_C4R(pSrcDataCUDA, oSrcSize, nSrcPitchCUDA, oSrcROI,
            pDstDataCUDA, nDstPitchCUDA, oDstROI,
            nAngle, -aBoundingBox[0][0], -aBoundingBox[0][1], NPPI_INTER_CUBIC);
        break;
    }
    assert(nppRet == NPP_NO_ERROR);

    cudaMemcpy2D(pDstData, nDstPitch, pDstDataCUDA, nDstPitchCUDA, oDstSize.width * nImgBpp, oDstSize.height, cudaMemcpyDeviceToHost);

    fiRet = FreeImage_Save(FIF_BMP, pDstBmp, "./retFreeImage.bmp");
    assert(fiRet);

    nppiFree(pSrcDataCUDA);
    nppiFree(pDstDataCUDA);

    cudaDeviceReset();

    FreeImage_Unload(pSrcBmp);
    FreeImage_Unload(pDstBmp);
}

void  NppbyOpenCV2() {
    cudaError_t cuRet;
    NppStatus nppRet;
    BOOL fiRet = false;
    unsigned char* pSrcData = NULL;
    unsigned char* pDstData = NULL;
    Npp8u* pSrcDataCUDA = NULL;
    Npp8u* pDstDataCUDA = NULL;
    NppiSize oSrcSize = { 0 };
    NppiSize oDstSize = { 0 };
    NppiRect oSrcROI = { 0 };
    NppiRect oDstROI = { 0 };
    int nImgBpp = 0;
    int nSrcPitch = 0;
    int nDstPitch = 0;
    int nSrcPitchCUDA = 0;
    int nDstPitchCUDA = 0;
    double aBoundingBox[2][2] = { 0 };
    double nAngle = 0;

    FreeImage_Initialise(0);

    /* 载入文件 */
    Mat pSrcMat = imread("./bird.jpg", IMREAD_UNCHANGED);

    //获取图像深度
    nImgBpp = pSrcMat.channels();
    cout << "freeImg nImgBpp :" << nImgBpp << endl;
    //获取数据
    pSrcData = pSrcMat.data;

    oSrcSize.width = pSrcMat.cols;
    oSrcSize.height = pSrcMat.rows;
    nSrcPitch = pSrcMat.step;

    oSrcROI.x = oSrcROI.y = 0;
    oSrcROI.width = oSrcSize.width;
    oSrcROI.height = oSrcSize.height;

    nAngle = atof("90");

    /* 设置显卡,构建上下文 */
    cuRet = cudaSetDevice(0);
    assert(cuRet == cudaSuccess);

    /* 分配显存 */
    int type = 0;
    switch (nImgBpp)
    {
    case 1:
        pSrcDataCUDA = nppiMalloc_8u_C1(oSrcSize.width*nImgBpp, oSrcSize.height, &nSrcPitchCUDA);
        break;
    case 3:
        pSrcDataCUDA = nppiMalloc_8u_C3(oSrcSize.width*nImgBpp, oSrcSize.height, &nSrcPitchCUDA);
        break;
    case 4:
        pSrcDataCUDA = nppiMalloc_8u_C4(oSrcSize.width*nImgBpp, oSrcSize.height, &nSrcPitchCUDA);
        break;
    default:
        assert(0);
        break;
    }
    assert(pSrcDataCUDA != NULL);

    /* 将原图传入显存 */
    cudaMemcpy2D(pSrcDataCUDA, nSrcPitchCUDA, pSrcData, nSrcPitch, oSrcSize.width*nImgBpp, oSrcSize.height, cudaMemcpyHostToDevice);

    /* 计算旋转后长宽 */
    nppiGetRotateBound(oSrcROI, aBoundingBox, nAngle, 0, 0);
    oDstSize.width = (int)ceil(fabs(aBoundingBox[1][0] - aBoundingBox[0][0]));
    oDstSize.height = (int)ceil(fabs(aBoundingBox[1][1] - aBoundingBox[0][1]));

    /* 建目标图 */
    Mat pDstMat(oDstSize.height, oDstSize.width, pSrcMat.type());

    pDstData = pDstMat.data;

    nDstPitch = pDstMat.step;
    oDstROI.x = oDstROI.y = 0;
    oDstROI.width = oDstSize.width;
    oDstROI.height = oDstSize.height;

    /* 分配显存 */
    switch (nImgBpp)
    {
    case 1:
        pDstDataCUDA = nppiMalloc_8u_C1(oDstSize.width, oDstSize.height, &nDstPitchCUDA);
        break;
    case 3:
        pDstDataCUDA = nppiMalloc_8u_C3(oDstSize.width, oDstSize.height, &nDstPitchCUDA);
        break;
    case 4:
        pDstDataCUDA = nppiMalloc_8u_C4(oDstSize.width, oDstSize.height, &nDstPitchCUDA);
        break;
    }
    assert(pDstDataCUDA != NULL);
    cudaMemset2D(pDstDataCUDA, nDstPitchCUDA, 0, oDstSize.width * nDstPitch, oDstSize.height);

    /* 处理 */
    switch (nImgBpp)
    {
    case 1:
        nppRet = nppiRotate_8u_C1R(pSrcDataCUDA, oSrcSize, nSrcPitchCUDA, oSrcROI,
            pDstDataCUDA, nDstPitchCUDA, oDstROI,
            nAngle, -aBoundingBox[0][0], -aBoundingBox[0][1], NPPI_INTER_CUBIC);
        break;
    case 3:
        nppRet = nppiRotate_8u_C3R(pSrcDataCUDA, oSrcSize, nSrcPitchCUDA, oSrcROI,
            pDstDataCUDA, nDstPitchCUDA, oDstROI,
            nAngle, -aBoundingBox[0][0], -aBoundingBox[0][1], NPPI_INTER_CUBIC);
        break;
    case 4:
        nppRet = nppiRotate_8u_C4R(pSrcDataCUDA, oSrcSize, nSrcPitchCUDA, oSrcROI,
            pDstDataCUDA, nDstPitchCUDA, oDstROI,
            nAngle, -aBoundingBox[0][0], -aBoundingBox[0][1], NPPI_INTER_CUBIC);
        break;
    }
    assert(nppRet == NPP_NO_ERROR);

    cudaMemcpy2D(pDstData, nDstPitch, pDstDataCUDA, nDstPitchCUDA, oDstSize.width*nImgBpp, oDstSize.height, cudaMemcpyDeviceToHost);

    imwrite("./retOpenCV2_90.bmp", pDstMat);
    assert(fiRet);

    nppiFree(pSrcDataCUDA);
    nppiFree(pDstDataCUDA);

    cudaDeviceReset();
}
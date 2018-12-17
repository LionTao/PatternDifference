def Pattern_Otherness_Calculation(ImageDirectory):
    import cv2
    import numpy as np

    srcimg = cv2.imread(ImageDirectory, 0)
    height, width = srcimg.shape

    #    print(srcimg.shape)
    #   将图像resize至边长为9的倍数
    if height % 9 != 0:
        height = height + (9 - height % 9)
    if width % 9 != 0:
        width = width + (9 - width % 9)
    dstimg = cv2.resize(srcimg, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
    #    print(dstimg.shape)

    height, width = dstimg.shape
    N = height * width // 81
    ImageList = []  # 存储图像矩阵
    OthernessList = []  # 存储差异性矩阵
    res = []  # 存储归一化后的结果
    sum = np.mat(np.zeros((9, 9)))

    for i in range(height // 9):
        for j in range(width // 9):
            sum += dstimg[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9]
            ImageList.append(dstimg[i * 9:(i + 1) * 9, j * 9:(j + 1) * 9])
    Pa = sum / N  # 平均图像块
    for i in range(N):
        OthernessList.append(np.sum(np.abs(Pa - ImageList[i])))

    #   归一化
    maxOtherness = max(OthernessList)
    minOtherness = min(OthernessList)
    for i in range(N):
        res.append((OthernessList[i] - minOtherness) / (maxOtherness - minOtherness))

    #    print(res)
    return res


if __name__ == '__main__':
    res=Pattern_Otherness_Calculation("13000.jpeg")
    print(res)

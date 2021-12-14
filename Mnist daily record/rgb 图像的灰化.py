import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as im


'''
      1）Gray=B；Gray=G；Gray=R

      2）Gray=max(B+G+R)

      3）Gray=(B+G+R)/3

      4）Gray= 0.072169B+ 0.715160G+ 0.212671R

      5）Gray= 0.11B+ 0.59G+ 0.3R
      关于YUV空间的彩色图像，其Y的分量的物理意义本身就是像素点的亮度，由该值反映亮度等级，
      因此可根据RGB和YUV颜色空间的变化关系建立亮度
      Y与R、G、B三个颜色分量的对应：Y=0、.3R+0.59G+0.11B，以这个亮度值表达图像的灰度值。  
      '''

def path(s) -> str:

    for i in s:
        if(i == '\\'):
            i = '/'
    return s

# print(img.shape)#     (512, 512, 3)   512x512 像素  三维  存储方式为  3个矩阵

'''list assignment index out of range：列表超过限制

一种情况是：list[index]index超出范围

另一种情况是：list是一个空的，没有一个元素，进行list[0]就会出现错误！'''
img = im.imread(path("C:/Users/林丿子轩/PycharmProjects/2021/12/Mnist/Mnist daily record/baby_GT.bmp"))

def Gray(img):
    imgR = img[0]
    imgG = img[1]
    imgB = img[2]

    print(imgR)
    print(imgB)
    print(img[3])

def convert_rgb_to_y(img):
    if type(img) == np.ndarray:
        return img[:, :, 0]
        #return 16. + (64.738 * img[:, :, 2] + 129.057 * img[:, :, 1] + 25.064 * img[:, :, 0]) / 256.
    # elif type(img) == torch.Tensor:
    #     if len(img.shape) == 4:
    #         img = img.squeeze(0)
    #     return 16. + (64.738 * img[0, :, :] + 129.057 * img[1, :, :] + 25.064 * img[2, :, :]) / 256.
    else:
        raise Exception('Unknown Type', type(img))

print(Gray(img))
plt.imshow(convert_rgb_to_y(img))
plt.show()
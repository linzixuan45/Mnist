import matplotlib.pyplot as plt
import matplotlib.image as im
import numpy as np
#编辑离散数据


# x = np.arange(0,6,0.1)
# y1 =np.sin(x)
# y2 = np.cos(x)
# plt.plot(x,y1,label = "sin")
# plt.plot(x,y2,linestyle="--",label ="cos",color = 'green')  #用虚线绘制
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('sin & cos')
# '''
# 实际使用中，legend（）有一个loc参数，用于控制图例的位置。
# 比如 plot.legend(loc=2) , 这个位置就是4象项中的第二象项，也就是左上角。
# loc可以为1,2,3,4 这四个数字。
# '''
# plt.legend(loc = 1) # 显示图例的位置
#
# plt.show()


#编辑图片
img = im.imread('C:/Users/林丿子轩/Desktop/paper code/SRCNN-pytorch-master/data/baby_GT.bmp')
for i in img:
    print(i)
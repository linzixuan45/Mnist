import numpy as np
import matplotlib.pyplot as plt


 # numpy 中的函数
 # y = y.astype(np.int)   类型转换
 # y = y>4  bool 运算
 # np.dim(x)  返回X的维度
 # A.shape  实例的形状
 # 矩阵的乘法  np.dot(A,B)  点积
def sigmoid(x):
    return 1/(1+np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def softmax_1(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y


def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x-c)
    sum_x = np.sum(exp_x)
    return exp_x / sum_x



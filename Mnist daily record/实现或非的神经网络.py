import numpy as np

def And(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tem = np.sum(w*x) +b
    if tem <=0:
        return 0
    else:
        return 1

def Nand(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tem = np.sum(w * x) + b
    if tem <= 0:
        return 0
    else:
        return 1


def Or( x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5  , 0.5])
    b = -0.2
    tem = np.sum(w * x) + b
    if tem <= 0:
        return 0
    else:
        return 1


def Xor(x1,x2):
    s1 = Nand(x1,x2)
    s2 = Or(x1,x2)
    y = And(s1,s2)
    return y


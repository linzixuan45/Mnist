import  numpy as np
import string

#1.13
#  python是动态类型语言，也就是不需要指定变量的类型。其自动依据上下文来判断类型

#1.34 切片
# a = np.array(range(1,10))#[1 2 3 4 5 6 7 8 9]
# b = a[0:2] #[1 2]
# c = a[:3]#[1 2 3]
# d = a[0:9:2]#[1 3 5 7 9]
# e = a[-1::-1]#[9 8 7 6 5 4 3 2 1]
# f = a[:-2:2]#[1 3 5 7]
# g = a[-1:]# [9]
# alpha = [a,b,c,d,e,f,g]
# for i in alpha:
#     print(i)


#1.36 bool 注意其运算符为
# and  or   not  xor



# 1.42 类  class  包含构造函数 __init__(self,,,)

# class man:
#     def __init__(self,name):
#         self.name = name
#     def hello(self):
#         print(self.name)
#     def creat(self,age,school):
#         self.age = age
#         self.school = school
#     def introduce(self):
#         print("name: "+self.name+"  school is:  "+self.school)
#         age = str(self.age)
#         print('age:'+age)
#
# jlx = man("zixuan")
# jlx.creat(22,"GDUT")
# jlx.introduce()
# print(type(jlx.age))

# 1.54 numpy 的 N维数组
# A = np.array([[1,2],[3,4]])
# print(A)



#1.55 numpy 的广播功能
    # 会自动将低纬度向量升到高纬度

#1.56 访问元素
    # .flatten() 使对象一维化
    #bool化
# X =np.array([[2,3],[4,5],[6,7]])
# X = X.flatten()
# X = X>15
# print(type(X[0]))  #<class 'numpy.bool_'>
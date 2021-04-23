'''
Author: Yannq
Date: 2021-02-18 17:38:48
LastEditTime: 2021-02-18 17:43:26
LastEditors: Yannq
FilePath: \Day06\function0.py
Description: 函数参数的默认值与可变参数
Attention: 
'''

def add1(a=0, b=0, c=0):
    # 三个数相加
    print('a = %d, b = %d, c = %d'%(a, b, c))
    return a + b + c

def add2(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add1(c = 1))
print(add2(1, 2, 3, 4, 5, 6, 7))

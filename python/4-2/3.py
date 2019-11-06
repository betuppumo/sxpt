#coding=utf-8

from math import pi as PI

n = int(input())

# 请在此添加代码，实现圆的面积计算，并输出面积结果
#********** Begin *********#

def s(n):
    return  round(PI*(n**2),2)

print(s(n))

#********** End **********#


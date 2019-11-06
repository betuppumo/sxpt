#coding=utf-8

# 输入正整数n
n = int(input())

# 请在此添加代码，对输入的正整数n进行阶乘运算，并输出计算结果。
#********** Begin *********#

def fact(n):
    t=1
    for i in range(1,n+1):
        t*=i
    return t
print(fact(n))

#********** End **********#


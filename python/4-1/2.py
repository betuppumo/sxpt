#coding=utf-8

# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最大公约数
#********** Begin *********#
def gcd(m,n):
    if not m:return n
    elif not n:return m
    elif m is n :return m
    if m>n: d=n
    else:d=m
    while m%d or n%d:d-=1
    return d


#********** End **********#

# 调用函数，并输出最大公约数
print(gcd(a,b))



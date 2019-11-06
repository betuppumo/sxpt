#coding=utf-8

# 输入一个正整数
x = int(input())

# 请在此添加代码，将输入的一个正整数分解质因数
#********** Begin *********#

def f(n,value=[]):
    for i in range(2,int(n/2+1)):
        if n%i==0:
            value.append(i)
            f(n/i,value)
            # if not value:value.append(n)
            return value
        if i >=n/2-1:
            value.append(int(n))
            break
result=f(x)
if result is None:result=[x]

#********** End **********#

# 输出结果，利用map()函数将结果按照规定字符串格式输出
print(x,'=','*'.join(map(str,result)))



# 定义位运算处理函数bit, 其中bitone和bittwo两个参数为需要进行位运算的变量，由测试程序读入。
def bit(bitone, bittwo):
    # 请在此处填入将bitone,bittwo按位与的代码，并将运算结果存入result变量
    ###### Begin ######
    result=bitone&bittwo
    ####### End #######
    print(result)

    # 请在此处填入将bitone,bittwo按位或的代码，并将运算结果存入result变量
    ###### Begin ######
    result=bitone  | bittwo
    ####### End #######
    print(result)

    # 请在此处填入将bitone,bittwo按位异或的代码，并将运算结果存入result变量
    ###### Begin ######
    result = bitone ^ bittwo
    ####### End #######
    print(result)

    # 请在此处填入将bitone按位取反的代码，并将运算结果存入result变量
    ###### Begin ######
    result = ~ bitone
    ####### End #######
    print(result)

    # 请在此处填入将bittwo左移动两位的代码，并将运算结果存入result变量
    ###### Begin ######
    result=bittwo<<2
    ####### End #######
    print(result)

    # 请在此处填入将bittwo右移动两位的代码，并将运算结果存入result变量
    ###### Begin ######
    result=bittwo>>2
    ####### End #######
    print(result)
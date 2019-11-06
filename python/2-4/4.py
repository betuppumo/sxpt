# 定义成员片段函数member，参数me为待判断的人名，member_list为成员名单
def member(me, member_list=[]):
    # 请在if后面的括号中填入判断变量me是否存在于list中的语句
    ###### Begin ######
    if ( me in member_list):
        print("我是篮球社成员")
    else:
        print("我不是篮球社成员")
    ####### End #######


    # 请在if后面的括号中填入判断变量me是不否存在于list中的语句
    ###### Begin ######
    if (me not in member_list ):
        print("我不是篮球社成员")
    else:
        print("我是篮球社成员")
        ####### End #######

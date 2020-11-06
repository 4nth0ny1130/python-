a = input("输入ascii码,以,分隔:")

a = a.split(",") #用,切分字符串放进一个列表

for i in a :    #遍历这个列表
    i = int(i)  #转int类
    i = chr(i)  #ascii转文字
    print(i,end='')

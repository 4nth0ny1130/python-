import re
a = input(":")                   #获取输入
p = re.compile('\d+', re.S)
all = re.findall(p, a)           #匹配正则
results = list(map(int, all))    #把str表换为int表


for x in results:               #迭代
    a=str("&#x" + hex(x))       #hex输出int,转为str
    a1=a.replace("0x","")       #replace方法删除0x
    print(a1,end='')           #输出+;  不换行




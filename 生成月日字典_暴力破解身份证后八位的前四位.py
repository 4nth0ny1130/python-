month = []
day = []
for i in range(0,4):
    for j in range(0,10):
        d = str(i) + str(j)
        day.append(d)
        if d == '31':
            break
    if d == '31':
        break
day = day[1:]


month = []
for i in range(0,3):
    for j in range(0,10):
        d = str(i) + str(j)
        month.append(d)
        if d == '12':
            break
    if d == '12':
        break
month = month[1:]
date = []
for i in month:
    for j in day:
        md = i + j
        date.append(md)
month = month[1:]
date.remove('0230')
date.remove('0231')
date.remove('0431')
date.remove('0631')
date.remove('0931')
date.remove('1131')

date =str(date)                           #怎么尝试打印出来都是['0101','0102','0103','0104','0105']这样的,要不就死活不换行
date= date.replace("\'","")               #没办法了就用这么蠢的方法,有更好的方法把它的输出变成一行一个的欢迎提交Issues,感谢OTZ
date= date.replace("[","")                
date= date.replace("]","")
date= date.replace(",","")
date= date.replace(" ","\n")

f = open(r'C:\Users\min\Desktop\生成文件\月日.txt',"a")   #自己改文件路径
print (date,file = f)
f.close()
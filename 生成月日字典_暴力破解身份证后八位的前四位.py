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

f = open(r'C:\Users\min\Desktop\生成文件\月日.txt',"a")   #自己改文件路径

for line in date:             #变成一行一个
    f.write(line+'\n')
f.close()
f = open(r'C:\Users\min\Desktop\生成文件\月日.txt',"a")
i=0
while i < 9999:
    i=str(i).rjust(4,'0')
    f.write(i+'\n')
    i=int(i)
    i+=1
f.close

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

mmdd = []
for i in month:
    for j in day:
        md = i + j
        mmdd.append(md)
mmdd.remove('0230')
mmdd.remove('0231')
mmdd.remove('0431')
mmdd.remove('0631')
mmdd.remove('0931')
mmdd.remove('1131')


date=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
a=[]
for i in date:
    i=ord(i)
    a.append(i)
a.append(95)    #多加个下划线的ascii值
f = open(r'C:\Users\min\Desktop\生成文件\ascii所有字母字典.txt',"a")
for line in a:             #变成一行一个
    f.write(str(line)+'\n')
f.close()
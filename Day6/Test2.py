f1 ='./file1.txt'
fh = open(f1,'r')
str = fh.read()
strNew = ''
fh.close()
alist = list(str.strip().split('\n'))
dic = dict()
for i in alist:
    dic[i.split(';')[0].split(':')[1].strip()] =i.split(';')[1].split(':')[1].strip()

for key in dic:
    strNew +=f'name:{key};salary:{dic[key]};tax:{0.1*int(dic[key]):.0f};income:{0.9*int(dic[key]):.0f}\n'

f1 ='./file2.txt'
fh = open(f1,'w')
fh.write(strNew)
fh.close()
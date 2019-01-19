import pprint
fileName ='./0005_1.txt'
def putInfoToDict(fileName):
    clist = []
    dic1 =dict()
    with open(fileName) as fo:
        lines = fo.read().splitlines()
        for line in lines:
            line = line.replace('\t','').replace('\'','').replace(',','').replace('(','').replace(')','').replace(';','').strip()
            temp = line.split(' ')
            checkintime = temp[0]+' '+temp[1]
            lessonid = temp[2].strip()
            stuid = int(temp[3].strip())
            dic2 = {'lessonid': int(lessonid), 'checkintime': checkintime}
            if stuid not in dic1.keys():
                clist.append(dic2)
                dic1[stuid] = clist
            else:
                dic1[stuid].append(dic2)
            clist = []
    pprint.pprint(dic1)
putInfoToDict(fileName)
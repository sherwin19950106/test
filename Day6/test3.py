'''
冒泡排序法
'''

def forList(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list


alist =[4,5,1,3,7,9,2,6,8,0]
print(forList(alist))
'''
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面
'''

def mySort(alist):
    newList = []
    while len(alist) > 0:
        samll = min(alist)
        newList.append(samll)
        del alist[alist.index(samll)]
    return  newList


alist = [7, 3, 4, 3, 8, 1, 2]
print(mySort(alist))
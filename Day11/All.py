from random import  randint
import time
import os


def choose1(room):
    while True:
        choose = input('请选择敲门/喂食（1/2）')
        if choose == '1':
            room.animal.roar()
            break
        elif choose == '2':
            room.animal.feed(input('输入食物名称'))
            break
        else:
            print('输入错误')



class Tiger():
    name = '老虎'
    weight = 200
    def roar(self):
        print('wow!!')
        self.weight -= 5
        print(f'这是老虎，体重减轻5，现在体重是{self.weight}')
    def feed(self, food):
        if food =='meat':
            self.weight +=10
            print(f'这是老虎，喂对了，体重加10斤,现在体重是{self.weight}')

        else:
            self.weight -= 10
            print(f'这是老虎，喂错了，体重减轻10，现在体重是{self.weight}')

class Sheep():
    name = '羊羊'
    weight = 100
    def roar(self):
        print('mie~~')
        self.weight -= 5
        print(f'这是羊羊,体重减轻5，现在体重是{self.weight}')
    def feed(self, food):
        if food =='grass':
            self.weight +=10
            print(f'这是羊羊,喂对了，体重加10斤,现在体重是{self.weight}')
        else:
            self.weight -= 10
            print(f'这是羊羊,喂错了，体重减轻10，现在体重是{self.weight}')
class Room():
    def __init__(self,num):
        self.num =num
        if randint(0, 1) == 1:
            self.animal =Tiger()
        else:
            self.animal = Sheep()

print('------游戏开始------')
rlist = []
for one in range(1, 11):
    r = Room(one)
    rlist.append(r)
for one in rlist:
    print(f'房间号：{one.num:0>2}  动物：{one.animal.name}  体重：{one.animal.weight}')
startTime = time.time()
while True:
    endTime =time.time()
    if (endTime - startTime)>10:
        break
    else:
        room = rlist[randint(0,9)]
        print(f'房间号{room.num}')
        choose1(room)
print('------游戏结束------')
print('------结果如下------')
for one in rlist:
    print(f'房间号：{one.num:0>2}  动物：{one.animal.name}  体重：{one.animal.weight}')




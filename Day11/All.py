'''
每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
然后随机给出房间号，要求游戏者选择敲门还是喂食。
如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤
如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。
游戏3分钟结束后，显示每个房间的动物和它们的体重。
'''



from random import  randint
import time

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
    if (endTime - startTime)>180:
        break
    else:
        room = rlist[randint(0,9)]
        print(f'房间号{room.num}')
        choose1(room)
print('------游戏结束------')
print('------结果如下------')
for one in rlist:
    print(f'房间号：{one.num:0>2}  动物：{one.animal.name}  体重：{one.animal.weight}')




# coding: utf-8
from random import randint
def game():
    s= randint(1,1000)
    i=-1
    while i!=s:

        i=int(input('請猜一個1~1000間的數字：'))
        if i>s:
            print('太大了，找小一點喔~')
        elif i==s:
            print('恭喜你~~答對了！')
        else:
            print('太小啦，再找大一點吧')
play=True
while play:
    game()
    print('--------------')
    again=input('再玩一次？')
    if again=='no':
        play=False

# coding: utf-8
words='''枯藤
老樹
昏鴨
小橋
流水
人家
古道
西風
瘦馬
夕陽
西下
斷腸人
在天涯'''
st=words.split('\n')
from random import sample,randint,choices
n=randint(5,10)

for i in range(n):
    m=randint(3,6)
    sentance =sample(st,m)
    print(' '.join(sentance))

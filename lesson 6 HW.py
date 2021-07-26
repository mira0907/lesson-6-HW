# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 11:35:07 2021

@author: dkjua
"""
score=[]
na=[]
high=0
who=0
y=int(input('學生數量?'))
for i in range(y):
    name=input('名字?')
    x=int(input('成績?'))
    score.append(x)
    na.append(name)
    if high<x:
        high=x
        who=i
print(high)
print(na[who])

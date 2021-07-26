# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:31:19 2021

@author: dkjua
"""
mylist=[]
i=0
y=int(input('人數?'))
while i<int(y):
    x=input('成績?')
    mylist.append(x)
    i=i+1

i=0
while i<y :
    print("第" + str(i+1) + "個成績是" + mylist[i] + "分")
    i=i+1
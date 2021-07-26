# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:47:56 2021

@author: dkjua
"""
students=[]
num=input('學生數量?')
for i in range(int(num)):
    name=input('名字?')
    score=int(input('成績?'))
    student=[name,score]
    students.append (student)
high=0
who_high=0
for i in range(int(num)):
    if students[i][1]>high:
        high=students[i][1]
        who_high=i
print(str(high)+';'+str(students[who_high][0]))
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:11:35 2020

@author: domi
"""
scores = []
sum = 0
highest = 0
lowest = 100



x=input("people")
x=int(x)
print(x)

for i in range(x):
    score = input("輸入成績")
    score = int(score)
    scores.append(score)
for i in range(x):
    if scores[i] > highest:
        highest = scores[i]
    if scores[i] < lowest:
        lowest = scores[i]
    sum =scores[i] + sum
average = sum / x

print("平均分:",average)
print("最高分:",highest)
print("最低分:",lowest)
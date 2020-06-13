# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:53:46 2020

@author: domi
"""


math=list()
avg=0
total=()

x=input("people")
x=int(x)
print(x)

for i in range(x):
   
    
    name = input('Please input the name: ')
    score = input("輸入成績")
    score = int(score)
    oneperson = list()
    oneperson.append(name)
    oneperson.append(score)
    math.append(oneperson)
print(math)
# avg score
for i in math:
    total = total+i[1]
avg = total / x
print("The average is", avg)
# highest score
high=0
person=''
for i in math:
    if i[1] < high:
        high=i[1]
        person=i[0]
print(person, "got the Lowest score:", high)
# lowest score
low=100
person=''
for i in math:
    if i[1] < low:
        low=i[1]
        person=i[0]
print(person, "got the Lowest score:", low)

print("平均分:",avg)

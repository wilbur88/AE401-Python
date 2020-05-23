# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:02:34 2020

@author: domi
"""


math=input('輸入數學分數')
eng=input ('輸入英文分數')
math=int(math)
eng=int(eng)
if (math>=90 and eng>=90):
    print("你成功了!!")
elif(math<60 and eng<60):
    print("再加油")
elif(math<60 or eng<60):
    print("要處罰")
    

else:
    print('pass')



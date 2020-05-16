# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:50:45 2020

@author: domi
"""


print("輸入員的半徑")
r=input("你的半徑: ")
r=float(r)
print(type(r))
o='%2.2f' %(r*2*3.14)
a=r*r*3.14
print('周長是' , o)
print('面積是' , a)

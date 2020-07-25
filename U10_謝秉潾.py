# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:15:19 2020

@author: domi
"""

"""
fo = open('myfile.txt', 'w')
fo.write('this is a test')

"""


fo = open('myfile.txt', 'a')
fo.write('and I')
fo.close()

fo = open('myfile.txt', 'r')
myletter = fo.read()
print(myletter)
fo.close()

import os.path

if os.path.isfile('myfile.txt'):
        print('yes')
else:
        print('no')
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:40:27 2020

@author: domi
"""


import turtle
alex=turtle.Turtle()

def draw_square(unit):
  for i in range(4):
    alex.forward(unit)
    alex.left(90)
    
draw_square(10)
draw_square(15)
draw_square(30)
turtle.done()
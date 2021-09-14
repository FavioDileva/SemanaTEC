#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:47:24 2021

@author: faviodileva
"""

"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
import turtle

from freegames import vector




def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    
    r=start.x-end.x 

    turtle.circle(r)
    end_fill()



    

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x,start.y)
    down()
    begin_fill()
    
     for count in range(4):
            forward (end.x-start.x)
            left(90)
            forward(end.y-start.y)
            left (90)
      end_fill()

def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3): #Se hace el for para el proceso 3 veces por los lados del triangulo
        forward(end.x - start.x) #Se avanza hacia la dirección deseada en el tamaño deseado
        left(120) #Se da un giro a la izquierda de 120 grados

    end_fill()
   





def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda:color('yellow'),'Y') #Color agregado amarillo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

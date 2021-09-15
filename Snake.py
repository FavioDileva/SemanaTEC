
"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *
import time
import turtle
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
spd = 1000


def select():  # Imprime el letrero que le indica al jugador cómo cambiar la velocidad
    w = turtle.Turtle()
    w.color('Blue')
    style = ('Courier', 20, 'bold')  # Definiendo el estilo del texto
    w.hideturtle()
    # Dibujando el rectángulo
    w.penup()
    w.goto(-250, -100)
    w.pendown()
    w.begin_fill()
    for count in range(2):
        w.forward(1500 - 1000)
        w.left(90)
        w.forward(400 - 200)
        w.left(90)
    w.end_fill()
    # Escribiendo el texto
    w.color('White')
    w.penup()
    w.goto(250, 40)
    w.pendown()
    w.write('Cambiar velocidad: (presiona) ', font=style, align='right', move=False)
    w.penup()
    w.goto(-80, 0)
    w.pendown()
    w.write('B para baja', font=style, align='left', move=False)
    w.penup()
    w.goto(-80, -40)
    w.pendown()
    w.write('M para media', font=style, align='left', move=False)
    w.penup()
    w.goto(-80, -80)
    w.pendown()
    w.write('A para alta', font=style, align='left', move=False)
    time.sleep(4)
    w.clear()


def baja():  # Cambia el valor de la variable global spd para configurar velocidad baja
    global spd
    spd = 150
    print("Velocidad: Baja")


def media():  # Cambia el valor de la variable global spd para configurar velocidad media
    global spd
    spd = 80
    print("Velocidad: Media")


def alta():  # Cambia el valor de la variable global spd para configurar velocidad alta
    global spd
    spd = 20
    print("Velocidad: Alta")


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def snack(x, y):
    global food
    food.x = randrange(-10, 10)*5
    food.y = randrange(-10, 10)*5


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    if head.x == 190:  # Tomando en cuenta los límites si la cabeza de la serpiente
        change(0, -20)  # Llega a los límites se mueve dos espacios hacía cualquier lado y/o atrás
        change(-10, 0)

    if head.y == -200:
        change(-20, 0)
        change(0, 10)

    if head.x == -200:
        change(0, 20)
        change(10, 0)
        
    if head.y == 200:
        change(20, 0)
        change(0, -10)

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, spd)  # Estableciendo el valor de la velocidad al elegido por el usuario


def store(key, value):
    """"Store value in state at key."""
    state[key] = value


select()
state = {'start': None, 'speed': media}
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onscreenclick(snack)
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
# Guardando los valores de las teclas a utilizar para cambiar la velocidad
onkey(lambda: store('speed', baja), 'B')
onkey(lambda: store('speed', media), 'M')
onkey(lambda: store('speed', alta), 'A')
# Llamando con las teclas a las funciones encargadas del cambio de velocidad
onkey(lambda: baja(), 'B')
onkey(lambda: media(), 'M')
onkey(lambda: alta(), 'A')
move()
done()

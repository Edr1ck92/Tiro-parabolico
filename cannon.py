"""Cannon, hitting targets with projectiles.

Exercises

1. Velocidad del balón y proyectil sean más rápidos-Iñaki
2. Que el juego nunca termine
"""

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 400) / 25 #Aquí se cambia la velocidad del proyectil
        speed.y = (y + 400) / 25


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:  
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5
        """Con este if hacemos que los circulos al llegar al lado izquierdo de la pantalla reaparezcan del lado derecho"""
        if target.x<-180:
            target.x=190
            target.y = randrange(-150, 150)
            

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()
    

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 10)
    """Aquí se le cambia la velocidad al proyectile y a los balones, entre más chico el valor más rápido y viceversa"""


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

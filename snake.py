import turtle
from turtle import Turtle, Screen
import time
screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
game_on = True
screen.tracer(0)

def snakes(name, x_start, y_start):
    name = Turtle('square')
    name.penup()
    name.color('white')
    name.speed('fastest')
    name.shapesize(1)
    name.goto(x_start, y_start)
    return name


s1 = snakes('s1', 0, 0)
s2 = snakes('s2', -20, 0)
s3 = snakes('s3', -40, 0)

s = [s1, s2, s3]
while game_on:
    screen.update()
    time.sleep(.1)
    for i in range(len(s) - 1, 0, -1):
        new_x = s[i - 1].xcor()
        new_y = s[i - 1].ycor()
        s[i].goto(new_x, new_y)
    s[0].forward(20)
    s[0].left(90)




screen.exitonclick()


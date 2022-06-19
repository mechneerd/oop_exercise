import turtle
import random
from turtle import Turtle, Screen
color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

t = Turtle()
t.speed('fastest')
t.penup()
number_of_dots = 100
turtle.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.penup()
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)
t.hideturtle()








screen = Screen()
screen.exitonclick()
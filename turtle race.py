from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(prompt="Which colour turtle do you think will win ?", title="Make a bet")
screen.bgcolor('black')

if user_choice:
    race_on = True


def turtles(color_name, x_start, y_start):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.color(color_name)
    turtle.goto(x_start, y_start)
    return turtle


p1 = turtles('red', x_start=-230, y_start=-90)
p2 = turtles('blue', x_start=-230, y_start=-60)
p3 = turtles('green', x_start=-230, y_start=-30)
p4 = turtles('yellow', x_start=-230, y_start=0)
p5 = turtles('purple', x_start=-230, y_start=30)
p6 = turtles('orange', x_start=-230, y_start=60)

turtles_list = [p1, p2, p3, p4, p5, p6]
while race_on:
    for i in turtles_list:
        if i.xcor() != 230:
            i.forward(random.randint(0, 1))
        else:
            if user_choice == i.pencolor():
                print(f'You won ,The winner is {i.pencolor()}')
            else:
                print(f'You lost ,The winner is {i.pencolor()}')
            race_on = False

screen.bye()

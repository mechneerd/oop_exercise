import turtle
from turtle import Screen



t = turtle.Turtle()
s = Screen()
def forward():
    t.forward(20)
def backward():
    t.backward(20)
def clockwise():
    new_head = t.heading() - 10
    t.setheading(new_head)
def counter_clockwise():
    new_head = t.heading() + 10
    t.setheading(new_head)
def clear():
    s.resetscreen()

s.listen()
s.onkey(fun=forward, key="w")
s.onkey(fun=backward, key="s")
s.onkey(fun=clockwise, key="d")
s.onkey(fun=counter_clockwise, key="a")
s.onkey(fun=clear, key="c")





s.exitonclick()
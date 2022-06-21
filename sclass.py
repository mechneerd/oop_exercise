import turtle
from turtle import Turtle


position = [(0, 0), (-20, 0), (-40, 0)]
distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.build_snake()
        self.head = self.snakes[0]

    def build_snake(self):
        for pos in position:
            self.full_snake(pos)

    def full_snake(self, pos):
        name = Turtle('square')
        name.penup()
        name.color('white')
        name.speed(1)
        name.shapesize(1)
        name.goto(pos)
        self.snakes.append(name)

    def extend(self):
        self.full_snake(self.snakes[-1].pos())

    def mv(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].forward(distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)





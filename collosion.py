from turtle import Turtle
from snake import Snake


class Impact(Snake):

    def __init__(self):
        super().__init__()
        self.head.xcor()
        self.head.ycor()

    def check_pos(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x == -300 or 300:
            self.write('GAME OVER')


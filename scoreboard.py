from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.board_update()
        self.hideturtle()

    def board_update(self):
        self.write(f'Score : {self.score}', align='center', font=('Aerial', 10, 'normal'))

    def score_update(self):
        self.score += 1
        self.clear()
        self.board_update()



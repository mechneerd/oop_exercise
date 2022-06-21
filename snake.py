from turtle import Turtle, Screen
import time
from sclass import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True
screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
#Todo move the snake
screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='d', fun=snake.right)

while game_on:
    screen.update()
    time.sleep(.1)
    snake.mv()
    # to check distance from food to head of the snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_update()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    #todo find if snake colloide itself
    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()


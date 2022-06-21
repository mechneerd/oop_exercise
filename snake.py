import turtle
from turtle import Turtle, Screen
import time
from sclass import Snake
from food import Food


screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
game_on = True
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key='w',fun=snake.up)
screen.onkey(key='s',fun=snake.down)
screen.onkey(key='a',fun=snake.left)
screen.onkey(key='d',fun=snake.right)


while game_on:
    screen.update()
    time.sleep(.1)
    snake.mv()
    # to check distance from food to head of the snake
    if snake.head.distance(food) < 15:
        food.refresh()






screen.exitonclick()


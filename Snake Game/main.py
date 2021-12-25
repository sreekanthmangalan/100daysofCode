from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake_in_the_game = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake_in_the_game.up, "Up")
screen.onkey(snake_in_the_game.down, "Down")
screen.onkey(snake_in_the_game.left, "Left")
screen.onkey(snake_in_the_game.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake_in_the_game.move()

# detect collision with food
    if snake_in_the_game.head.distance(food) < 15:
        food.refresh()
        snake_in_the_game.extend()
        scoreboard.increase_score()

# Detect collision with wall
    if snake_in_the_game.head.xcor() > 280 or snake_in_the_game.head.xcor() < -280 or \
            snake_in_the_game.head.ycor() > 280 or snake_in_the_game.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

# Detect Collision with tail
    for part in snake_in_the_game.snake[1:]:
        if snake_in_the_game.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
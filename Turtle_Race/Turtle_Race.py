from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race among \nred,orange,yellow,"
                                                          "green,blue,purple?:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_name = ["turt1", "turt2", "turt3", "turt4", "turt5", "turt6"]
y_positions = [-70, -40, -10, 20, 50, 80]
for turt_index in range(0, 6):
    turtle_name[turt_index] = Turtle(shape="turtle")
    turtle_name[turt_index].color(colors[turt_index])
    turtle_name[turt_index].penup()
    turtle_name[turt_index].goto(-230, y_positions[turt_index])

if user_bet:
    is_race_on = True

while is_race_on:

    for turtles in turtle_name:
        if turtles.xcor() > 210:
            is_race_on = False
            winning_turtle = turtles.pencolor()
            if winning_turtle == user_bet:
                print("Congrats! You won the bet")
            else:
                print(f"You lose.{winning_turtle} won")

        rand_distances = random.randint(0, 15)
        turtles.forward(rand_distances)

screen.exitonclick()
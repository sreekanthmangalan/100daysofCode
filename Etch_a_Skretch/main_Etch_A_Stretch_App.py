from turtle import Turtle, Screen

turt = Turtle()
screen = Screen()


def move_forward():
    turt.forward(10)


def move_backward():
    turt.backward(10)


def turn_left():
    new_heading = turt.heading() + 10
    turt.setheading(new_heading)


def turn_right():
    new_heading = turt.heading() - 10
    turt.setheading(new_heading)


def clear_screen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
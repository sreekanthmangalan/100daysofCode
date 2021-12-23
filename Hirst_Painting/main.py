from turtle import Turtle, Screen, colormode
import random
# import colorgram

turt = Turtle()

# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
colormode(255)
color_list = [(57, 106, 148), (224, 200, 110), (133, 85, 59), (222, 141, 65), (195, 145, 171), (234, 225, 203), (144, 179, 203), (224, 233, 230), (138, 82, 106), (209, 91, 68), (134, 182, 136), (187, 79, 121), (69, 104, 89), (236, 222, 230), (65, 155, 89), (133, 133, 75), (49, 155, 194), (183, 192, 201), (213, 178, 191), (22, 68, 111), (21, 59, 94), (226, 176, 168), (174, 202, 182), (115, 124, 149), (156, 207, 216), (70, 59, 48), (72, 64, 53), (119, 46, 42), (107, 48, 59)]

turt.hideturtle()
turt.speed("fastest")
turt.setheading(225)
turt.penup()
turt.forward(300)
turt.setheading(0)

for _ in range(10):
    for _ in range(10):
        turt.dot(20, random.choice(color_list))
        turt.forward(50)
    turt.left(90)
    turt.forward(50)
    turt.left(90)
    turt.forward(500)
    turt.setheading(360)

screen = Screen()
screen.exitonclick()

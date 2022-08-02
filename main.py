# import colorgram
#
# colorgram_output = colorgram.extract("image.jpg", 35)
# rgb_colors = []
# for color_object in colorgram_output:
#     # rgb_named_tuple = color_object.rgb
#     # rgb_named_tuple is a named tuple hence we can use both ways
#     # r = rgb_named_tuple[0] = rgb_named_tuple.r
#     r = color_object.rgb.r
#     g = color_object.rgb.g
#     b = color_object.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(42, 2, 176), (81, 252, 177), (224, 151, 110), (154, 3, 85), (5, 210, 101), (4, 138, 60), (244, 42, 125), (109, 108, 245), (251, 252, 56), (184, 184, 250), (210, 106, 6), (175, 113, 246), (35, 35, 251), (139, 1, 0), (251, 37, 35), (51, 239, 57), (222, 115, 158), (16, 127, 143), (86, 249, 252), (185, 43, 107), (22, 5, 103), (10, 209, 214), (97, 7, 50), (228, 165, 206), (104, 7, 4), (206, 119, 31), (10, 112, 26), (235, 166, 164), (14, 107, 110), (243, 13, 23)]

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.setposition(-200, -200)

t.colormode(255)


def random_color():
    color = random.choice(color_list)
    return color

for row in range(10):
    for column in range(10):
        tim.dot(20, random_color())
        tim.forward(50)
    tim.speed('fastest')
    tim.penup()
    if row != 9:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.right(180)
        tim.speed('normal')
tim.hideturtle()

























screen = t.Screen()
screen.exitonclick()


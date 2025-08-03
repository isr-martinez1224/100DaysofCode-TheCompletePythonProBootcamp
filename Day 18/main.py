# import turtle
# tim = turtle.Turtle()
#
# from turtle import Turtle
#
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
# for x in range(31):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# Shape drawings
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for x in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


# Random Walk
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color

# Random lines
# angles = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")
# for x in range(250):
#     tim.color(random_color())
#     tim.setheading(random.choice(angles))
#     tim.forward(50)

#Spirograph
# circles, radius of 100, must rotate and come back to beginning
# random colors each time

tim.speed("fastest")
for angle in range(0, 360, 5):
    tim.setheading(angle)
    tim.color(random_color())
    tim.circle(100)



screen = Screen()
screen.exitonclick()


# import heroes
# print(heroes.gen())
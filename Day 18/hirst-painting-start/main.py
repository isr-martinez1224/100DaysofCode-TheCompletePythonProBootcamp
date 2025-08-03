###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
from turtle import Screen
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r #from color object
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

#10 x 10 dots, size 20, spaced out by 50
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tom = t.Turtle()

#set up painting inside minimized window
tom.penup()
tom.setheading(220)
tom.forward(300)
#print(tom.pos())
begin_x = tom.xcor()
tom.setheading(0)

t.colormode(255)

tom.speed("fastest")
for x in range(10):
    for y in range(10):
        #tom.color(random.choice(color_list))
        tom.pendown()
        tom.dot(20, random.choice(color_list))
        tom.penup()
        tom.forward(50)
    tom.setx(begin_x)
    tom.sety(tom.ycor() + 50)


screen = Screen()
screen.exitonclick()
import colorgram
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()

pos_x = -295
pos_y = -250
turtle.teleport(pos_x, pos_y)
turtle.speed("fastest")

# extracting colours from original image
colors = colorgram.extract("original_image_for_colour_extraction.jpg", 84)
color_list = []
# for reference colours come out as color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

for i in range(1, 101):
    color = random.choice(color_list)
    turtle.dot(20, color)
    turtle.fd(60)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.fd(60)
        pos_y += 60
        turtle.teleport(pos_x, pos_y)
        turtle.setheading(0)

screen.exitonclick()

# from turtle import *
# import turtle
# import random

# tur = turtle.Turtle()

# 1


# def prob1():
#     for i in range(4):
#         forward(100)
#         left(90)


# prob1()

# 2


# def prob2():
#     for j in range(100):
#         tur.forward(10)
#         tur.penup()
#         tur.forward(1)
#         tur.pendown()


# # prob2()
# 3
# color = ["red", "blue", "grey", "black", "brown", "yellow", "orange"]


# def prob3(n):
#     for i in range(n):
#         forward(100)
#         right(360 / n)


# for i in range(3, 11):
#     pencolor(random.choice(color))
#     # prob3(i)

# 4
# directions = [-1, 1]
# color = ["red", "blue", "grey", "black", "brown", "yellow", "orange"]
# speed(10)


# def prob4(n):
#     for i in range(n):
#         forward(10)
#         pencolor(random.choice(color))
#         right(random.choice(directions) * 90)


# # prob4(100)

# 5
# import turtle as tt

# tt.bgcolor("black")
# tt.pensize(2)
# tt.speed(100)


# def prob5():
#     for i in range(6):
#         for color in ("red", "magenta", "blue", "cyan", "green", "white", "yellow"):
#             tt.color(color)

#             tt.circle(100)

#             tt.left(10)

#         tt.hideturtle()


# prob5()

# 6
import colorgram
import turtle as turtle_module
import random


colors = colorgram.extract("img.jpg", 25)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

turtle_module.colormode(255)


tim = turtle_module.Turtle()


tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 25
dot_size = 100
dot_distance = 150
row_distance = 200
column_distance = 150
x = -column_distance * 2
y = row_distance * 2

for dot_count in range(number_of_dots):
    tim.goto(x, y)
    tim.dot(dot_size, random.choice(color_list))
    x += column_distance
    if (dot_count + 1) % 5 == 0:
        x = -column_distance * 2
        y -= row_distance

screen = turtle_module.Screen()
screen.exitonclick()

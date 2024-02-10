import random
from turtle import Turtle, Screen


def draw_pic(y_position):
    tim_turtle.penup()
    tim_turtle.setposition(-250, y_position)
    for num in range(10):
        color = random.choice(color_list)
        tim_turtle.dot(20, color)
        tim_turtle.forward(50)


color_list = [
    (196, 155, 116),
    (130, 88, 65),
    (178, 46, 86),
    (21, 112, 174),
    (217, 6, 25),
    (42, 191, 98),
    (243, 220, 83),
    (35, 140, 54),
    (9, 47, 134),
    (236, 48, 77),
    (141, 220, 202),
    (112, 166, 213),
    (221, 112, 144),
    (247, 86, 31),
    (4, 190, 221),
    (4, 57, 102)
]

tim_turtle = Turtle()
tim_turtle.speed('fastest')
tim_turtle.hideturtle()
my_screen = Screen()
my_screen.colormode(255)
y_pos = -200
for times in range(10):
    draw_pic(y_pos)
    y_pos += 50

my_screen.exitonclick()

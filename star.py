from turtle import Turtle, Screen
import random

def star(t, length):
    t.down()
    for _ in range(5):
        t.forward(length)
        t.right(144)
    t.up()

def pattern(t, radius, length, shape, num):
    angle = 360 / num
    for i in range(num):
        t.up()
        current_angle = i * angle
        t.right(current_angle)
        t.forward(radius)
        t.left(current_angle)
        t.down()
        t.color(random_color())
        shape(t, length)
        t.up()
        t.home()

def random_color():
    return (random.random(), random.random(), random.random())

screen = Screen()
screen.colormode(1.0)

num = int(input("Enter the number of stars: "))
length = int(input("Enter the length of the sides of the star: "))
radius = 2 * length
t = Turtle()
t.speed(1)
pattern(t, radius, length, star, num)

screen.mainloop()

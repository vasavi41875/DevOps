import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Pink Heart Art")

# Turtle setup
t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.pensize(1)
t.color("Red")

# Draw heart
for i in range(120):
    t.penup()
    t.goto(0, 40)

    angle = i * (math.pi * 2) / 120     

    x = 16 * (math.sin(angle) ** 3) * 15

    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 15

    t.pendown()
    t.goto(x, y)

    # Draw small flower/star at each point
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()
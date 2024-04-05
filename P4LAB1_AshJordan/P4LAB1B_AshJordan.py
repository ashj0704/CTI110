# Jordan Ash

# 4/03/2024

# P4LAB1B

# Using turtle graphics to draw initials.

import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(2)  # Set the drawing speed
t.pensize(3)  # Set the pen size
t.color("blue")  # Set the pen color

# Draw the first initial (E)
t.penup()
t.goto(-100, 0)
t.pendown()
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.penup()
t.goto(-100, 50)
t.pendown()
t.forward(50)
t.penup()
t.goto(-100, 0)
t.pendown()
t.forward(50)

# Draw the letter A
t.penup()
t.goto(-50, 0)
t.pendown()
t.left(75)
t.forward(150)
t.right(150)
t.forward(150)
t.backward(75)
t.right(105)
t.forward(50)

# Keep the window open until it's closed by the user
turtle.done()

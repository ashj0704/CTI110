# Jordan Ash

# 4/03/2024

# P4LAB1

# Using turtle graphics to create shapes.



import turtle

t = turtle.Turtle()
t.speed(2)  

side_length = 100
angle = 90
num_sides = 4

print("Drawing a square...")
sides_drawn = 0
while sides_drawn < num_sides:
    t.forward(side_length)
    t.right(angle)
    sides_drawn += 1

t.penup()
t.goto(0, -150)
t.pendown()

side_length = 100
angle = 120 
num_sides = 3

print("Drawing a triangle...")
sides_drawn = 0
while sides_drawn < num_sides:
    t.forward(side_length)
    t.left(angle)
    sides_drawn += 1

turtle.done()

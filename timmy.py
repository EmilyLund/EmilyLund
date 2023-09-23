import turtle
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def square(timmy, size, fill, border):
    timmy.fillcolor(fill)
    timmy.pencolor(border)
    timmy.begin_fill()
    for sides in range(4):
        timmy.forward(size)
        timmy.left(90)
    timmy.end_fill()

def triangle(timmy, size, fill, border):
    timmy.fillcolor(fill)
    timmy.pencolor(border)
    timmy.begin_fill()
    for sides in range(3):
        timmy.forward(size)
        timmy.left(120)
    timmy.end_fill()
    
def pentagon(timmy, size, fill, border):
    timmy.fillcolor(fill)
    timmy.pencolor(border)
    timmy.begin_fill()
    for sides in range(5):
        timmy.forward(size)
        timmy.left(72)
    timmy.end_fill()
    
def circle(timmy, radius, fill, border):
    timmy.fillcolor(fill)
    timmy.pencolor(border)
    timmy.begin_fill()
    timmy.circle(radius)
    timmy.end_fill()
    
def move(timmy, x, y):
    timmy.up()
    timmy.goto(x, y)
    timmy.down()

timmy = turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor(236, 255, 220)
timmy.shape('turtle')
timmy.speed(10)

count = 0
while True:
    i = random.randint(-300,300)
    j = random.randint(-300,300)
    move(timmy, i, j)
    radius = random.randint(10,75)
    fill = random_color()
    border = random_color()
    circle(timmy, radius, fill, border)
    count += 1
    if count > 4:
        break

for shape1 in range(5):
    i = random.randint(-300,300)
    j = random.randint(-300,300)
    move(timmy, i, j)
    size = random.randint(20,175)
    fill = random_color()
    border = random_color()
    square(timmy, size, fill, border)

count = 0
while count <= 5:
    i = random.randint(-300,300)
    j = random.randint(-300,300)
    move(timmy, i, j)
    size = random.randint(15,125)
    fill = random_color()
    border = random_color()
    pentagon(timmy, size, fill, border)
    count += 1
    
for shape2 in range(5):
    i = random.randint(-300,300)
    j = random.randint(-300,300)
    move(timmy, i, j)
    size = random.randint(20,150)
    fill = random_color()
    border = random_color()
    triangle(timmy, size, fill, border)

turtle.done()
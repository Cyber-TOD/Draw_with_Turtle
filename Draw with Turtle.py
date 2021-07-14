import turtle

t = turtle.Pen()
s = turtle.Screen()
t.shape('turtle')
t.speed(0)

def pendown():
    t.pendown()

def penup():
    t.penup()


def draw_circle():
    t.circle(50)

def draw_rectangle():
    for x in range(2):
        t.forward(100)
        t.left(90)
        t.forward(200)
        t.left(90)

def draw_triangle():
    for x in range(3):
        t.forward(100)
        t.left(120)

def draw_square():
    for x in range(4):
        t.forward(100)
        t.left(90)

def draw_star():
    for i in range(5):
        t.forward(200)
        t.left(144)

def draw_pentagon():
    for x in range(5):
        t.forward(100)
        t.left(72)

def draw_hexagon():
    for x in range(6):
        t.forward(100)
        t.left(60)

def draw_heptagon():
    for x in range(7):
        t.forward(100)
        t.left(51.42)

def draw_octagon():
    for x in range(8):
        t.forward(100)
        t.left(45)

def draw_nonagon():
    for x in range(9):
        t.forward(100)
        t.left(40)

def draw_decagon():
    for x in range(10):
        t.forward(100)
        t.left(36)

def penSize():
    t.pensize(1)

def penSize2():
    t.pensize(2)

def penSize3():
    t.pensize(3)

def penSize4():
    t.pensize(4)

def penSize5():
    t.pensize(5)

def penSize6():
    t.pensize(6)

def penSize7():
    t.pensize(7)

def penSize8():
    t.pensize(8)

def penSize9():
    t.pensize(9)

def moveForward():
    t.forward(10)
    
def moveBackward():
    t.backward(10)

def turnLeft():
    t.left(10)

def turnRight():
    t.right(10)    

s.onkey(moveForward, 'w')
s.onkey(moveBackward, 's')
s.onkey(turnLeft, 'a')
s.onkey(turnRight, 'd')
s.onkey(penSize, '1')
s.onkey(penSize2, '2')
s.onkey(penSize3, '3')
s.onkey(penSize4, '4')
s.onkey(penSize5, '5')
s.onkey(penSize6, '6')
s.onkey(penSize7, '7')
s.onkey(penSize8, '8')
s.onkey(penSize9, '9')
s.onkey(draw_circle, 'C')
s.onkey(draw_triangle, 'T')
s.onkey(draw_star, 'A')
s.onkey(draw_square, 'S')
s.onkey(draw_rectangle, 'R')
s.onkey(draw_pentagon, 'P')
s.onkey(draw_hexagon, 'h')
s.onkey(draw_heptagon, 'H')
s.onkey(draw_octagon, 'O')
s.onkey(draw_nonagon, 'N')
s.onkey(draw_decagon, 'D')
s.onkey(pendown, 'Down')
s.onkey(penup, 'Up')
s.listen()

turtle.done()

import turtle

def edasi_parem(pikkus, nurk):
    turtle.forward(pikkus)
    turtle.right(nurk)

def edasi_vasak(pikkus, nurk):
    turtle.forward(pikkus)
    turtle.left(nurk)


def kujund3():
    for i in range(4):
        edasi_parem(150, 90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    for i in range(3):
        edasi_vasak(150, 90)
    turtle.forward(110)

def kujund5():
    for i in range(6):
        edasi_vasak(100, 60)
    turtle.left(60)
    turtle.forward(200)
    turtle.left(180)
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(200)
    turtle.left(180)
    turtle.forward(100)
    turtle.right(60)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(200)

kujund3()
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
kujund5()

turtle.done()

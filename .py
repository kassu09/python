import turtle
import random

skoor = 0

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.setheading(random.randint(0, 360))

# kiirused
ristkyliku_kiirus = 20
kiirus = 10

# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
    global skoor
    nurk = ring.heading
    if ring.xcor() >= 300 or ring.xcor() <= -300:
        uus_nurk = 180 - nurk
        if uus_nurk < 0:
            uus_nurk += 360
        ring.setheading(uus_nurk)
    if ring.ycor() <= -300:
        print("Game over")
        turtle.bye
x = ristkylik.xcor()
y = ristkylik.ycor()
if (y + 10 >= ring.ycor() and ring.ycor() >= y- 10) and (x + 50 >=)
skoor+=1
turtle.hideturtle()
turtle.clear()
turtle.penup()
turtle.goto(-250,200)
turtle.pendown()
turtle.write(skoor)
print("Skoor:",skoor)
uus_nurk = 360 - nurk

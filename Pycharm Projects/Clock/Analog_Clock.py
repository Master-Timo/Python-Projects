import turtle
import time

wn = turtle.Screen()
wn.bgcolor("#11001F")
wn.setup(width=500, height=500)
wn.title("Analog Clock")
wn.tracer(0)

# drawing the pen

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.turtlesize(50)



def draw_clock(h, m, s, pen):
    #  draw clock face

    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    # draw time stamp lines
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # draw clock hands

    # hour hand

    pen.turtlesize(20)
    pen.up()
    pen.goto(0, 0)
    pen.color("yellow")
    pen.setheading(90)
    angle = (h/12) * 360
    pen.right(angle)
    pen.pendown()
    pen.forward(130)

    # minute hand

    pen.turtlesize(20)
    pen.up()
    pen.goto(0, 0)
    pen.color("orange")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.right(angle)
    pen.pendown()
    pen.forward(160)

    # seconds hand

    pen.up()
    pen.goto(0, 0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.right(angle)
    pen.pendown()
    pen.forward(100)



while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)

    pen.clear()


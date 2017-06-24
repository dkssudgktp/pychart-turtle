import turtle
import math
from math import acos, degrees

border = 10
length = 80
befornum = 0;

def getPita(a,b,c):
    return round(degrees(acos((b*b+c*c-a*a)/(float(2*b*c)))))


def getsize(x,y):
    return round(math.sqrt((y*y)+(x*x)))


def setXY(x,y):
    tess.penup()
    tess.setx(x)
    tess.sety(y)
    tess.pendown()

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def drawBroken(t, height):
    global befornum
    global length

    if befornum == 0:
        t.write("0")

    line = getsize(length,height - befornum)

    if (height - befornum)>0:
        t.setheading(getPita(height - befornum,line,length))
    else:
        t.setheading(-getPita(height - befornum,line,length))
    t.forward(line/2)
    t.write(str(height))
    befornum = height;
    t.end_fill()

def chart(a, b):
    numbars = len(b)
    maxheight = max(b)

    wn = turtle.Screen()
    wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)
    if a == 0:
        for i in b:
            drawBar(tess,i)
        wn.exitonclick()
    if a == 1:
        for i in b:
            drawBroken(tess, i)
        wn.exitonclick()

value1 = input("select graph (0~1)[0:barchar],[1:graph of broken lines]: ")
print("input value ex) 100 200 300: ")
value2 = list(map(int, input().split()))
chart(int(value1),value2)

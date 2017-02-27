import turtle
from turtle import *
bgcolor("green")
color("pink")

def draw(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

tess=turtle.Turtle()
tess.pensize(2)
tess.color("pink")

draw(tess,8,50)

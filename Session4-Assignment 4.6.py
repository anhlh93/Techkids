from turtle import *
bgcolor("green")
color("pink")
speed(-1)
def draw_poly(number, sz):
    for i in range(number):
        forward(sz)
        left(360/number)
def draw_equitriangle(t, sz):
    draw_poly(t,sz)
draw_equitriangle(3,50)

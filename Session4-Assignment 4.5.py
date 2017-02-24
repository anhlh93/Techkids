from turtle import *
bgcolor("green")
color("blue")
speed(-1)
def square(times, length):
    right(90)    
    for i in range (times*4):
        forward(length)
        left(90)
        length = length +3       
square(10,10)


def square(times, length):
    right(90)    
    for i in range (times*4):
        forward(length)
        left(95)
        length = length +3       
square(10,10)       

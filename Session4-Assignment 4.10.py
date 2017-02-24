from turtle import *
speed(-1)
def star(t):
    for i in range(5):
        forward(t)
        right(144)
for i in range(5):
    star(100)
    up()
    forward(350)
    right(144)
    down()

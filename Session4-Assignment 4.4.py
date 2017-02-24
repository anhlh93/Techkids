from turtle import*
color("blue")
bgcolor("green")
speed(-1)

def square(length):
    for i in range(4):
        forward(length)
        left(90)

number=20
length=100
for i in range(number):
    square(length)
    left(360/number)

from turtle import*
color("pink")
bgcolor("green")
pensize(5)

def square(length):
    for i in range(4):
        forward(length)
        left(90)
    
quantity=5
length=20

for i in range(quantity):
    square(length)
    up()
    setposition(length*(2*(i+1)),0)
    down()

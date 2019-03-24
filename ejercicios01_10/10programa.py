
import turtle

miT = turtle.Turtle()

def cuadrado(lado):
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    
    return lado*lado

miT = turtle.Turtle()
area01 = cuadrado(25)
miT.left(90)

area02 = cuadrado(50)
miT.left(90)

area03 = cuadrado(75)
miT.left(90)

area04 = cuadrado(100)
miT.left(90)


import turtle

miT = turtle.Turtle()

def cuadrado2(lado):
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    miT.forward(lado)
    miT.left(90)
    
    
    
    return lado*lado

miT = turtle.Turtle()
area01 = cuadrado2(25)
miT.left(90)

area02 = cuadrado(50)
miT.left(90)

area03 = cuadrado(75)
miT.left(90)

area04 = cuadrado(100)
miT.left(90)
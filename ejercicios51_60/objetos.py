import turtle

donatello = turtle.Turtle()
leonardo = turtle.Turtle()
raphael = turtle.Turtle()


donatello.shape('turtle')
donatello.color('purple')
donatello.fd(50)

leonardo.shape('turtle')
leonardo.color('blue')
leonardo.left(90)
leonardo.fd(50)

raphael.shape('turtle')
raphael.color('red')
raphael.speed(1)
raphael.lt(180) # lt : girar a la izquierda
raphael.fd(150) # fd : avanzar

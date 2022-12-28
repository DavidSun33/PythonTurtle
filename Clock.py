
import turtle

number = 0

turtle.width(2)
turtle.left(90)

for i in range(12):
    number += 1
    turtle.right(30)
    turtle.penup()
    turtle.forward(70)
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(20)
    turtle.write(str(number), align = "center", font = ("Arial", 10))
    turtle.backward(95)
    turtle.pendown()

turtle.penup()
turtle.right(90)
turtle.forward(135)
turtle.left(90)


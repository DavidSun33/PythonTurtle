import turtle as t

t.speed(0)
t.bgcolor("black")

angle = 122
for i in range(1000):
	t.pencolor("red")
	t.fd(300 - 2 * i)
	t.rt(angle)
	t.pencolor("yellow")
	t.fd(300 - 2 * i)
	t.rt(angle)

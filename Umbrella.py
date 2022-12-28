import turtle as t

t.bgcolor("black")
t.pensize(5)
radius = 200
angle = 45


def umbrella_part(radius, angle, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(radius)
  t.right(90 + angle)
  t.circle(radius, angle)
  t.right(90 + angle)
  t.forward(radius)
  t.end_fill()


for i in range(4):
  umbrella_part(radius, angle, "red")
  umbrella_part(radius, angle, "white")

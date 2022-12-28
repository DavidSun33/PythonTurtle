import turtle as t
t.penup()
t.goto(250,0)
t.rt(180)
t.pendown()
def Petal():
  t.fillcolor("dark green")
  t.begin_fill()
  t.circle(50,90)
  t.lt(90)
  t.end_fill()
for i in range(5):
  t.fd(50)
  for j in range(3):
    for i in range(2):
      Petal()
    t.rt(15)
  t.lt(35)
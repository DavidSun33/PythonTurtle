import turtle as t
t.pensize(10)
t.pencolor("green")
def petal():
  t.lt(45)
  t.fd(100)
  t.lt(180)
  t.circle(30,-180)
  t.rt(220)
  t.circle(30,-180)
  t.rt(20)
  t.backward(120)

for i in range(4):
  petal()
  t.rt(75)

t.rt(75)
t.fd(200)
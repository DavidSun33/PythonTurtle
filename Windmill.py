import turtle as t


def Wind_Quarter():
  t.fillcolor("red")
  t.begin_fill()
  t.forward(100)
  t.lt(90)
  t.forward(100)
  t.lt(135)
  t.fd(140)
  t.rt(135)
  t.end_fill()
  t.fillcolor("red")
  t.begin_fill()
  t.fd(75)
  t.rt(90)
  t.fd(75)
  t.rt(135)
  t.fd(107)
  t.end_fill()
  t.rt(135)
for i in range (4):
  Wind_Quarter()
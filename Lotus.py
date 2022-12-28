import turtle as t

def Petal():
  t.fillcolor("dark green")
  t.begin_fill()
  t.circle(50,90)
  t.lt(90)
  t.end_fill()
t.rt(60)
t.pencolor("light green")
for i in range (5):
  for j in range (2):
    Petal()
  t.lt(45)
t.lt(90)
t.circle(200,60)
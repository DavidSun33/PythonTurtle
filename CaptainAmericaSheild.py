import turtle as t
def star(color,starsize,x,y):
  t.goto(x-starsize/2,y+starsize/5)
  t.pencolor(color)
  t.fillcolor(color)
  t.begin_fill()
  for i in range(5):
    t.st()
    t.fd(starsize)
    t.rt(144)
  t.end_fill()
  t.fd(starsize/2+starsize/8)
  t.pencolor(color)
  t.fillcolor(color)
  t.begin_fill()
  for i in range(4):
    t.rt(72)
    t.fd(starsize/4)
  t.end_fill()
  
  
size=250

t.goto(0,-1*size)
t.ht()
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.circle(size)
t.end_fill()
size -= 50

t.goto(0,-1*size)
t.ht()
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(size)
t.end_fill()
size -= 50

t.goto(0,-1*size)
t.ht()
t.pencolor("red")
t.fillcolor("red")
t.begin_fill()
t.circle(size)
t.end_fill()
size -= 50

t.goto(0,-1*size)
t.ht()
t.pencolor("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(size)
t.end_fill()
size -= 50

star("white", 150,0,0)
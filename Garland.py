import turtle as t

def flower():
  for j in range (6):
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range (3):
      t.forward(10)
      t.rt(120)
    t.lt(60)
    t.end_fill()
  t.circle(40,35)
  
t.pencolor("red")
for k in range (10):
  flower()
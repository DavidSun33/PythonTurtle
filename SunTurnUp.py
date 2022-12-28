import turtle as t
t.bgcolor('#63C8DC')
print("repetitions     Y value (Every time it goes up by 10)")
s = t.Screen()
s.setup(600,600)
times=0
y=-200
x=0
d=0
t.hideturtle()
t.speed(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
def draw_sun():
  t.seth(0)
  t.pencolor("black")
  t.pu()
  t.goto(0,y)
  t.fillcolor("yellow")
  t.begin_fill()
  t.circle(30)
  t.end_fill()
  t.pu()
  t.goto(0,y+30)
  t.seth(d)
  for i in range(12):
    t.fd(50)
    t.pd()
    t.fd(20)
    t.pu()
    t.bk(70)
    t.lt(30)
for i in range(200):
  times+=1
  s.tracer(0)
  draw_sun()
  s.update()
  t.clear()
  y+=2
  x+=0
  d+=1
  t.goto(x,y)
  print(str(times)+"                "+str(y))
draw_sun()
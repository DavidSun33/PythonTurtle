import turtle as t

t.lt(90)
t.pu()

for i in range (1, 13):
  t.rt(30)
  t.fd(100)
  t.write(i)
  t.bk(100)

Hour = t.numinput("Hour Time please", "Hour Time gimme so I use")
for i in range(int(Hour)):
  t.rt(30)
t.pd()
t.pensize(5)
t.fd(40)
t.home()
t.lt(90)
Minute = t.numinput("Minute Time please", "Minute Time gimme so I use")
for i in range(int(Minute)):
  t.rt(6)

t.pd()
t.pensize(2)
t.fd(65)
t.home()
t.lt(90)
Seconds = t.numinput("Seconds Time please", "Seconds Time gimme so I use")
for i in range(int(Seconds)):
  t.rt(6)
t.pd()
t.pencolor("red")
t.pensize(1)
t.fd(75)
t.home()
t.lt(90)

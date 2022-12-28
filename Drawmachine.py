import turtle as t


def screensetup():
  s = t.getscreen()
  s.bgcolor('white')
  s.screensize(200, 200)


def dragging(x, y):
  t.ondrag(None)
  t.seth(t.towards(x, y))
  t.goto(x, y)
  t.ondrag(dragging)


screensetup()
dragging(0, 0)

import turtle
t=turtle.Pen()
for x in range(1,4):
	if x==1:
		t.penup()
	else:
		t.pendown()
	t.forward(150)
	t.left(120)
t.penup()
t.left(60)
t.forward(75)

t.pendown()
t.left(-60)
t.forward(75)
turtle.getscreen()._root.mainloop()
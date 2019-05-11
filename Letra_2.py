import turtle
t=turtle.Pen()

for x in range(1,4):
	if(x==3):
		t.penup()
	else:
		t.pendown()
	t.left(120)
	t.forward(200)

t.pendown()
t.left(180)
t.forward(50)
t.penup()
t.forward(150)
t.left(180)
t.pendown()
t.forward(50)
t.penup()
t.forward(100)

for x in range(1,4):
	if(x==3):
		t.penup()
	else:
		t.pendown()
	t.left(120)
	t.forward(100)

t.left(120)
t.forward(140)
t.right(120)
t.forward(40)
t.pendown()
t.left(120)
t.forward(40)
t.left(120)
t.forward(70)
t.left(120)
t.forward(70)
t.left(120)
t.forward(40)

turtle.getscreen()._root.mainloop()
import turtle
t=turtle.Pen()

def micuadrado(size):
	for x in range(1,27):
		t.forward(size)
		t.left(125)

micuadrado(80)
turtle.getscreen()._root.mainloop()
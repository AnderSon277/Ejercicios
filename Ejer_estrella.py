import turtle

t=turtle.Pen()

def par(tamano,lados):
	for x in range(n):
		t.forward(tamano)
		t.left(angulo)

def impar(tamano,lados):
	for x in range(1,(n+1)):
		t.forward(tamano)
		t.left(angulo)

n=int(input("Ingrese numero de lados de la estrella: "))
tamano=int(input("Ingrese el tamaño de la estrella: "))

if(n%2==0):
	angulo=(-360/n)+180
	par(tamano,n)
else:
	angulo=(-(360/n+180)*2)
	impar(tamano,n)
	
turtle.getscreen()._root.mainloop()

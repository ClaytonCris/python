import turtle
p = turtle.Pen()
p.speed(0)
turtle.bgcolor('black')


cores = ['red','yellow','blue','green']
for x in range(100):
    resto = x % 4
    cor = cores[resto]
    p.pencolor(cor)
    p.forward(x*5)
    p.left(92)

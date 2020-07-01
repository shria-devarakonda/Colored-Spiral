import turtle

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red']

t = turtle.Pen()

turtle.bgcolor('black')
turtle.speed(0)
# 0 is fastest

for x in range(500):
    t.pencolor(colors[x%6])
    t.forward(5 * x)
    t.left(118)
# modify these values and make cool stuff

turtle.mainloop()

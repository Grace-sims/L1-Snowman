import turtle as t

t.bgcolor ("#8adcff")

t.width (3)

t.speed (0)

t.color ("gray","white")
t.begin_fill ()
for x in range (36):
    t.forward (15)
    t.left(10)
t.end_fill ()

t.begin_fill ()
for x in range (36):
    t.forward (20)
    t.right(10)
t.end_fill ()

t.penup ()
t.goto (0,173)
t.pendown ()

t.begin_fill ()
for x in range (36):
    t.forward (10)
    t.left(10)
t.end_fill ()

t.penup ()
t.goto (30,223)
t.pendown ()

t.color ("black")
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.penup ()
t.goto (-25,223)
t.pendown ()

t.color ("black")
t.begin_fill ()
t.circle (10)
t.end_fill ()

t.penup ()
t.color ("red")
t.goto (-15,203)
t.pendown ()

t.begin_fill ()
t.setheading (270)
t.circle (20,180)
t.end_fill ()


t.mainloop ()
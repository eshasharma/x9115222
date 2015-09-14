from swampy.TurtleWorld import *
import math

print "-----------------------"
print "Exercise 4.2"
print "-----------------------"

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def polyline(t, n, length, angle):
    
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

flower(bob, 7, 80.0, 60.0)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

flower(bob, 10, 80.0, 80.0)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

flower(bob, 20, 140.0, 20.0)

die(bob)
world.canvas.dump()

wait_for_user()
import math

from swampy.TurtleWorld import *


def draw_pie(t, n, r):
    polypie(t, n, r)
    
    
def polypie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)


def isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
size = 100
draw_pie(bob, 5, size)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0
draw_pie(bob, 6, size)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0
draw_pie(bob, 7, size)

wait_for_user()

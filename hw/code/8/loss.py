import math
import math
import random
import sys

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random


def loss(x, y):
    n      = min(len(x), len(y)) #lengths should be equal
    losses = [ expLoss(i,xi,yi,n)
                 for i, (xi, yi)
                   in enumerate(zip(x,y)) ]
    return sum(losses)/n

def expLoss(i,x,y,n):
    return math.exp(loss1(i,x,y)/n)

def loss1(i,x,y):
    return (x - y) if better(i) == lt else (y - x)

def gt(x,y): return x > y
def lt(x,y): return x < y

def better(i):  return lt

def loss2(x, y):
    x,y    = objs(x), objs(y)
    n      = min(len(x), len(y)) #lengths should be equal
    losses = [ expLoss(i,xi,yi,n)
                 for i, (xi, yi)
                   in enumerate(zip(x,y)) ]
    return sum(losses) / n

def cdom(x, y):
   "x dominates y if it losses least"
   return x if loss2(x,y) < loss2(y,x) else y

def objs(x):
  "Returns the objectives inside x"
  return x.objectives # for example

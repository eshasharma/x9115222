import Model
import random 
from Model import *
from curses.ascii import CAN
import new

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class Kursawe(Model):
    def __init__(self):
        self.lo = -5
        self.hi=5
        self.candidate=[] 
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.n=3
   
    def candidates(self,i,direction,old):
        if (direction==True):
            old[i]=self.guess(i)
            new=old
        else : 
            new = [self.guess(x) for x in range(self.n)]
        return new 
    def f1(self,can):
        a,b,c = can
        def xy(x,y):
            return (-10*ee**((-0.2*sqrt(x*x + y*y))))
        return xy(can[0],can[1]) + xy(can[1],can[2])
    def f2(self,can):
        total=0
        for x in can :
            total+=(abs(x)**0.8) + (5*sin(x)**1)
        return total
    def guess(self,i):
        a= random.uniform(self.lo,self.hi)
        #print a
        return a 
    def objectives(self,can): 
        return self.f1(can),self.f2(can)
    def ok(self,can):
            flag=True
            return flag 
    def neighbour(self,point):
        i=random.randrange(0,2,1)
        value= self.candidates(i,True,point)
        return value
       
    
    def normalise_val(self):
        for i in range(1,101):
            var=self.candidates(0,False,0)
            f1,f2=self.objectives(var) 
            en=f1+f2
            if (en>self.emax):
                self.emax=en
            if (en<self.emin):
                self.emin=en
        #print self.emin, self.emax
        return self.emin, self.emax  
    
    def Energy(self,can,emax,emin):
       norm_energy =  (float)((sum(self.objectives(can)) - emin) / (emax- emin)) 
       return norm_energy
import Model 
from Model import *
import math 
import random 

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class Schaffer(Model):
    def __init__(self):
        self.lo = -10**5
        self.hi=10**5
        self.emin = 0.0
        self.emax = 1.0
        self.candidate=0.0
        self.n=1
        
      
    def f1(self,x):
        return (x**2)
    
    def f2(self,x):
        return (x-2)**2
    
    def guess(self):
        return (random.randrange(self.lo,self.hi,1))
    
    def candidates(self,i,direction,old): 
        candidate= self.guess()
        return (candidate)
    
    def objectives(self,can): 
        return self.f1(can),self.f2(can)
    
    def ok(self,can):
        return True
     
    def neighbour(self,point):
        #value=(float)(point+float(random.uniform(0.0,10.0)**3) +point*float(0.2*(random.uniform(0.0,15.0))))
        value= random.uniform( self.lo, self.hi)
        return value
   
    def normalise_val(self):
        for i in range(1,101):
            var=self.guess()
            f1,f2=self.objectives(var) 
            en=f1+f2
            if (en>self.emax):
                self.emax=en
            if (en<self.emin):
                self.emin=en
        self.minObj=self.emin
        self.maxObj=self.emax
      
        return self.emin, self.emax  
    
    def Energy(self,can,emax,emin):
        val=(self.f1(can) + self.f2(can))        
        norm_energy =(val - self.emin) / (self.emax - self.emin)
        return norm_energy
import Model 
import math 
import random 
from Model import *

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class Osyczka2(Model):
    def __init__(self):
        self.candidate=[] 
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.n=6 
        self.hi=[10, 10, 5, 6, 6, 10]
        self.lo=[0, 0, 1, 0, 1, 0]
      
       
    def f1(self,array):
            return -(25*(array[0]-2)**2 +(array[1]-2)**2 +
             (array[2]-1)**2 * (array[3]-4)**2 +
             (array[4]-1)**2)
    def f2(self,array):
            return sum([x**2 for x in array])
            
    def ok(self,can):
            return ( (((can[0]+can[1]-2)>=0) and ((6-can[0]-can[1])>=0) and ((2-can[0]+can[1])>=0) and (((2-can[0])+(3*can[1]))>=0))) and (((4-((can[2]-3)**2))-can[3])>=0) and ((((can[4]-3)**3)+can[5]-4)>=0)
    
        
    def candidates(self,i,direction,old):
        if (direction==True):
            while True:
                can= old
                val=self.guess(i)
                can[i]=val
                if (self.ok(can)): 
                    return can 
        else : 
            new = self.dec()
        return new 
        
    def guess(self,i):
        #print i 
        return self.lo[i] + r()*(self.hi[i] - self.lo[i])
        
    def dec(self):
        while True:
            can= []
            for i in range(self.n):
                val=self.guess(i)
                can.append(val)
            if (self.ok(can)): 
                    return can 
           
    def objectives(self,can): 
        return self.f1(can),self.f2(can)
    def neighbour(self,point):
        i=random.randrange(0,5,1)
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
        return self.emin, self.emax  
    
    def Energy(self,can,emax,emin):
        norm_energy =  ((self.f1(can) + self.f2(can)) - emin) / (emax- emin)
        return norm_energy
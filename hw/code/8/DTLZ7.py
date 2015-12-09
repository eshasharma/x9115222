'''
Created on Nov 17, 2015

@author: esharma
'''
import Model 
import math 
import random 
from Model import *

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class DTLZ7(Model):
    def __init__(self):
        self.candidate=[0] 
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.n=10 
        self.hi=[1,1,1,1,1,1,1,1,1,1]
        self.lo=[0,0,0,0,0,0,0,0,0,0]  
        self.name="DTLZ7"
    
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
                
    def ok(self,can):
        for i in range(0,self.n):
            if (can[i]<self.lo[i]) or (can[i]>self.hi[i]):
                return False
        return True
                  
    def f1(self,array): 
        fone=array[0]
        return fone
    
    def sum(self,array):
        sum1=0
        numlist =  [float(x) for x in array]
        s = sum(numlist)
        l = len(numlist)
        return s 
  
    def f2(self,array):
        ftwo= (1 + self.get_g(array)) * self.get_h(self.f1(array),self.get_g(array))
        return ftwo 
     
    def get_g(self, arr):
      res= float(0)
      res = 1 + float(9)/float(len(arr)) * sum(arr)
      return float(res) 
  
    def get_h(self, fone, g_value):
       res= float(0) 
       res  = float(self.n) - float(fone/( 1 + g_value)) * float(1 + math.sin(3* math.pi*fone))
       return res 
      
        
    def objectives(self,can): 
        return self.f1(can),self.f2(can)
                                    
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
        val=(self.f1(can) + self.f2(can))        
        norm_energy =(val - self.emin) / (self.emax - self.emin)
        return norm_energy
    
    def neighbour(self,point):
        i=random.randrange(0,10,1)
        value= self.candidates(i,True,point)
        return value    
       
      
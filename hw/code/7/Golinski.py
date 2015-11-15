'''
Created on Nov 8, 2015

'''
import Model 
from Model import *
import math 
import random 

pi  = math.pi
ee  = math.e
sin = math.sin
sqrt= math.sqrt
r   = random.random

class Golinski(Model):
    def __init__(self):
        self.candidate=[] 
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.n=7 
        self.hi=[3.6, 0.8, 28, 8.3, 8.3, 3.9, 5.5]
        self.lo=[2.6, 0.7, 17, 7.3,7.3, 2.9, 5]
        self.name="Golinski"
      
       
    def f1(self,dec_list):
       
        f1 = 0.7854*dec_list[0]*math.pow(dec_list[1],2)*(10*math.pow(dec_list[2],2)/3 + \
         14.933*dec_list[2]-43.0934)-1.508*dec_list[0]*(math.pow(dec_list[5],2)+math.pow(dec_list[6],2)) + \
         7.477*(math.pow(dec_list[5],3)+math.pow(dec_list[6],3))+0.7854 * \
         (dec_list[3]*math.pow(dec_list[5], 2)+dec_list[4]*math.pow(dec_list[6],2))
         
        return f1
        

    def f2(self,dec_list):
        x = math.sqrt(math.pow((745.0*dec_list[3])/(dec_list[1]*dec_list[2]),2)+1.69*math.pow(10,7)) / \
         (0.1 * math.pow(dec_list[5],3))
        return x
        
    def ok(self,array):
       
        
        g1=1.0/(array[0]*math.pow(array[1],2)*array[2]) - 1.0/27.0 <= 0
        g2=1.0/(array[0]*math.pow(array[1],2)*math.pow(array[2],2)) - 1.0/397.5 <= 0
        g3=math.pow(array[3],3)/(array[1]*math.pow(array[2],2)*math.pow(array[5],4)) - 1.0/1.93 <= 0
        g4=math.pow(array[4],3)/(array[1]*array[2]*math.pow(array[6],4)) - 1.0/1.93 <= 0
        g5=array[1]*array[2] - 40 <= 0
        g6=array[0]/array[1] - 12 <= 0
        g7=5 - array[0]/array[1] <= 0
        g8=1.9 - array[3] + 1.5*array[5] <= 0
        g9=1.9 - array[4] + 1.1*array[6] <= 0 
        g10=(self.f2(array))<=1300
        g11=math.sqrt(math.pow((745.0*array[4]/(array[1]*array[2])),2)+(1.575*math.pow(10,8))) /(0.1*math.pow(array[6],3)) <= 1100
        
        return g1 and g2 and g3 and g4 and g5 and g6 and g7 and g8 and g9 and g10 and g11 
    
        
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
        return random.uniform(self.lo[i],self.hi[i])
        
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
        return self.dec()
    
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
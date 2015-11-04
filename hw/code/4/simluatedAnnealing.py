import random 
import math
import sys

class simulatedannealing(object):
    
    kmax=3000
    emin = sys.maxint
    emax = -sys.maxint
    range=[-100000.0, 100000.0]
    cooling=150
    "we will aim to minimise the energy in this annealer"
    
    
    def find_max_min(self):
        for i in range(1,101):
            y= float(random.uniform(self.range[0],self.range[1]))
            f1=math.pow(y, 2)
            f2=math.pow((y-2), 2)
            f_total=f1+f2
            if (f_total<self.emin): 
                self.emin=f_total
            if (f_total>self.emax): 
                self.emax=f_total
   
    def find_energy(self,var): 
        f1=math.pow(var, 2)
        f2=math.pow((var-2), 2)
        energy= ((f1 + f2) - self.emin) / (self.emax- self.emin)           
        return energy 
    
    def point(self):
        value = float(random.uniform(self.range[0],self.range[1]))
        return value
    
    def neighbour(self,point):
        value=point+float(random.uniform(0.0,10.0)**3) +point*float(0.2*(random.uniform(0.0,15.0)))
        return value
    
    def prob_jump(self,enear,emine,temp):
        a = math.e**((emine -enear)/temp)
        b = random.random()
        return  a < b

    def simulated_annealer(self):
        self.find_max_min()
        energy=[]
        l=''
        k=1.0
        ebest=sys.maxint
      
        while(k<=self.kmax):
                me= self.point()
                emine= self.find_energy(me)
                near=self.neighbour(me)
                enear=self.find_energy(near)
                if (emine<ebest):
                    new='!'
                    best,ebest=me,emine
                elif (enear<emine):
                    new='+'
                    me,emine= near,enear
                elif (self.prob_jump(enear,emine,float((k/self.kmax)*self.cooling))): 
                    new='?'  
                    me,emine= near,enear  
                else:
                    new='.'
                l=l+new
        
                if (k>0):
                    if ((k%100)==0):  
                        print k,ebest,l 
                        l='' 
                k=k +1
               
      
        print "kmax=" , self.kmax  ,"cooling =" ,self.cooling ,"energy_minimum=" , ebest, "best point=" ,best
ne=simulatedannealing()
ne.simulated_annealer()
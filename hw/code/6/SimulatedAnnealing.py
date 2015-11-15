import random 
import math
import sys
import Model
import Schaffer
import Kursawe
import Osyczka2
from Schaffer import *

class simulatedannealing(object):
    def __init__(self, model):
        self.model = model
        self.kmax = 3000
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.cooling=100
        self.simulated_annealer(model)
    
    "we will aim to minimise the energy in this annealer"
    
    def prob_jump(self,enear,emine,temp):
        a = math.e**((emine -enear)/temp)
        b = random.random()
        return  a < b
    

    def simulated_annealer(self,model):
        self.emin,self.emax =model.normalise_val()
        print self.emax , self.emin
        sol0= self.model.candidates(0,False,0)
        sol0Energy= model.Energy(sol0,self.emax,self.emin)
        best=sol0
        ebest=sol0Energy
        l=''
        k=1.0
       
      
        while(k<=self.kmax):
                new='.'
                solNear=self.model.neighbour(sol0)
                solNearEnergy=model.Energy(solNear,self.emax,self.emin)
                if (sol0Energy<ebest):
                    new='!'
                    best,ebest=sol0,sol0Energy
                    sol0=solNear
                elif (solNearEnergy<sol0Energy):
                    new='+'
                    sol0,sol0Energy= solNear,solNearEnergy
                elif (self.prob_jump(solNearEnergy,sol0Energy,((float(k)/float(self.kmax)*self.cooling)))): 
                    new='?'  
                    sol0,sol0Energy= solNear,solNearEnergy  
                
                l=l+new
        
                if (k>0):
                    if ((k%100)==0):  
                        print k,ebest,l 
                        l='' 
                k=k +1
               
      
        print "kmax=" , self.kmax  ,"cooling =" ,self.cooling ,"energy_minimum=" , ebest, "best point=" ,best

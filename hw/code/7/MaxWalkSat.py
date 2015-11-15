import random 
import sys
import Model
import Schaffer
import Kursawe
import Osyczka2
from Model import *
class maxwalksat(object):
    def __init__(self, model):
        self.model = model
        self.max_tries = 25
        self.max_changes = 101
        self.threshold =250
        self.p=0.5
        self.maxwalksat_f(model)
        self.emin = sys.maxint
        self.emax = -sys.maxint
                       
    def roll_marbles_everywhere(self,variable,model):
        max_energy = -sys.maxint
        max_direction=-1
        max_scored_point=variable
        for i in range(0,model.n):
            variable=self.roll_marbles_one_direction(i,variable,model)
            current_energy= model.Energy(variable,self.emax,self.emin)
            if (current_energy>max_energy):
                max_scored_point,max_energy,max_direction=variable,current_energy,i
        return max_scored_point,max_energy,max_direction
       
    def roll_marbles_one_direction(self,i,variable,model):
            x= model.candidates(i,True,variable)
            return x 
            
    def maxwalksat_f(self,model):
        model = self.model
        re=''
        max_energy=-sys.maxint
        current_energy=0.0
        max_scored_dimension=-1
        max_scored_point=[]
        self.emin,self.emax =model.normalise_val() 
        print self.emax , self.emin
        for i in range(1,self.max_tries): 
            re=''
            variable = self.model.candidates(0,False,0)
            for j in range (1,self.max_changes):
                append=' .'
                current_energy=model.Energy(variable,self.emax,self.emin)
                if (current_energy > self.threshold): 
                    print "maximum energy is ",current_energy," maximum scored point is ",variable
                    return variable
                
                r= random.random()
                
                if (self.p <r ): 
                    variable,current_energy,max_scored_dimension=self.roll_marbles_everywhere(variable,model)
                    if (current_energy>max_energy):
                        max_scored_point,max_energy=variable,current_energy
                        append=' !'
                    else:
                        append=' +'
                  
                       
                else: 
                    if(max_scored_dimension>-1):
                        variable=self.roll_marbles_one_direction(max_scored_dimension,variable,model)
                        current_energy= model.Energy(variable,self.emax,self.emin)
                        append=' .'
                        if (current_energy>max_energy):
                            max_scored_point,max_energy=variable,current_energy
                 
                  
                re=re+append
                if (j==50):
                    print i*j ,max_energy,re
                    re=''
        print "maximum energy is ",max_energy," maximum scored point is ",max_scored_point                                 


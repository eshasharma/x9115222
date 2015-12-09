'''
Created on Nov 19, 2015

@author: esharma
'''
import random 
import math
import sys
import Model


from sk import *
from global_variables import *
from loss import *

class simulatedannealing(object):
    def __init__(self, model):
        self.model = model
        self.kmax = 400
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.cooling=100
        self.simulated_annealer(model)
        self.name='simulatedannealing'
        self.result=[]
        self.final_energy=[]
    
    "we will aim to minimise the energy in this annealer"
    
    def prob_jump(self,enear,emine,temp):
        a = math.e**((emine -enear)/temp)
        b = random.random()
        return  a < b
    

    def simulated_annealer(self,model):
        self.emin,self.emax =model.normalise_val()
        #print self.emax , self.emin
        sol0= self.model.candidates(0,False,0)
        sol0Energy= model.Energy(sol0,self.emax,self.emin)
        best=sol0
        ebest=sol0Energy
        l=''
        k=1
    #    d_energy=dict()
     #   count_dict=0 
        list_energy=[]
        a12_small=0.56
        prev_energy=[0 for _ in range(21)]
        list_loss= []
       # print prev_energy
        while(k<=self.kmax):
                    new=' .'
                    solNear=self.model.neighbour(sol0)
                    solNearEnergy=model.Energy(solNear,self.emax,self.emin)
                    if (sol0Energy<ebest):
                        new=' !'
                        best,ebest=sol0,sol0Energy
                        sol0=solNear
                    elif (solNearEnergy<sol0Energy):
                        new=' +'
                        sol0,sol0Energy= solNear,solNearEnergy
                        #if (sol0Energy<ebest):
                        #    best,ebest=sol0,sol0Energy
                    elif (self.prob_jump(solNearEnergy,sol0Energy,((float(k)/float(self.kmax)*self.cooling)))): 
                        new=' ?'
                        sol0,sol0Energy= solNear,solNearEnergy  
                        #if (sol0Energy<ebest):
                         #   best,ebest=sol0,sol0Energy
                
                    l=l+new
                    list_energy.append(sol0Energy)
                    if (k>0):
                        if ((k%25)==0):
                            print k,ebest,l 
                        #    d_energy[count_dict]=list_energy
                            l1=list_energy
                            l2=prev_energy
                            # print l1
                            #print l2
                            a12_result=a12(l2,l1)
                            if (a12_result>a12_small):
                                self.kmax =self.kmax +5
                            else :
                               self.kmax=self.kmax -1
                            prev_energy=list_energy
                           # print prev_energy
                            list_energy=[]
                            l='' 
                       #     count_dict=count_dict+1
                            if (k==25):
                                first_energy=prev_energy
                    k=k +1
        final_energy=prev_energy
        print final_energy,first_energy
        x=loss(final_energy,first_energy)


             
        global_variable.loss_inter=x

        
     #   print d_energy[count_dict]
        print "kmax=" , self.kmax  ,"cooling =" ,self.cooling ,"energy_minimum=" , ebest, "best point=" ,best
        
       
      
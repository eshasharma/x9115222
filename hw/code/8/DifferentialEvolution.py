'''
Created on Nov 17, 2015

@author: esharma
'''
import math
import sys


import Model

from sk import *
from global_variables import *
from loss import *

class differentialEvolution(object):
    def __init__(self, model):
        self.model = model
        self.kmax = 1000
        self.max_changes = 100
        self.threshold =0
        self.p=0.5
        self.f=0.75
        self.crossover=0.3
        self.epsilon=0.01
        self.emin = sys.maxint
        self.emax = -sys.maxint
        self.DifferentialEvolution_f(model)
        self.name='differentialEvolution'

    def DifferentialEvolution_f(self,model):
        self.emin,self.emax =model.normalise_val()
        model=self.model
        re = ""
        frontier=[model.candidates(0,False,0) for _ in range(self.max_changes)]
        best_energy=model.Energy(frontier[0],self.emax,self.emin)
        best_solution=frontier[0]
        k=0
        list_energy=[]
        a12_small=0.56
        prev_energy=[0 for _ in range(21)]
        while k<self.kmax :
            re=""

            if(best_energy==self.threshold):
                break

            for i, solution in enumerate(frontier):
                seen = []
                while len(seen) < 3:
                    rand_index = random.randint(0, 99)
                    if rand_index == i:
                        continue
                    if rand_index not in seen:
                        seen.append(rand_index)
                mutation=frontier[seen[0]]
                current_energy=model.Energy(solution,self.emax,self.emin)
                append=" ."
                if(self.crossover < random.random()):
                    if(model.Energy(mutation,self.emax,self.emin)<current_energy):
                        current_energy=model.Energy(mutation,self.emax,self.emin)
                        frontier[i] = mutation
                        append = " +"

                else:
                    mutation=[]
                    for j in xrange(model.n):
                        l=model.lo[j]
                        m=model.hi[j]
                        inter = (frontier[seen[0]][j] + self.f* (frontier[seen[1]][j] - frontier[seen[2]][j]))
                        if inter >= l and inter <= m:
                            mutation.append(inter)
                        else:
                            mutation.append(frontier[seen[random.randint(0, 2)]][j])

                    if(model.ok(mutation) and model.Energy(mutation,self.emax,self.emin)<current_energy) :
                        frontier[i]=mutation
                        current_energy=model.Energy(mutation,self.emax,self.emin)
                        append=" +"

                if(current_energy<best_energy  and current_energy>=self.threshold):
                    append=" ?"
                    best_energy=current_energy
                    best_solution=frontier[i]
                list_energy.append(current_energy)
                re=re+append
                k+=1
                if (k>0):
                    if (k==25):
                                first_energy=prev_energy
                    if k % 25 is 0:
                        print k,best_energy,re
                        re = ""
                       
                        l1=list_energy
                        l2=prev_energy
                       # print l1,l2
                           # print l1
                            #print l2
                        a12_result=a12(l1,l2)
                    #print a12_result
                        if (a12_result>a12_small):
                            k =k +5
                        else :
                            k=k -1
                        prev_energy=list_energy
                        list_energy=[]
                        l=''

        final_energy=prev_energy
        x=loss(final_energy,first_energy)

        global_variable.loss_inter=x

        print("\nBest Solution : " + str(best_solution))
        print("Best Energy : " + str((model.Energy(best_solution,self.emax,self.emin))))
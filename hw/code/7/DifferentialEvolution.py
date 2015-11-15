import random
import math
import sys

import Kursawe
import Model
import Schaffer


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

    def DifferentialEvolution_f(self,model):
        self.emin,self.emax =model.normalise_val()
        model=self.model
        re = ""
        frontier=[model.candidates(0,False,0) for _ in range(self.max_changes)]
        best_energy=model.Energy(frontier[0],self.emax,self.emin)
        best_solution=frontier[0]
        k=0
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

                re=re+append
                k+=1
                if k % 25 is 0:
                    print k,best_energy,re
                    re = ""

        print("\nBest Solution : " + str(best_solution))
        print("Best Energy : " + str((model.Energy(best_solution,self.emax,self.emin))))
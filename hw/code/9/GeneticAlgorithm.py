import random
import math
import sys




class GeneticAlgorithm(object):
    def __init__(self, model,fileName):
        self.model = model
        self.kmax = 1000
        self.population_Size = 100
        self.lifes=5
        self.threshold =0
        self.p_crossover=0.98
        self.p_mutation=0.05
        self.frontier_distribution=0.8
        self.emin = [sys.maxint]*model.numberOfObjs
        self.emax = [-sys.maxint]*model.numberOfObjs
        self.fileName=fileName
        self.GeneticAlgorithm_f(model)


    def bin_dom(self,can1,can2):
        #print can1,can2
        can1_obj=self.model.objectives(can1)
        can2_obj=self.model.objectives(can2)
        #print(can2_obj,can1_obj)
        if can1_obj==can2_obj:
            return False
        for i in xrange(self.model.numberOfObjs):
            if (can2_obj[i]<can1_obj[i]):
                return False
        return True

    def checkBestEnergy(self,population_frontier,model):
        best_sol=population_frontier[0]
        best_energy=model.Energy(population_frontier[0],self.emax,self.emin)
        for i in xrange (self.population_Size):
            tmp_energy=model.Energy(population_frontier[i],self.emax,self.emin)
            if(tmp_energy < best_energy):
                best_energy=tmp_energy
                best_sol=population_frontier[i]
        return best_energy,best_sol

    def selectParents(self,population_frontier,population_Size):
        i,j=random.randrange(0,population_Size,1),random.randrange(0,population_Size,1)

        return population_frontier[i],population_frontier[j]

    def crossover(self,parent1,parent2,crossover_prob,model):
        if(crossover_prob>random.random()):
            x= random.randint(1,model.n)
            child1=parent1[0:x]+parent2[x:model.n]
            child2=parent2[0:x]+parent1[x:model.n]
            return child1,child2
        else:
            return parent1,parent2


    def mutate(self,candidate,mutate_probability,model):
        if(mutate_probability>random.random()):
            x=random.randint(0,model.n-1)
            mutated_cand=candidate
            mutated_cand[x]=model.guess()
            if(model.ok(mutated_cand)):
                return mutated_cand
            else:
                return candidate
        return candidate

    def makeNewFrontier(self,children,population_frontier):
        new_frontier=[]
        j=0
        k=0
        for i in xrange(self.population_Size):
            if(self.frontier_distribution>random.random):
                new_frontier.append(children[j])
                j=j+1
            else:
                new_frontier.append(population_frontier[k])
                k=k+1
        return new_frontier

    def evaluateChildren(self,frontier,model):
        dict_frontier_energy={}
        sorted_frontier=[]
        dict_frontier_energy[0]=model.Energy(frontier[0],self.emax,self.emin)
        sorted_frontier.append(frontier[0])
        for i in xrange(1,self.population_Size,1):
            energy_temp=model.Energy(frontier[i],self.emax,self.emin)
            j=0
            for j in xrange(len(sorted_frontier)):
                if j in dict_frontier_energy:
                    check_energy=dict[j]
                else:
                    check_energy=model.Energy(sorted_frontier[j],self.emax,self.emin)
                    dict[j]=check_energy
                if(energy_temp>check_energy):
                    sorted_frontier.insert(j,frontier[i])
                    break
            if (j==len(sorted_frontier)):
                sorted_frontier.insert(j,frontier[i])
        return sorted_frontier

    def calculate_best_frontier(self,population_frontier):
        pop_front_best=[]
        for can1 in population_frontier:
            flag=True
            for can2 in population_frontier:
                if(can1==can2):
                    continue
                if self.bin_dom(can2,can1):
                    flag=False
                    break
            if flag:
                pop_front_best.append(can1)
        population_frontier_old=pop_front_best[:]
        if(len(population_frontier_old)!=100):
            i=0
            while i<(100-len(pop_front_best)):
                can=population_frontier[random.randint(0,99)]
                if(can in population_frontier_old):
                    continue
                else:
                    population_frontier_old.append(can)
                    i=i+1
        return population_frontier_old


    def GeneticAlgorithm_f(self,model):
        self.emin,self.emax=model.normalise_val()
        #print self.emin,self.emax
        population_frontier=[model.candidates(0,False,0) for _ in range(self.population_Size)]

        population_frontier_old=self.calculate_best_frontier(population_frontier)

        pop_front_best=population_frontier_old[:]
        #print len(population_frontier_old)
        #print population_frontier_old

        k=0
        life=0
        while k<self.kmax :
            i=0
            children=[]
            for i in xrange(self.population_Size):
                parent1,parent2= self.selectParents(population_frontier_old,len(population_frontier_old))
                child1,child2=self.crossover(parent1, parent2,self.p_crossover,model)
                child1=self.mutate(child1,self.p_mutation,model)
                child2=self.mutate(child2,self.p_mutation,model)
                if(self.bin_dom(child1,child2)):
                    children.append(child1)
                elif(self.bin_dom(child1,child2)):
                    children.append(child2)
                else:
                    x=random.randint(0,100)
                    if(x%2==0):
                        children.append(child2)
                    else:
                        children.append(child1)
            population_frontier_new=[]
            for can1 in population_frontier:
                flag=True
                for can2 in population_frontier:
                    if(can1==can2):
                        continue
                    if(self.bin_dom(can1,can2)):
                        flag=False
                        break
                if flag:
                    population_frontier_new.append(can1)
            tmp=[]
            new_frontier=False
            for a in population_frontier_new:
                for b in pop_front_best:
                    if self.bin_dom(a,b):
                        tmp.append(a)
                        pop_front_best.remove(b)
            if tmp:
                pop_front_best.extend(tmp)
                new_frontier=True
            if new_frontier:
                life=0
            else:
                life=life+1
            if(life==self.lifes):
                break

            population_frontier=children
            population_frontier_old=population_frontier_new

            k=k+1


        name='Pareto_Fronts/'+self.fileName
        f=open(name,'w')
        i=0
        for i in xrange(len(pop_front_best)):
            k=0
            for j in (self.model.objectives(pop_front_best[i])):
                j=(j - self.emin[k]) / (self.emax[k]- self.emin[k])
                k+=1
                s=str(j)
                f.write(s)
                f.write(" ")
            f.write("\n")
        f.close();


        return pop_front_best

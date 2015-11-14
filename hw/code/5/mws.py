'''
Created on Oct 28, 2015


'''
import random 
import sys


class maxwalksat(object):
    max_tries=25
    max_changes =101
    threshold=250  
    l=[]
    p=0.5
    emin = sys.maxint
    emax = -sys.maxint 
    bounds_high= [10, 10, 5, 6, 6, 10]
    bounds_low = [0, 0, 1, 0, 1, 0]
    
       
    def jump(self):
        while True:
            variable= []
            for i in range(6):
                val=self.assign_value(i)
                variable.append(val)
               
            if self.check_constraints(variable):
                return variable
   
    def assign_value(self,i):
        x=self.bounds_low[i]+(float)(random.random()*(self.bounds_high[i]-self.bounds_low[i])*1/0.5)
        return x
    
    def check_constraints(self,array):
        flag1=flag2=flag3=False
        if (((array[0]+array[1]-2)>=0) and ((6-array[0]-array[1])>=0) and ((2-array[0]+array[1])>=0) and (((2-array[0])+(3*array[1]))>=0)): 
            flag1=True
        if (((4-((array[2]-3)**2))-array[3])>=0):
            flag2=True
        if ((((array[4]-3)**3)+array[5]-4)>=0):
            flag3=True
        flag=(flag1 and flag2 and flag3 )
        return flag    
    
    
    def roll_marbles_everywhere(self,variable):
        max_energy = -sys.maxint
        max_direction=-1
        for i in range(0,6):
            variable=self.roll_marbles_one_direction(i,variable)
            current_energy= self.energy(variable,True)
            if (current_energy>max_energy):
                max_scored_point,max_energy,max_direction=variable,current_energy,i
        return max_scored_point,max_energy,max_direction
       
    def roll_marbles_one_direction(self,i,variable):
        while True:
            x=variable
            a=self.assign_value(i)
            x[i]=a
            if self.check_constraints(x):
                return x 
    
      
    def normalise_val(self):
        for i in range(1,101):
            var=self.jump()
            en=self.energy(var,False)
            if (en>self.emax):
                self.emax=en
            if (en<self.emin):
                self.emin=en
        print self.emin, self.emax  
           
    def energy(self,array,normalise):
        f1=float(((array[1]-2)**2)-(25*(array[0]-1)**2)+((array[2]-1)**2)*((array[3]-4)**2)+((array[4]-1)**2))
        #f1=float(((array[1]-2))**2+((array[2]-1)**2)+ ((array[3]-4)**2)+((array[4]-1)**2)-(25*(array[0]-2)**2))
        f2=float(((array[0])**2)+((array[1])**2)+((array[2])**2)+((array[3])**2)+((array[4])**2)+((array[5])**2))
        if (normalise==True):
            result =((f1 + f2) - self.emin) / (self.emax - self.emin)
        if (normalise==False):
            result =float((f1 + f2))
        return result     

         
    def maxwalksat_f(self):
        re=''
        max_energy=-sys.maxint
        current_energy=0.0
        max_scored_dimension=-1
        max_scored_point=[]
        self.normalise_val() 
        for i in range(1,self.max_tries): 
            re=''
            variable = self.jump()
            for j in range (1,self.max_changes):
                if (current_energy > self.threshold): 
                    print "maximum energy is ",current_energy," maximum scored point is ",variable
                    return variable
                if (self.p < random.random()): 
                    variable,current_energy,max_scored_dimension=self.roll_marbles_everywhere(variable)
                    if (current_energy>max_energy):
                        max_scored_point,max_energy=variable,current_energy
                        append=' +'
                    else:
                        append=' .'
                else: 
                    append=' ?'
                    if(max_scored_dimension>-1):
                        variable=self.roll_marbles_one_direction(max_scored_dimension,variable)
                        current_energy= self.energy(variable,True)
                        if (current_energy>max_energy):
                            max_scored_point,max_energy=variable,current_energy
                            
                        
                re=re+append
                if (j==50):
                    print i*j ,max_energy,re
        print "maximum energy is ",max_energy," \nmaximum scored point is ",max_scored_point                                 

ne=maxwalksat()
ne.maxwalksat_f()

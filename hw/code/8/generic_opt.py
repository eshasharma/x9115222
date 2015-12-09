'''
Created on Nov 17, 2015

@author: esharma
'''
from sk import *
from global_variables import *
import Model
import SimulatedAnnealing
import MaxWalkSat

from SimulatedAnnealing import *
from MaxWalkSat import *

from DifferentialEvolution import differentialEvolution
from MaxWalkSat import maxwalksat

from DTLZ7 import *

#,maxwalksat, differentialEvolution

#simulatedannealing(Schaffer())
#[simulatedannealing,maxwalksat, differentialEvolution]:
#maxwalksat(Schaffer())
for model in [DTLZ7]:
    data_lists = [['simulatedannealing'],['maxwalksat'],['differentialEvolution']]
    k=0
   # for _ in range(20):
    for optimizer in [simulatedannealing,maxwalksat, differentialEvolution]:

            list_loss=[optimizer.__name__]

            for _ in range(20):
                optimizer(model())
                list_loss.append(global_variable.loss_inter)
            data_lists[k]=list_loss
            k=k+1

    print data_lists
    rdivDemo(data_lists)

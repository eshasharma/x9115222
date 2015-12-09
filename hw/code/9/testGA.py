import Model
import DTLZ7
import DTLZ5
import DTLZ3
import DTLZ1
import GeneticAlgorithm
import os

from GeneticAlgorithm import GeneticAlgorithm
from DTLZ7 import DTLZ7
from DTLZ5 import DTLZ5
from DTLZ3 import DTLZ3
from DTLZ1 import DTLZ1
from hypervolume_runner import HyperVolume_wrapper

models=[DTLZ1,DTLZ3,DTLZ5,DTLZ7]
objs=[2,4,6,8]
decs=[10,20,40]
i=0
iterations=0
while iterations<1:
    for model in models:
        print model
        print '\n\n'
        for x in decs:
            print '\t\t\t',x,'\t\t\t',
        print
        for j in objs:
            print j,
            for k in decs:
                #modelName=model+'('+str(j)+','str(k)+')'
                #print modelName
                #print model(j,k)

                fileName='DTLZ-PF'+str(i)+'.txt'
                GeneticAlgorithm(model(j,k),fileName)
                HyperVolume_wrapper()
                os.remove('./Pareto_Fronts/'+fileName)
                i+=1
            print

    iterations=iterations+1







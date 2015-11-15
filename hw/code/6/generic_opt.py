import Model
import SimulatedAnnealing
import MaxWalkSat
import Schaffer
import Kursawe
import Osyczka2

from SimulatedAnnealing import *
from MaxWalkSat import *
from Schaffer import *
from Kursawe import *
from Osyczka2 import *

for optimizer in [simulatedannealing, maxwalksat]:  
    for model in [Schaffer,Osyczka2,Kursawe]:
        print "-------------------------------------------------------------------------------------"
        print "Optimizer '{}' Model '{}'".format(optimizer.__name__, model.__name__)
        print "-------------------------------------------------------------------------------------"
        optimizer(model())      
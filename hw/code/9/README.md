# x9115222

# Repository for CS 591(Automated Software Engineering)

Contributors:-

  Bhanu Anand(bhanuanand28)
  
  Esha Sharma(eshasharma)
  
  Vinay Todalge (vntodalge)

_____________________________________________________________________________________________________________________________

##Coding up the Gentic Algorithm and applying it to  DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives and 10, 20 , 40 decisions

### Running Instructions 
  1. Clone the github repository x9115222 from git@github.com:bhanuanand28/x9115222.git
  2. Navigate to ./x9115222/hw/code/9 
  3. run testGA.py
 
###Abstract
In this study, we have implemented a genetic algorithm .This genetic algorithm is run on each of DTLZ 1 , 3, 5 , 7 each time with
2,4,6,8 objectives and each of 10, 20 , 40 decisions. We run this model using the default parameters without tuning those. The analysis
of the application and performance of the Genetic Algorithm on different variations of DTLZ is done using the hypervolume function. 
We measure the hypervolume for 20 iterations . We have then plotted the hypervoume using an excel spreadsheet. Through this experiment, 
we learnt that the Genetic Algorithm performs best on  

###Introduction and Background
To implement a Genetic Algorithm and run it on TLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives and 10, 20 , 40 decisions.To 
check and compare the performance of the Genetic Algorithm on the different parameters passed. 
###Type 1 , Type 2 , Type 3 Comparison Operators
###Genetic Algorithm used ###Implementation 
Genetic algorithms are optimization algorithms which mimics the process of natural selection . In this program we did not used 
the following algorithm which we implemented: 
1. Generate the pareto frontier initially . 
2. Pareto best From the pareto frontier apply Binary domination and select parents . The number pf perants selected here will be betwen 3 to 4. 
3. Create children from the parent population using crossover . Crossover is done only when probabality condition is met. 
4. Mutate the childeren with proabality of 5 % . 
5. Create a new frontier with the children . 
6. If any child doninates any parent on the pareto best remoce the child and replace with parent . 
7. We use early termination if no child dominates reduce lives by 1 else continue with the original count of lives . 
8. Conditons used for Binary Domination : 
9. Fianl frontier is the best frontier created . 

###Implementation 
1. We have implemtent the Genetic Algorithm psuedocode specified above with the following paramters : 
2. To check the efficiency of the Genetic Algorithm we calculate the hypervolume for the model passed . 
3. Hyervolume measure the 

###Results
####DTLZ1 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ1.jpg)

####DTLZ3 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ3.jpg)

####DTLZ5 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ5.jpg)

####DTLZ7 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ7.jpg)


It can be observed from the graphs that GA works best on
###Conclusions

###Threats to Validity 
1. We ran the code only for 20 iterations . Running the code for a larger number of iterations may produce better statitics. 
2. We used the Hypervolume between generations to compute the graph . We could have used multiple other tools to calcuate the efficiency 
as well . 
3. We checked only for DTLZ . This could have been checked for multiple models . 

###Future Work 
1. The code could be run for more number of iterations. 
2. We could use hypervolume etc to generate more than 20 graphs and affirm the results across these graphs . 
3. We could use functions other than hypervolume etc to compare efficiency. 
4. We could vary the early termination conditions . 
5. We could use GA to tune models other than DTLZ and check performance on those . 


###References:-

 1. [Pseudo-code for Genetic Algorithm](http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html)
 
 2. [Hypervolume Calculator](https://github.com/ai-se/storm/tree/master/PerformanceMetrics) 
 3. 
 ###References

1. https://github.com/txt/mase/blob/master/lessthan.md
2. https://github.com/txt/mase/blob/master/STATS.md

###Acknowledgements

The study uses code for Scott knott , Loss functions which can be found here: 
 1.  https://github.com/txt/mase/blob/master/src/doc/sk.py

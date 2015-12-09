# x9115222
##Coding up the Gentic Algorithm 

#####Group Members:

- Esha Sharma 

- Bhanu Anand

- Vinay Togalde

### Running Instructions 

###Abstract
We have implemented a genetic algorithm . The genetic algorithm is then run on DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives 
and 10, 20 , 40 decisions. We run this model using the default parameters specified . The analysis of the Genetic Algorithm on 
different variations of DTLZ is done using the hypervolume. We then plot the hypervolume for different objectives and decisions and 
check the performance on different models . We run this 20 times on each . We found that . 

###Objective
To implement a Genetic Algorithm and run it on TLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives and 10, 20 , 40 decisions.To 
check and compare the performance of the Genetic Algorithm on the different parameters passed. 

###Genetic Algorithm used 
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
#DTLZ1 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ1.jpg)

#DTLZ3 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ3.jpg)

#DTLZ5 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ5.jpg)

#DTLZ7 -First era vs Final era
![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/9/ScreenShots/DTLZ7.jpg)


It can be observed from the graphs that GA works best on


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



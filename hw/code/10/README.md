# x9115222

# Repository for CS 591(Automated Software Engineering)

Contributors:-

  Bhanu Anand(bhanuanand28)
  
  Esha Sharma(eshasharma)
  
  Vinay Todalge (vntodalge)

_____________________________________________________________________________________________________________________________

##Hyper Parameter Optimization

### Running Instructions 
  1. Clone the github repository x9115222 from git@github.com:bhanuanand28/x9115222.git
  2. Navigate to ./x9115222/hw/code/10 
  3. run testGA.py
  
###Abstract
In this study we used Differential Evolution(DE) to generate the set of values which decide the extend of mutation ,crossover , 
the number of candidates and the number if generations that a genetic algorithm(GA) will run. We use DE to tune our default control 
settings. The DE tunes the GA so that the set of values which performs the most efficiently optimized solution for different 
DTLZs get generated. We apply DE to tune our GAs which optimise DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives and 10, 20 
, 40 decision. We observe that tuning the GA via DE improves the performance of GA. 

###Introduction and Background
When we use Genetic Algorithm to optimise a problem ,there are a number of parameters which decide the extent of mutation ,
crossover etc. These parameters greatly influence the performance of a GA . In the previous code we used default values for this 
optimisation. In this study we apply Differential Evolution and generate different sets of default parameter settings. These are 
then used to run GA on DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives and 10, 20 , 40 decisions. We analuze the performance 
of DE on the GAs by comparing the hypervolumes generated before and after the tuning is done.

###Genetic Algorithm 
A Genetic Algorithm is a optimization algorithm which mimics the process of natural selection. In a genetic algorithm we use selection 
to generate the best population, we then use mutationa and crosssover with the default probabilty to generate children. The children
are then compared to the parents to see if the population is getting evolved for better. Like natural selection , this process uses
crossover, mutation and selection. 

###Differential Evolution 
Differential evolution (DE) is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to 
a given measure of quality. DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate 
solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best 
score or fitness on the optimization problem at hand. In this way the optimization problem is treated as a black box that merely 
provides a measure of quality given a candidate solution and the gradient is therefore not needed.

###Implementation 
To tune the GA via DE , we created a list of decisions and assigned max and min values to them . We created a range of values within 
which the candidate for parameter are to be picked. Using these we created the list of candidate solutions which were used as default 
parameters for the GA. 

For each of the Candidate solutions we ran the GA as in code 9 and found the loss between the first and last generation . If the loss 
was significant we selected the paramter candidate geberated or we continued with the last one. For each model , we found the pareto 
frontier generated at the end and the best solution at the end of the DE's run and found the hyprvolume for this . 

We used this methos to find hypervolume for DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives 
and 10, 20 , 40 decisions.
self.hi=[300, 500, 0.99, 0.09, 0.9]
        self.lo=[100, 100, 0.50, 0.01, 0.4]
To compare we generated abaseline of reults using our code 9 . the paramters used however were 
kmax = 200 , 
population size = 100 
lives = 5
crossover =0.98
mutation_proba=0.05 
frontier_distributon - 0.8

###Results

####DTLZ1 - before and after optimization

![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/10/ScreenShots/DTLZ1.jpg)

####DTLZ3 - before and after optimization

![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/10/ScreenShots/DTLZ3.jpg)

####DTLZ5 - before and after optimization

![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/10/ScreenShots/DTLZ5.jpg)

####DTLZ7 - before and after optimization

![alt tag](https://github.com/bhanuanand28/x9115222/blob/master/hw/code/10/ScreenShots/DTLZ7.jpg)
It can be observed from the graphs that GA wokrs best on


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



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
When we use Genetic Algorithm to optimise a problem , there are a number of default values which are used in the optimisation . 
The Genetic Algorithm's extent of optimisation depends on these default parameters . We use DE to find which of these default 
values produce best results for optimisation by a GA. We use DE to tune the GA to work most efficiently . We applied DE to tune
our GAs and ran our GAs on DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives and 10, 20 , 40 decisions. We analyse the difference
betwwen the performance of DE on the GAs by comparing the hypervolumes generated. We then plotted the hypervolume values found 
and analysed the difference between them to see whether or not the performance of the GA is increased because of tuning via DE. 
We found that 

###Objective
To use Differential Evolution to tune a Genetic Algorithm which is run on DTLZ 1 , 3, 5 , 7 each time with 2,4,6,8 objectives 
and 10, 20 , 40 decisions.To check and compare the performance of the Genetic Algorithm on the different parameters passed and 
check whether or not tuning via DE improves performance of the optimizer. 

###Genetic Algorithm and Differential Evolution 

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



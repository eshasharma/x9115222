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
It can be observed from the graphs that GA wokrs best on


###Threats to Validity 
1. We ran the code only for 20 iterations . Running the code for a larger number of iterations may produce better statitics. 
2. We used the loss value between generations to compute the graph . We could have used hypervolume or any other machinery to do this 
comparison as well and based our results on the aggreagation of those results . 
3. We used weights 1 for both objectives in the aggegation function . This could be evaluated with some other weights assigned 
as well. 
4. The inner loop in each optimiser was run just 1000 times , This could have been run more number of times . 
5. The value of 0.56 seemed to be large . 


###Future Work 
1. The code could be run for more number of iterations. 
2. We could use hypervolume etc to generate more than 1 graph and affirm the results across these graphs . 
3. The inner loop could be run more than 1000 times . 
4. The weights could have been assigned by inputting the weights to an optimiser and deciding which produces best optimisation and 
tuning our optimizer based on that . 
5. We could use the value of 0.56 and tune our optimiser to that. 
6. We could tun this for other optimisers like GA and see where DE stands in comparison.




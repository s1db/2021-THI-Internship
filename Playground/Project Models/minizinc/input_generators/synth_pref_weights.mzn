include "alldifferent.mzn";
% Code Status:
% + Everything works as intended
% Look up increasing.mzn global

int: agents;
int: candidates;
int: unique_solutions;

int: combinations = product(1..candidates);

array [1..unique_solutions] of var 1..agents: weights;

constraint sum(weights) = agents;
constraint forall(i in 2..unique_solutions)(weights[i-1] > weights[i]);

solve 
:: int_search(weights, first_fail, indomain_random, complete)
satisfy;

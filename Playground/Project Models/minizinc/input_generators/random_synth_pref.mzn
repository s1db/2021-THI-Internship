include "alldifferent.mzn";

% Code Status:
% + Everything works as intended

int: candidates;
set of int: CANDIDATES = 1..candidates;
int: num_sol;
set of int: NUM_SOL = 1..num_sol;

int: permutations_num = product(1..candidates);
array [CANDIDATES, NUM_SOL] of var 1..candidates: permutations;

constraint forall(i in NUM_SOL, j in NUM_SOL where i != j)(
  alldifferent(permutations[CANDIDATES, i]) /\ permutations[CANDIDATES, i] != permutations[CANDIDATES, j]
);


solve 
:: int_search(permutations, first_fail, indomain_random)
satisfy;

output [ "\(permutations[i,j])" ++ 
         if j == num_sol then " \n" else " " endif 
         |
         i in CANDIDATES, j in NUM_SOL];

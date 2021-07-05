% + Gives a result
% - Doesn't give the right result
% TODO:
%  - Use a trick for indexing, perhaps write a function for it
%  - 

include "alldifferent.mzn";

int: candidates;
set of int: CANDIDATES = 1..candidates;
int: num_sol;
set of int: NUM_SOL = 1..num_sol;

int: permutations_num = product(CANDIDATES);
array [CANDIDATES, NUM_SOL] of var CANDIDATES: permutations;
constraint alldifferent(permutations[CANDIDATES, 1]);

% change range
constraint forall(j in 2..num_sol)(
  permutations[CANDIDATES, j] = swap(permutations[CANDIDATES, 1],  (j mod candidates)+1)
);

function array [CANDIDATES] of var int: swap(array [CANDIDATES] of var int: arr, CANDIDATES: i) = %arr;
    let{
         array [CANDIDATES] of var int: temp = [
%              arr[j]
             if j == i /\ i != 1
             then arr[i-1]
             else if j == i-1 /\ i != 1
               then arr[i]
               else arr[j]
               endif
             endif
             
%            if j == i 
%            then arr[i-1] 
%            else if j == (i-1) /\ i != 1
%              then arr[i] 
%              else arr[j] 
%              endif 
%            endif  
           | j in CANDIDATES];
     } in temp;


solve 
:: int_search(permutations, first_fail, indomain_random)
satisfy;

output [ "\(permutations[i,j])" ++ 
         if j == num_sol then " \n" else " " endif 
         |
         i in CANDIDATES, j in NUM_SOL];

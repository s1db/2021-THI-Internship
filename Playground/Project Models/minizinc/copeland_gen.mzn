include "globals.mzn";

% Code Status:
%   + Compiles and runs.
%   + Outputs an array of comparision scores between competition.
%   + Identifies the winner in a competiton.
%   - Doesn't output a single answer.

int: candidates = 4;
int: voters = 5;
set of int: CANDIDATES = 0..candidates-1;
set of int: VOTERS = 0..voters-1;

array[CANDIDATES, VOTERS] of int: rankings;
                                      %V1  V2  V3  V4  V5
rankings = array2d(CANDIDATES, VOTERS,[0,  0,  3,  3,  1,   % A
                                       1,  1,  0,  0,  2,   % B
                                       2,  2,  1,  1,  3,   % C
                                       3,  3,  2,  2,  0]); % D

array[CANDIDATES, CANDIDATES] of var int: scores = copeland(rankings);
array[CANDIDATES] of var int: election_result = copeland_result(scores);

output ["Scores:\n"];
output [ "\(scores[i,j])" ++ 
         if j == candidates-1 then " \n" else " " endif 
         |
         i in CANDIDATES, j in CANDIDATES];
output ["\nElection Results:\n"];
output [
  "\(election_result[i])" ++ " " | i in CANDIDATES
];

solve satisfy;

function array [CANDIDATES] of var int: copeland_result(array[CANDIDATES, CANDIDATES] of var int: score) =
let{
  array[CANDIDATES] of var int: result;
  float : majority = int2float(voters)/2;
  constraint forall(i in CANDIDATES)(
    result[i] = sum(j in CANDIDATES)(
      if score[i,j] > majority 
      then 2
      else if int2float(score[i,j]) == majority
           then 1
           else 0
           endif
      endif
    )
  );
} in result;


function array [CANDIDATES, CANDIDATES] of var int: copeland(array [CANDIDATES, VOTERS] of int: a) = 
    let{
        array[CANDIDATES, CANDIDATES] of var int: score;
        constraint forall(i in CANDIDATES, j in CANDIDATES)(
            if i != j
            then score[i,j] = compare(i,j)
            else score[i,j] = 0
            endif
        );
    } in score;

function int: compare(CANDIDATES: aid, CANDIDATES: bid) = 
    let{
        int: a = sum(f in VOTERS)(bool2int(rankings[aid, f] < rankings[bid, f])) 
    } in a;

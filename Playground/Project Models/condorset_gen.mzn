include "globals.mzn";

int: agents = 4;
set of int: AGENTS = 0..agents-1;
% at the moment we will only consider agents ranking each other
% TODO: generalise to agents ranking candidates later.
array[AGENTS,AGENTS] of int: rankings;

rankings = array2d(AGENTS,AGENTS, [0, 1, 1, 2, 3, 0, 0, 3, 2, 3, 2, 0, 1, 2, 3, 1,]);

array[int,int] of var int: scores = copeland(rankings);

solve satisfy;


function array [int, int] of var int: copeland(array [AGENTS,AGENTS] of int: a) = 
    let{
        array[AGENTS, AGENTS] of var int: score;
        array [int] of var int: r = [0,0];
        constraint forall(i,j in AGENTS where i < j)(
            r = compare(i,j) -> 
            score[i,j] = r[0] -> 
            score[j,i] = r[1]
        );
    } in
    score
;

function array [int] of var int: compare(AGENTS: aid, AGENTS: bid) = 
    let{
        int:a=0; int:b=0;
        constraint forall(f in 0..agents)(
            if rankings[f, aid] > rankings[f, bid]
            then b = b + 2
            else if rankings[f,aid] < rankings[f,bid] 
              then a = a+2 
              else a = a+1 -> b = b+1
              endif
            endif
        );
      array[int] of int: p = [a,b];
    } in p;
    
%    A, B, C, D
% [| 0, 1, 1, 2, % A
%  | 3, 0, 0, 3, % B
%  | 2, 3, 2, 0, % C
%  | 1, 2, 3, 1, % D
%  |];


% rankings[3,2] = 0, i.e agent D ranks C first

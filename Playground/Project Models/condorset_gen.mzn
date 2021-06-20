int: agents = 4;
set of int: AGENTS = 0..agents;

% at the moment we will only consider agents ranking each other
% TODO: generalise to agents ranking candidates later.
array[AGENTS,AGENTS] of int: rankings;

rankings =
%  A, B, C, D
[| 0, 1, 1, 2, % A
 | 3, 0, 0, 3, % B
 | 2, 3, 2, 0, % C
 | 1, 2, 3, 1, % D
 |];


% rankings[3,2] = 0, i.e agent D ranks C first

function array [AGENTS] of var int: copeland(array [AGENTS,AGENTS] of int: a) = 
    let{
        array[AGENTS, AGENTS] of int: score;
        array [int] of var int: r;
        constraint forall(i, j in AGENTS)(
            r = compare(i,j);
            score[i,j] = r[0];
            score[j,i] = r[1];
        );
    } in
    score
;

function array[AGENTS] of var int: compare(AGENTS: aid, AGENTS: bid) = 
    let{
        int: ascore;
        int: bscore;
        constraint forall( i in AGENTS)(
            if rankings[i,aid] > rankings[i,bid] 
            then bscore = bscore + 2
            else 0
            endif
            
            if rankings[i,aid] < rankings[i,bid] 
            then ascore = ascore + 2 
            else 0
            endif
            
            if rankings[i,aid] == rankings[i,bid] 
            then ascore += 1 bscore += 1;
            else 0 
            endif
            
            array [int] of var int: r = [ascore, bscore]
        )
    } in r;
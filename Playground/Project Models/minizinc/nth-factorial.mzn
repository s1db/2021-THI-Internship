% Not required since all will be a random arrangement of the original.
% Thus, to model a 'real' election we need to model the distribution and not individual voting patterns.
% Hence, the next step is generate a random alldifferent set of votes.

int: n;
int: size;
set of int: SIZE = 0..size-1;

array [SIZE] of var int: remainder;
array [SIZE] of var int: quotent;
%array [SIZE] of var int: factordict;

constraint quotent[0] = n-1;
constraint remainder[0] = 0;

constraint forall(i in 1..size-1)( quotent[i] = quotent[i-1] div (i+1) );
constraint forall(i in 1..size-1)( remainder[i] = quotent[i-1] mod (i+1) );

constraint forall(i in 0..size-1)(
  
);

function array [SIZE] of var int: swap(array [SIZE] of int: arr, SIZE: fst, SIZE: snd) = 
    let{
        int: temp = arr[fst];
        constraint arr[fst] = arr[snd];
        constraint arr[snd] = temp;
    } in arr;

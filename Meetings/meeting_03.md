# Meeting 03

_Meeting will take place on 8st July 2021, at 14:30 IST._

## Notes

## SAT 03 July 2021
- Read Chapter 09 of cos.

## SUN 04 July 2021
- Worked on generating inputs
    - n-th permute
    - 'clustered' ordering
- Chapter 10 of cos

## MON 05 July 2021
- Chapter 10 of cos cont.
- Ideating over how to study the copeland method.


## Chapter 9 Notes CompSoc
### Motivation
- On the preference aggregation and voting of finite domain values. 
- Voting maps a preference profile to a set of alternatives. This is complicated when the set of alteratives is large because of the combinatorial structure of the problem.
- 3 Examples:
    - Multiple referenda: wants that are not homogeneous often being grouped together.
    - Group configuration: Groups need to come together and arrive at a collective concensus to promote a collective agenda to pass a motion.
    - Committee Elections/multiwinner elections: A set selecting a subset.
- Structure of the 3 examples:
    A = D_1 X ... D_p where D_i is a finite value domain of X_i.
- Still the major issue is e trade-off between expressivity and cost. Lacy and Niou (2000)
    + Number of possibilities grows exponentially with the domains, thus a high cognitive cost, probably not a problem for computers.
    - If the voter gives only their top ranked preference, then not as expressive but easy on the compute.


- Plurality voting is arbitrary since 3 or more alternatives are tied together to a single vote in combinatorial structure problems.

THOUGHT: Could this be related to the curse of dimensionality?

## Meeting Points of Discussion
- 10.8 of cos highlight
    - Distortion: 
        - the downside of converting to ordinal rankings is that it leads to loss of important information. 
        - max-min normalization might be helpful. 
        - refer to paper related to loss of information.
    - Learnability of winners. 
- combinatorial voting and curse of dimensionality.

random sampling a viable solution set and picking copeland winners:
- key questions:
    - in a sample is it possible for one of the lesser values to be a copeland winner?
    - in a sample whats the probability that one of the values with a lower copeland score is actually a winner?
        - how do we model and study this?
    - starting off directly in mz-py might not be viable till we don't answer these questions, thus let's try to model this first.
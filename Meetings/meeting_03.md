# Meeting 03

_Meeting will take place on 8st July 2021, at 14:30 IST._

## Notes

### SAT 03 July 2021
- Read Chapter 09 of comsoc.

### SUN 04 July 2021
- Worked on generating inputs
    - n-th permute
    - 'clustered' ordering
- Chapter 10 of comsoc

### MON 05 July 2021
- Chapter 10 of comsoc cont.
- Ideating over how to study the large-preference profile copeland methods statistically.

### TUE 06 July 2021
- Central Question: Is the sampling method for Copeland even viable?
- Important papers from chapter 10 of comsoc.
    - [ (.) ] Strategic Candidacy and Voting Procedures Dutta et.al.
        - AIM: To figure out how strategic entry affects every non-dictatorial voting procedure that satisfies unanimity.
        - Doesn't concern our problem since we're assuming that IIA is satisfied.
        - This paper only deals with Non-dictatorship and Unanimity, thus IIA is not satisfied.
### WED 07 July 2021
- [x] Read more papers and write why they're important.
- [x] Come up with ideas for implementing Copeland.
- [x] Go over Python code and add comments.

- [ (.) ] The Unavailable Candidate Model: A Decision-Theoretic View of Social Choice, Lu et.al
    - AIM: Candidates may be unavailable after vote aggregation. Minimizes expected voter dissatisfaction with the chosen candidate.
    - RESULT: Kemeny consensus produces optimal allocation when candidates disappear.
- [ (.) ] Rank Aggregation Methods for the Web.
    - AIM: Take a bunch of search engines and look at page ranks, aggregate them with a voting method to pick winners in an attempt to filter spam. 
### THU 08 July 2021
## Chapter 9 Notes CompSoc
### Motivation
[ (.) ] TL;DR: Not directly related to the problem at hand, will be helpful when extending further to combinatorial voting problems. Deals mainly with effective ways to aggregate preferences for multi-object selection.
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

[ (.) ] THOUGHT: Could this be related to the curse of dimensionality?

## Meeting Points of Discussion
- Go over code written.
- What is Dueling Bandit Problem?
- Constraint Sampling.
- Tips on exploring the subject domain?
- Tips on reading papers?

- 10.6 Uncertain Set of Alternatives
    - The problem with the current literature is that it focuses on alternatives being unavailable after a vote and not the potential of an unavailable alternative becoming available again.
- Incremental Voting literature
    - The problem with this domain is that it again deals with re-voting on the same candidates with the same agents.
- 10.8 of comsoc highlight
    - Distortion:
        - the downside of converting to ordinal rankings is that it leads to loss of important information. 
        - max-min normalization might be helpful. 
        - refer to paper related to loss of information.
        - might be beneficial to retain the objective scores and maintain the 'opportunity cost'. 
    - Learnability of voting methods.
- combinatorial voting and curse of dimensionality.

Is random sampling a viable method to arrive at a solution set and picking copeland winners?:
- key questions:
    - in a sample is it possible for one of the lesser values to be a copeland winner?
    - in a sample whats the probability that one of the values with a lower copeland score is actually a winner?
        - how do we model and study this?
        - Does IIA make this problem trivial?
    - starting off directly in mz-py might not be viable till we don't answer these questions, thus let's try to model this first.
    - The problem with the 'random' approach is that it doesn't give the solver a direction to search with, and a random walk can be computationally expensive since every new solution, the set is updated. Like we have a social welfare max/min methodology, thus it might be interesting to couple the two, use a social welfare function to give direction to the solver and use a voting mechainism at consecutive intervals to find an appropriate solution.
        - How does Condorcet get around score updates?
            - It compares to everything in the set and other solutions don't have to be updated.
# Meeting 00

_Meeting took place on 17th June 2021, at 13:30 IST._

## Tasks for next meeting
- [ ] Go through the tooling, Minizinc Python API and CPMpy and pick one.
- [ ] Read up on Copeland method and (weighted) tournament solutions.
- [ ] Briefly go through the current codebase.


## Voting Paper Notes (Incomplete)
https://docs.google.com/document/d/1mCtHC0vHYQ3Ko_X-VGyC6FiA3jbKV9r93Bb7SOTchLo/edit?usp=sharing




## MAS Chapter 09 Notes (Incomplete)
- [x] Section 01
- [x] Section 02
- [x] Section 03 -- Voting
    - Voting Methods:
        - Plurality voting - person with most votes wins. Limited expression of voters
        - Cumulative voting - Each voter given k votes that are distributed arbitrarily, most votes wins.
        - Approval voting - Each voter can cast a single vote for as many of the candidates as he wishes; the candidate with the most votes is selected.
        --RANKING METHODS--
        - Elimination methods - 
        - Borda voting - rankings + plurality 
        - Nanson’s method - rankings + plurality + Elimination
        - Pairwise elimination - given order of comparision each person needs to pick a winner, least preferred is eliminated, then recalculated.
    - Voting Paradoxes:
        - Condorcet condition - pairwise winner
        - Sensitivity to a losing candidate -  A third candidate who stands no chance of being selected can thus act as a “spoiler,” changing the selected outcome.
        - Sensitivity to the agenda setter - 
- [x] Section 04 --  Social Functions
    - Social welfare functions:
        - Pareto efficiency (PE):
            - Same as strict Pareto efficiency.
        - Independence of irrelevant alternatives(IIA):
            - the selected ordering between two outcomes should depend only on the relative orderings they are given by the agents.
        - Nondictatorship (ND): That there does not exist a single agent whose preferences always determine the social ordering.
        => No result satisfies all 3.
        - Arrow's Theorem: If |O| ≥ 3, any social welfare function W that is Pareto efficient and independent of irrelevant alternatives is dictatorial.
    - Social choice functions:
- [ ] Section 05 -- Ranking systems

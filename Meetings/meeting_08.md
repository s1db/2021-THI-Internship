# Meeting 08
Date: 2021-08-26 0900 BST

## Notes
- Candidates when uniformly distributed have a skewed distribution of copeland score frequencies.
- The frequency of copeland score is dependent on the step size and deletion ratio.
- Resources for weighted tournaments.
    - In the handbook of of social choice.
    - look into top cycles.
    - eigen value decompositoin of the agacency matrix, page 86 weighted tournaments.
    - kengall-wei scores. 
- Small combinatorial problems if we can find small but useful
    - photo assignment.
    - define the problem as a minizinc problem.
    - familiarise yourself to the model.
    - play around with small instances. (5)
## Tasks
- TUE:
    - [ ] Try implementing the photo assignment problem in Python+MiniZinc.
        - multiple agents, specified by the program.
        - each votes on a solution, 'satisfied' by having either 2 of its friends around itself.
            - thus, the ranking is essentially just 0 or 1 or 2 by each agent on a certain solution.
        - [x] Read model
        - [x] Read and apply inputs to the imported model.
        - [x] Solve the model. 
        - [x] Reads solutions from set of solutions.
            - [x] Gets the preferences of each solution.
        - [x] Computes the copeland score for the set of solutions.
    - [ ] Turn into a Python class.
    
    - [ ] Read up on weighted tournaments.
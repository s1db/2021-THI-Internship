# Meeting 7
Date: 2021-08-22 10:00 BST
## Work done:
- Implemented deletion of candidates.
- Implemented reading and writing of the preference profiles.
- Implemented plots comparing the original copeland score and the copeland score with deletion of candidates.
## Topics to go over
- Effect of candidates being deleted.
    - Lower score candidates anyway don't have a chance at winning since the number of agents is constant.
    A
    B
    C
- Using copeland method for heuristic search in ML.
- Is deletion a feasible approach?

## Tasks
- Implement the deletion of candidates in the lazy implementation of the copeland method.
- Distribution of copeland scores (Histogram)
    - x axis: copeland scores.
    - y axis: frequency of that score.
    - Can be used for stopping criteria.
- Randomise the preference profiles.
    - Only pick a subset/fixed budget.
- Experiments with the deletion of rates.
- Gap b/w the real and deletion copeland score.
    Weighted tournament.
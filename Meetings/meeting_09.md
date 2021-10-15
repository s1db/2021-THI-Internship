# Meeting 09
Date: 2021-09-02 0900 BST

## Notes
- Varying solutions of even small cases.
- Using satisfy instead of maximize to guide the search leads to multiple 'bad' solutions.

- Possibly generate a limited number of solutions by adding constraints to the model and asynchronously sending solutions to the copeland functions w/ deletion.
- Could add random 'set of constraints' to the model to expedite.

## Tasks
- Alter the copeland function to maximize the score instead of minimizing the score.
- Compare systematic ordering (solve satisfy) with random (solve::insearch(int_search_space::random_restart(...))) and with a diversity mixin.
- Create a few slides to copeland deletion method.
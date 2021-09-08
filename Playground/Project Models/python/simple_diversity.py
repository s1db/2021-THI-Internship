"""
A minimal working example that shows how a diversity mixin would work.

In principle:
    1.) Get a solution
    2.) Define a boolean decision variable for every variable we care about
        Tie it to x[i] != x_old[i]
    3.) Set "maximize differences" as objective
    4.) Solve
"""
print("Hello you")

import logging
import os
logging.basicConfig(filename="minizinc-python.log", level=logging.DEBUG)

from minizinc import Instance, Model, Result, Solver, Status
from minizinc import Instance, Model, Solver

# Load n-Queens model from file
small_model = Model("./small.mzn")
# Find the MiniZinc solver configuration for Gecode
gecode = Solver.lookup("gecode")
# Create an Instance of the n-Queens model for Gecode
instance = Instance(gecode, small_model)


# Find and print all intermediate solutions
print("Normal traversal")
with instance.branch() as inst:
    inst["old_solutions"] = []
    result = inst.solve(all_solutions=True)
    for i in range(len(result)):
        print(result[i, "x"])

# Inverted traversal of solutions
print("Inverted traversal")
with instance.branch() as inst:
    inst["old_solutions"] = []
    inst.add_string("solve :: int_search(x, input_order, indomain_max, complete) satisfy;")
    result = inst.solve(all_solutions=True)
    for i in range(len(result)):
        print(result[i, "x"])

# Random traversal of solutions
print("Random traversal")
with instance.branch() as inst:
    inst["old_solutions"] = []
    inst.add_string("solve :: int_search(x, input_order, indomain_random, complete) satisfy;")
    result = inst.solve(all_solutions=True)
    for i in range(len(result)):
        print(result[i, "x"])

# Maximizing diversity of solutions
print("Diversity maximization")

# this is tied to what we have in the "simple_diversity_mixin.py"
variables_of_interest_key : str  = "diversity_variables_of_interest"

# we'll need a solution pool of previously seen solutions
# to rule out condorcet cycles; a solution is stored as a Python dictionary from variable to value
solution_pool = []

search_more : bool = True
no_solutions = 0

while search_more:
    with instance.branch() as inst:
        if solution_pool: # once we have solutions, it makes sense to maximize diversity
            inst.add_string("solve maximize diversity_abs;")
        else:
            inst.add_string("solve satisfy;")

        inst["old_solutions"] = solution_pool
        res = inst.solve()

        if res.solution is not None:
            print(res["x"])

        search_more = res.status in {Status.SATISFIED, Status.ALL_SOLUTIONS, Status.OPTIMAL_SOLUTION}
        if search_more:
            next_sol_vars = res[variables_of_interest_key]  # copy the current solution variables
            solution_pool += next_sol_vars




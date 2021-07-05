import minizinc

from minizinc import Model
import logging
from copeland_runner import CopelandRunner

logging.basicConfig(filename="minizinc-python.log", level=logging.DEBUG)

from minizinc import Instance, Model, Result, Solver, Status

# hooking up the base model
gecode = Solver.lookup("gecode")
m = Model("../minizinc/base_model_pref_profile_2_2.mzn")
#m.add_file("wallis_sample2_2.dzn")

# define core variables of interest (we can have multiple occurrences of the same scores,
# but the projection onto the variables of interest have to change
variables_of_interest = ["x", "y", "control"]
use_weak_condorcet_domination = True

copeland_runner = CopelandRunner(m, gecode, variables_of_interest, "AGENTS", "agent_prefers", use_weak_condorcet_domination)
copeland_runner.debug = True # stores intermediate generated MZN files for debugging
copeland_runner.run_basic()
#copeland_runner.run_extended()
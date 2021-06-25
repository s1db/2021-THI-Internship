import logging

logging.basicConfig(filename="minizinc-python.log", level=logging.DEBUG)

import minizinc

model = minizinc.Model(["nqueens.mzn"])
solver = minizinc.Solver.lookup("gecode")
instance = minizinc.Instance(solver, model)
instance["n"] = 12
print(instance.solve())
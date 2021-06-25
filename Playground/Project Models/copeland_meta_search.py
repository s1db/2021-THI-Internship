import minizinc as mz
import numpy as np

logging.basicConfig(filename="minizinc-python.log", level=logging.DEBUG)

model = mz.Model(["minizinc/copeland_gen.mzn"])
solver = mz.Solver.lookup("gecode")
instance = mz.Instance(solver, model)
instance["n"] = 9
print(instance.solve())


class CopelandRunner():
    def __init__(self, model, solver, variables_of_interest, agents_key, agent_prefers_key, use_weak_condorcet_domination=False):
        self.model = model
        self.variables_of_interest = variables_of_interest
        self.solver = solver
        self.inst = mz.Instance(self.solver, self.model)
        self.agents_key = agents_key
        self.agent_prefers_key = agent_prefers_key
        self.all_solutions = []

    def copeland_rank(rankings):
        CANDIDATES = rankings.shape[0]
        VOTERS = rankings.shape[1]
        scores = np.fromfunction(np.vectorize(lambda a, b: np.count_nonzero(
            rankings[a, :] < rankings[b, :])), shape=(CANDIDATES, CANDIDATES), dtype=int)
        result = np.fromiter(((2*np.sum(scores[a, :] > VOTERS/2) + np.count_nonzero(
            scores[a, :] == VOTERS/2)) for a in range(CANDIDATES)), int)
        return result

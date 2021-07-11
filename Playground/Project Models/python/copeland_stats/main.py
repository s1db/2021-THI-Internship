import numpy as np

#
# GOALS:
#     - [ ] Create a large preference profile.
#     - [ ] Compute the copeland score for it.
#     - [ ] Take random samples of the preference profile to converge on the copeland set.
#

CANDIDATES = 4
VOTERS = 5

rankings = np.array([0, 0, 3, 3, 1,
                     1, 1, 0, 0, 2,
                     2, 2, 1, 1, 3,
                     3, 3, 2, 2, 0]).reshape((CANDIDATES, VOTERS))


def copeland():
    return np.fromfunction(np.vectorize(lambda a, b: np.count_nonzero(rankings[a, :] < rankings[b, :])), shape=(CANDIDATES, CANDIDATES), dtype=int)


def scores_calc(a, score):
    return 2*np.sum(score[a, :] > VOTERS/2) + np.count_nonzero(score[a, :] == VOTERS/2)


def scores():
    return np.fromiter((scores_calc(x, copeland()) for x in range(CANDIDATES)), int)


print(scores())

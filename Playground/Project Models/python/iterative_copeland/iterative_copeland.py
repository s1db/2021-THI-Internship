'''
Iterative Copeland:
    - VOTERS/AGENTS -> the agents that rank/score the different candidates.
    - CANDIDATES -> the set of solutions that the different agents rank/score.
    - Cadidates are added in each iteration.
    - Our aim is do better than recomputing the whole matrix at each iteration.
    - Numpy is avoided to study the computational complexity of the whole program.
    - Once done, check if it gives the same output when the candidates are shuffled.
    - Present literature claims that Copeland Method is NP.
    - We want to check if adding a new candidate iteratively is also NP with a constant number of agents.
        - It's computationally cheaper than I thought! 
    - We also want to check if its better than recomputing the whole matrix.
'''
'''
PROJECT NOTE:
    - the rankings will either need to be recomputed at each iteration, or we'll need to use an ordinal approach.
        - Iteratively adding candidates would technically require a recompute of all rankings.
    - Incase of the ordinal approach, utility of each voter needs to be normalized.
    - ML literature has many ways scores can be computed and normalized to mitigate bias.
    - This can also be defied as a reasonable constraint on the problem at hand.
'''
'''
OPEN QUESTIONS NOTE:
    # Could rankings be replaced with utility scores?
    # How does that affect the copeland method?
    # Refer to chapter 10 of comsoc.
'''
import math
VOTERS = 5
CANDIDATES = 4

#                     V_0 V_1 V_2 V_3 V_4   <-- voters/agents
original_rankings = [[0,  0,  3,  3,  1],   # C_0
                     [1,  1,  0,  0,  2],   # C_1
                     [2,  2,  1,  1,  3],   # C_2
                     [3,  3,  2,  2,  0]]   # C_3 <-- candidates
                                            # ...


'''
    - Computes the complete matrix
    - Only performs half the comparisions.
    - Returns an array which grows as an arithmetic progression with the no candidates.
    - A visual proof for how this works and why it can be done iteratively with the addition of a new candidate: 
        https://docs.google.com/presentation/d/1QSrd2i72x5r1nJ_GzHoGXJsJYefKVytp2YtCwlCuWYo/edit?usp=sharing
'''
def pairwiseScoreCalcListFull(pref_profile, no_of_candidates):
    scores = []
    for i in range(no_of_candidates):
        for j in range(i):
            scores.append(sum([pref_profile[i][k] < pref_profile[j][k] for k in range(VOTERS)]))
    return scores

'''
    - Similar to the code above.
    - Difference being that it doesn't recompute all scores, just appends to the scores list.
    - NOTE: Needs to be changed to use the global scores array rather than a local copy.
'''
def pairwiseScoreCalcListNew(scores, pref_profile, no_of_candidates):
    for j in range(no_of_candidates):
        scores.append(sum([pref_profile[no_of_candidates][k] < pref_profile[j][k] for k in range(VOTERS)]))
    return scores

def copelandScoreFull(scores, no_of_agents, no_of_candidates):
    final_score = [0]*no_of_candidates
    for x,i in enumerate(scores):
        return None        
'''
- Reads list of scores and presents the scores[r][c] value
'''
def matrix2list(r, c, scores_list, no_of_voters):
    if r < c: return no_of_voters - scores_list[math.ceil((c*(c-1)/2) + r)]
    elif r == c: return 0
    else: return scores_list[math.ceil((r*(r-1)/2) + c)] # NOTE: change to roof/floor respectively. Not appropriately tested
'''
def list2matrix(k, scores_list):
    # r < c
    # 2*i = (r**2 - r + c)
    2*k = r**2 - r + 2*c
    r = 
    c = 
    i = n - 2 - math.floor(math.sqrt(-8*k + 4*n*(n-1)-7)/2.0 - 0.5)
    j = k + i + 1 - n*(n-1)/2 + (n-i)*((n-i)-1)/2
    # this tells us that RHS is even.
    return (i,j)
'''
scores = pairwiseScoreCalcListFull(original_rankings, CANDIDATES)

'''
    - Prints complete score matrix
'''
def fullScoreMatrixOutput():
    for i in range(CANDIDATES):
        s = ""
        for j in range(CANDIDATES):
            s = s + str(matrix2list(i, j, scores, VOTERS)) + " "
        print(s)

fullScoreMatrixOutput()
'''
- Compares all preference profiles with each other.
- Returns a CANDIDATE X CANDIDATE matrix.
- Uses matrices and not lists.
'''
@DeprecationWarning
def scoreCalc(pref_profile):
    scores = []
    for x in pref_profile:
        l = []
        for y in pref_profile:
            l.append(sum([x[k] < y[k] for k in range(len(x))]))
        scores.append(l)
    return scores

@DeprecationWarning
def copelandScore(pref_profile, agents, voters):
    copeland_score = []
    for i in range(agents):
        copeland_score.append(scoreCalc(i))
    return copeland_score

'''
# Grows with each addition to the candidates, samples from the original profile.
i_rankings = []
i_scores = []
# Adds new agents, one at a time.
for x, i in enumerate(original_rankings):
    i_rankings.append(i)
    i_scores = pairwiseScoreCalcListNew(i_scores, i_rankings, x)
    print(i_scores)
'''
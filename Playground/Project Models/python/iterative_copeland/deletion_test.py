'''
NOTE:
- [x] Create voter profiles
    - [x] Write code to pickle the profiles.
    - [x] Generate profiles and see if they can be opened.
- [x] Implement the iterative version of adding and deleting candidates (2 hours)
    - [x] Implement the iterative version of adding. (30 minutes)
    - [x] Implement the deleting feature. (1 hour)
- [ ] Compare the results of the new Copeland score with the original Copeland score to see if it got the winners right. (3 hours)
'''

import iterative_copeland as ic
import pickle
import numpy as np
from array import array

import matplotlib.pyplot as plt

# Reading pickled files and storing the data.
pickled_file = open("voter_profiles/random_large.vt", "rb")
preference_profile = pickle.load(pickled_file)
true_copeland_score = None

try:
    true_copeland_score = pickle.load(pickled_file)
except:
    None

pickled_file.close()

# Processing the data.
candidates = len(preference_profile)
agents = len(preference_profile[0])
# t = preference_profile[-1]
# preference_profile[-1] = preference_profile[-2]
# preference_profile[-2] = t

def deletionCopeland(preference_profile, step, deletion_ratio):
    i_preference_profile = []
    for i in range(0, candidates, step):
        # Growing set of candidiates.
        i_preference_profile.extend(preference_profile[i : i+step])
        score_list = ic.pairwiseScoreCalcListFull(
            i_preference_profile, len(i_preference_profile), agents)
        copeland_score = ic.copelandScoreFull(score_list, len(i_preference_profile), agents)
        
        sorted_copeland_score = np.argsort(copeland_score)
        no_of_deleted_candidates = int(deletion_ratio*len(i_preference_profile))
        to_be_deleted = sorted_copeland_score[0:no_of_deleted_candidates]
        
        i_preference_profile = [i for j, i in enumerate(i_preference_profile) if j not in to_be_deleted]
    score_list = ic.pairwiseScoreCalcListFull(
            i_preference_profile, len(i_preference_profile), agents)
    copeland_score = ic.copelandScoreFull(score_list, len(i_preference_profile), agents)
    return (i_preference_profile, copeland_score)

ipp, cs = deletionCopeland(preference_profile, 100, 0.1)
print("--------")
print(len(ipp) == len(cs))
print("--------")
not_deleted_candidate_ids = []
for i,x in enumerate(preference_profile.tolist()):
    if x in np.array(ipp).tolist():
        not_deleted_candidate_ids.append(i)
print(not_deleted_candidate_ids)
print(len(not_deleted_candidate_ids) == len(cs))

plt.plot(not_deleted_candidate_ids, cs, 'ro')
plt.plot(range(candidates), true_copeland_score, 'bo')
plt.show()
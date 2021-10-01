import iterative_copeland as ic
import pickle
import numpy as np
from array import array

import matplotlib.pyplot as plt


def deletionCopeland(preference_profile, step, deletion_ratio):
    # Processing the data.
    candidates = len(preference_profile)
    agents = len(preference_profile[0])
    i_preference_profile = []
    for i in range(0, candidates, step):
        # Growing set of candidiates.
        i_preference_profile.extend(preference_profile[i: i+step])
        score_list = ic.pairwiseScoreCalcListFull(
            i_preference_profile, len(i_preference_profile), agents)
        copeland_score = ic.copelandScoreFull(
            score_list, len(i_preference_profile), agents)

        sorted_copeland_score = np.argsort(copeland_score)
        no_of_deleted_candidates = int(
            deletion_ratio*len(i_preference_profile))

        to_be_deleted = sorted_copeland_score[0:no_of_deleted_candidates]
        i_preference_profile = [i for j, i in enumerate(
            i_preference_profile) if j not in to_be_deleted]
    score_list = ic.pairwiseScoreCalcListFull(
        i_preference_profile, len(i_preference_profile), agents)
    copeland_score = ic.copelandScoreFull(
        score_list, len(i_preference_profile), agents)
    return (i_preference_profile, copeland_score)


def plot(filename):
    # Reading pickled files and storing the data.
    pickled_file = open("voter_profiles/"+filename+".vt", "rb")
    preference_profile = pickle.load(pickled_file)
    true_copeland_score = None
    # Processing the data.
    candidates = len(preference_profile)
    agents = len(preference_profile[0])

    score_list = ic.pairwiseScoreCalcListFull(
        preference_profile, candidates, agents)
    true_copeland_score = ic.copelandScoreFull(score_list, candidates, agents)
    true_copeland_score = [i/candidates for i in true_copeland_score]
    pickled_file.close()

    ipp, cs = deletionCopeland(preference_profile, 10, 0.4)
    cs = [i/len(cs) for i in cs]
    not_deleted_candidate_ids = []
    for i, x in enumerate(preference_profile.tolist()):
        if x in np.array(ipp).tolist():
            not_deleted_candidate_ids.append(i)
    

    fig, (ax1) = plt.subplots(1)
    fig.suptitle('Copeland Scores')
    fig.set_size_inches(11.69,8.27)
    ax1.plot(not_deleted_candidate_ids, cs, 'ro')
    ax1.plot(range(candidates), true_copeland_score, 'bo')
    ax1.legend(['Copeland Score Post Deletion', 'Real Copeland Score'])
    ax1.set_xlabel('Candidate IDs')
    ax1.set_ylabel('Normalised Copeland Score')

    # plt.hist(true_copeland_score, bins=np.arange(
    #     min(true_copeland_score), max(true_copeland_score)+1), color='w')
    plt.show()
for i in ["inverted", "normal", "random", "search_more"]:
    for j in ['5']:
        # try:
        plot(i+str(j))
        print(i+str(j))
        # except:
        #     None
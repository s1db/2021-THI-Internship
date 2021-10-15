import iterative_copeland as ic
import pickle
import numpy as np
from array import array
from celluloid import Camera
import imageio

from os import listdir
from os.path import isfile, join


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def deletionCopelandFamily(preference_profile, step, deletion_ratio):
    # Processing the data.
    candidates = len(preference_profile)
    agents = len(preference_profile[0])
    familyipp = []
    familycs = []
    i_preference_profile = []
    for i in range(0, candidates, step):
        # step-size equivalent no of candidates added.
        i_preference_profile.extend(preference_profile[i: i+step])
        # calculation of pairwise score
        score_list = ic.pairwiseScoreCalcListFull(
            i_preference_profile, len(i_preference_profile), agents)
        # calculation of copeland score
        copeland_score = ic.copelandScoreFull(
            score_list, len(i_preference_profile), agents)

        sorted_copeland_score = np.argsort(copeland_score)
        no_of_deleted_candidates = int(
            deletion_ratio*len(i_preference_profile))

        familyipp.append(i_preference_profile)
        familycs.append(copeland_score)

        to_be_deleted = sorted_copeland_score[0:no_of_deleted_candidates]
        i_preference_profile = [i for j, i in enumerate(
            i_preference_profile) if j not in to_be_deleted]
    score_list = ic.pairwiseScoreCalcListFull(
        i_preference_profile, len(i_preference_profile), agents)
    copeland_score = ic.copelandScoreFull(
        score_list, len(i_preference_profile), agents)
    familyipp.append(i_preference_profile)
    familycs.append(copeland_score)
    print(len(familyipp[0]))
    print(len(familycs[0]))
    assert len(familyipp[0]) == len(familycs[0])
    return (familyipp, familycs)

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

    familyipp, familycs = deletionCopelandFamily(preference_profile, 10, 0.6)
    familyndci = []
    for i in range(len(familycs)):
        cs = familycs[i]
        ipp = familyipp[i]
        cs = [i/len(cs) for i in cs]
        not_deleted_candidate_ids = []
        for i, x in enumerate(preference_profile.tolist()):
            if x in np.array(ipp).tolist():
                not_deleted_candidate_ids.append(i)
        familyndci.append(not_deleted_candidate_ids)
    assert len(familyipp) == len(familycs) == len(familyndci)
    for i in range(len(familycs)):
        assert len(familyipp[i]) == len(familycs[i]) == len(familyndci[i])
    
    
    fig, ax1 = plt.subplots()
    camera = Camera(fig)
    for i in range(len(familyipp)):
        not_deleted_candidate_ids = familyndci[i]
        cs = familycs[i]
        cs = [j/len(cs) for j in cs]
        fig.suptitle('Copeland Scores')
        fig.set_size_inches(11.69,8.27)
        ax1.plot(range(candidates), true_copeland_score, 'bo')
        ax1.legend(['Real Copeland Score', 'Copeland Score Post Deletion'])
        ax1.set_xlabel('Candidate IDs')
        ax1.set_ylabel('Normalised Copeland Score')
        ax1.plot(not_deleted_candidate_ids, cs, 'ro')
        camera.snap()
        # ax1.lines.pop(0)
    animation = camera.animate(blit=False)
    animation.save('gifs/'+filename+'.gif', writer = 'imagemagick')

def changespeed():
    onlyfiles = ['gifs/' + f for f in listdir("./gifs/") if isfile(join("./gifs/", f))]
    for file in onlyfiles:
        gif = imageio.mimread(file)
        imageio.mimsave(file, gif, fps=1)


for i in ["inverted", "normal", "random", "search_more"]:
    for j in ['4','5','6']:
        try:
            plot(i+str(j))
            print(i+str(j))
        except:
            None
            

changespeed()
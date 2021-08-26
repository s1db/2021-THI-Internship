# Meeting 05

_Meeting will take place on 22nd July 2021, at 14:30 IST._

## Points of Discussion
- Code changes/additions:
    - bipolar bias      - fuzzing
    - unipolar bias     - shift to numpy
    - clustered
- Copeland method is not Independence of Irrelevant Alternatives.
    - 'Irrelevant' is defined as 'non winners'
    - Candidates thus cannot be deleted if we're picking 1 winner and not a set of winners.
    - Refer to https://math.libretexts.org/Bookshelves/Applied_Mathematics/Math_in_Society_(Lippman)/02%3A_Voting_Theory/2.11%3A_Whats_Wrong_with_Copelands_Method to understand why.
- We would need to use a bipolar template as our sample as we can predict the result through median voter theorem.

- Bipolar/Median voter theorem implementation has a floating point round-off error.
    - Decide on which distribution implementation to use bipolar/clustered i.e ratio/number of entries.
- Median voter theorem does not hold for combinatorial elections.
    - Thus, for combinatorial choice problems copeland method might not be preferred.

- problems with the current implementation of clustered.py:
    - lexicographical ordering isn't working properly due to it being list comparisons.
    - Shuffling the list of candidates is not working properly.

## Next Steps

Parameters for experimental:
    - Take a JSON file as input.
    - Experiment runner that JSON as input and outputs the preference profiles using the templates.
    - Tie the copeland implementation to the experimental runner.
    - Make plots of the some of the template results.
        - Look into the distribution of the preferences.
    - Facade pattern.
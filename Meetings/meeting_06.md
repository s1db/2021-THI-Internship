# Meeting 06

_Meeting will take place on 29nd July 2021, at 17:30 IST._

## Notes
Fuzzing to be a percentage.
Export as JSON.

Use the current generated templates with run condorcet and copeland runners (MiniZinc).
Move towards very large voter profiles.
    Explore using local search.
        pick k solutions (say best 50%) and introduce k/2 new solutions.
        minizinc with output a 'stream' and we'll manipulate the solver with python 'copeland-ish' implementation.
        Compare the local search approach with the complete copeland score.
        See how many 'solutions picked'/size of the neighborhood impacts the 'copeland-local-search' score compared to the 'copeland-complete' score.
Goals:
    - [x] Implement a copeland deletion algorithm
    - [x] Study how deletion impacts the selection condorcet winner.
    - [x] Compare the two, local-search and complete copeland.
    - [x] Give the option of picking up on a 'pattern'.

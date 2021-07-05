# Meeting 02

_Meeting will take place on 1st July 2021, at 14:30 IST._

## Sprint Goals
- [x] Go through present codebase
- [x] Generation of synthetic preference profiles (random or realistic)
- [x] Add on of diversity mixin
## Daily Checklist
### MON 28th June 2021
- [x] CP2020 video.
    - E.g: Problems of itinerary selection.
    - Numerical optimization isn't ideal for all cases.
    - We don't want someone unfairly dominate the preferences.
    - Can be adapted to any optimization problem with multiple agents.
    - Related work(soft constraints and social choice):
        - sequential voting paper 
            [+] sequential voting + any evaluation criteria
            [+] builds of sequential voting work and has nice math properties.
            [-] no backtracks thus can lead to less optimal solutions.
        - Distributed Constraint Optimization
            [-] focus has distributed/async execution of solvers
- [x] Read CCO notes
    - Goal: Social Choice Functions + Constraint Optimization
        - find a set of potential solutions and get the agents to rank them.
        - find the preferred solution.
        - use a secondary objective function to select from the filtered solution set.
    - Intro to voting:
        - Everyone agent ranks a contestant.
        - a SCF returns a set of winners after evaluating the votes.
        - larger the set of contestants, the harder it is to find a condorcet winner -- aka pairwise winner.
        - Borda counting -- rankings augmented by points and most points wins.
- [x] Alexander's video from last week
    - Run condorce in the important file algo>vm>
        - using sample problem 2.2
        - prints all solutions
    - base model
        - 4 fake combinatorial solutions to artifically constraint the model.
        - if any of the 4 is chosen an associated value is set for x and y.
        - set order helps with debugging.
    - each iteration leads to a comparison and a winner is chosen.
- [x] Copeland Meta Search
    - [x] Basic setup
    - [x] Figure out how to use randomness in search.
### TUE 29th June 2021
- 
### WED 30th June 2021
### THU 01th June 2021
- [x] 1430 Meeting
### FRI 02th June 2021
### SAT 03th June 2021
### SUN 04th June 2021

## Notes
- Voting book. -- Metric Preferences
- Clustered votes example in Python
- Wallis Book -- Condorcet Method and Extended Method
- Chapter 9 and 10 of Social CS book
### Thoughts on the copeland ranking algorithm
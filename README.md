# GA_8Queens
Genetic algorithm implemetation for 8 queens problem.

Structure:
  -	Board.py - board display
  -	Fitness.py - fitness calculation functions
  -	Main.py - run point, algorithm
  -	Queens.py - genetic algorithm functions

***

Individuals are represented in 1D array: indexes represent the row, values represent the column, counting starts from 0.

Board displays the individual on a 2D array, 0 representing empty space, 1 representing a queen.

## Usage

The user can enter starting generation size, mutation rate and the amount of times the program will be run.
Running the program once will display:
  - the state of the solution individual
  - the representation on the board
  - how many generations it took to find the solution

![Single_run](/assets/single.png "Run single time")

Running the program more than one time will display:
  - how many generations it took to find the solution
  - the state of the solution individual
  - statistics of the runs

![Multiple_run](/assets/multiple.png "Run multiple times")


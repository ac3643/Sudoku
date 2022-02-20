# Sudoku
Sudoku Solver with Backtracking and Forward Checking

## Execution Options:

1. `$ python3 sudoku.py <input string>` 

This option allows you to run the sudoku solver on a single sudoku puzzle.

Try it out with the hardest Sudoku in the world! 

Input String:

800000000003600000070090200050007000000045700000100030001000068008500010090000400

Solution:

812753649943682175675491283154237896369845721287169534521974368438526917796318452

2. `$ python3 sudoku.py` 

This option reads the "sudoku-start.txt" file which contains 400 Sudoku Puzzles. The program outputs "output.txt" which contains all 400 solutions. 

WARNING: running sudoku.py on 400 Sudoku puzzles may take around 5 minutes in total. To speed up run time, comment out print statements in lines 401 and 410. 

"Sudokus_finish.txt" contains solutions to puzzles. Run `$ python3 file_comp2.py` to compare "output.txt" to "sudoku_finish.txt". 

See ReadMe.txt for run time statistics. 



## Conways Game of Life 2.0
#### (Framework for New Rules)

### Setup:
- download Python 3.12
- to run file, in terminal (navigating to same directory is easiest in running), type ```python3 conways.py```
- if on mac, run ```brew install tcl-tk``` for mouse optimization (or ```pip3 install tcl-tk``` if you don't want to install homebrew and instead use the baseline Python pip, but i recommend homebrew) 

### Creating New Rules
- In ```conways.py```, navigate towards the bottom, which is marked by code.
- Comment out the rule you don't want to run (using # at the beginning of the line)
- And then simply add the replacement!

#### e.g., removing overpopulation rule
```new_grid[row][col] = 1 if alive_neighbors in [2, 3] else 0``` -> ```new_grid[row][col] = 1 if alive_neighbors >= 2 else 0```
- For a populated cell to survive, it must have exactly two or three **or four** neighbors.
- Each cell that is populated, but only has one neighbor dies, as if by solitude.
- ~~Each cell that is populated and has four or more neighbors dies, as if by overpopulation.~~ -> No death by overpopulation.
- Each empty cell with three populated neighbors becomes populated.

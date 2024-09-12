# NU-Wild-Rabbit

## Run Han's Demo
```sh
python3 integrate.py
# You can specify BFS or DFS in the python script
```

## Example Matrix
```python
import numpy as np

example_maze = np.mat([[3, 2, 2, 1],
                       [1, 2, 1, 1],
                       [2, 2, 2, 2],
                       [4, 1, 2, 2]])
```

## Pre-defiend Data Structue
The maze is defiend as a 2D matrix in numpy. Each element in this matrix is a int number. Here's the corresponding states for different numbers:
* 1: Wall
* 2: Free
* 3: Start
* 4: Goal
* 5: Visiting
* 6: Visited
* 7: Available Path
* 8: Unavailable Path

## Roadmap
We should have three main funcitons, each is a class.
* Maze Generator: Generates a maze map with predefiend data structue (2D numpy matrix).
  * Input: User UI / Random Generating
  * Output: 2D Numpy Matrix
* Maze Solver: Iterates the maze matrix state and record every iterated state for further visualization.
  * Input: 2D Numpy Matrix
  * Output: Recorded 2D Numpy Matrices in every iteration
* Maze Visualizer: Visualizing the maze map.
  * Input: 2D Numpy Matrix
  * Output: Visualization

## Installation
```sh
git clone git@github.com:HarrisonBounds/Maze-Solver.git
```
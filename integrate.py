from random_generator import *
from visualizer import *
from solver import *

rg = RandomGenerator(dim_m=25, dim_n=25)
maze = rg.generate_random_maze()
        
ms = MazeSolver(maze)
ms.solve_maze_recursive()
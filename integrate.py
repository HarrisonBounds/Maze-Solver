from random_generator import *
from visualizer import *
from solver import *

rg = RandomGenerator(dim_m=20, dim_n=20)

# maze = rg.generate_random_maze()
# dfsms = DFSMazeSolver(maze)
# dfsms.solve_maze_recursive()

maze = rg.generate_random_maze()
bfsms = BFSMazeSolver(maze)
bfsms.solve_maze_recursive()
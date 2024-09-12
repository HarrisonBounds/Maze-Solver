from random_generator import *
from visualizer import *

rg = RandomGenerator(dim_m=10, dim_n=10)
maze = rg.generate_random_maze()

vis = MazeVisualizer()
vis.display_single_state(maze, 1.0)
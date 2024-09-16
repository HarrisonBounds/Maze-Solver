from maze import Maze
from DFS_solver import DFSSolver

maze = Maze(45,80)
maze.init_random_maze_map()

bfs_solver = DFSSolver(maze)
bfs_solver.find_the_goal()
bfs_solver.find_the_shortest_path()
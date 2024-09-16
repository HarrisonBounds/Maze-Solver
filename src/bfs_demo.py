from maze import Maze
from BFS_solver import BFSSolver

maze = Maze(180,320)
maze.init_random_maze_map()

bfs_solver = BFSSolver(maze)
bfs_solver.find_the_goal()
bfs_solver.find_the_shortest_path()
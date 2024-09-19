from maze import Maze
from new import BFSSolver

rows = int(input("How many rows do you want the maze to have?: "))
cols = int(input("How many columns do you want the maze to have?: "))
choice = int(input("Type 1 for BFS and 2 for DFS: "))

maze = Maze(rows, cols)
maze.init_random_maze_map()
maze = maze.as_matrix()

solver = BFSSolver(maze)

if choice == 1:
    solver.solver(maze)
if choice == 2:
    solver.dfs(maze)
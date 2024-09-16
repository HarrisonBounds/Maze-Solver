from maze import Maze
from algorithms import Maze_Solver

rows = int(input("How many rows do you want the maze to have?: "))
cols = int(input("How many columns do you want the maze to have?: "))
choice = int(input("Type 1 for BFS and 2 for DFS: "))

maze = Maze(rows, cols)
maze.init_random_maze_map()
maze = maze.as_matrix()

solver = Maze_Solver(maze, rows, cols)

if choice == 1:
    solver.bfs(maze)
if choice == 2:
    solver.dfs(maze)
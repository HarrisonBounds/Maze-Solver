from var_names import *
import random

class Maze:

    def __init__(self, size):
        self.size = size
        self.start_row = None
        self.start_col = None
        self.goal_row = None
        self.goal_col = None
        self.maze_grid = [[None] * size for _ in range (size)] 

    def gen_maze(self):
        size = self.size
        start_row, start_col = random.randint(0, size), random.randint(0, size)
        goal_row, goal_col = random.randint(0, size), random.randint(0, size)

        while goal_row == start_row and goal_col == start_col:
            goal_row, goal_col = random.randint(0, size), random.randint(0, size)

        self.start_row = start_row
        self.start_col = start_col
        self.goal_row = goal_row
        self.goal_col = goal_col
        
        maze_grid = [[None] * size for _ in range (size)] 
        square_type = [WALL, FREE]

        for row in range(size):
            for col in range(size):
                if row == start_row and col == start_col:
                    maze_grid[row][col] = START
                elif row == goal_row and col == goal_col:
                    maze_grid[row][col] = GOAL
                else:
                    maze_grid[row][col] = random.choice(square_type)
        return start_row, start_col, goal_row, goal_row, maze_grid

size = 4
maze = Maze(size)
start_row, start_col, goal_row, goal_col, maze = maze.gen_maze()
print(start_row, start_col)
print(goal_row, goal_row)

print(maze)

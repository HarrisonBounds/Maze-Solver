from var_names import *

# right, down, left, up
dirs = [(0, 1), (1, 0), (0, -1), (1, 0)] # AI Citation

class Square():
    def __init__(self, val, x, y, isWall):
        self.val = val
        self.x = x
        self.y = y
        self.isWall = isWall
        self.isStart = False
        self.isGoal = False
        self.neighbor_list = []

    def get_neighbors(self):
        return self.neighbor_list
    

cur_path = []
sln_path = []
class MazeSolver():
    def __init__(self, maze):
        self.maze = maze
        self.visited_stack = []


        # AI Citation 1a 
        self.square_grid = [[None] * len(maze) for _ in range (len(maze))] # to access the squares and their relationships
        
    def is_valid_move(self, row, col):
        if row < len(self.maze) and row >= 0 and col < len(self.maze) and col >= 0: # within bounds
            return self.square_grid[row][col] != WALL and self.square_grid not in self.visited_stack # AI Citation 1a
        return False
        
    def create_relationships(self):
        maze_size = len(self.maze)
        for row in range (maze_size):
            for col in range (maze_size):

                square_val = self.maze[row][col]
                if square_val != WALL: # only add neighbors for non-wall squares
                    square = Square(square_val, row, col, square_val == WALL)

                    if square_val == START: # START square
                        square.isStart = True
                        cur_path.append(square) 
                        sln_path.append(square)
                    
                    if square_val == GOAL: # GOAL square
                        square.isGoal = True

                    for item in dirs:
                        new_row, new_col =  row + item[0], col + item[1] # AI Citation
                        if (self.is_valid_move(new_row, new_col)):
                            neigh_val = self.maze[new_row][new_col]
                            if neigh_val != 1: # not a wall
                                neigh = Square(neigh_val, new_row, new_col, False)
                                if neigh_val == GOAL: # GOAL square
                                    neigh.isGoal = True
                                square.neighbor_list.append(neigh)


def dfs_helper(square):
    print("Visiting:", (square.x, square.y), square.val)
    cur_path.append(square)
    sln_path.append(square)

    if square.isGoal == True:
        print("GOAL FOUND")
        return True

    for neigh in square.neighbor_list:
        return dfs_helper(neigh)

    sln_path.remove(square)
    return False


def dfs():
    square = cur_path.pop()
    return dfs_helper(square)


example_maze = [[99, 0, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 0],
                [100, 1, 1, 1]]

mymaze = MazeSolver(example_maze)
mymaze.create_relationships()
dfs()

from var_names import *

# right, down, left, up
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # AI Citation

class Square():
    def __init__(self, val, row, col, isWall):
        self.val = val
        self.row = row
        self.col = col
        self.isWall = isWall
        self.isStart = False
        self.isGoal = False
        self.neighbor_list = [] # can just be a list of indices, not Square objects

    def get_neighbors(self):
        return self.neighbor_list
    

class MazeSolver():
    def __init__(self, maze):
        self.maze = maze
        self.visited_list = []
        self.stack = []
        self.sln_path = [] # AI Citation 1a

        # AI Citation 1a 
        self.square_grid = [[None] * len(maze) for _ in range (len(maze))] # to access the squares and their relationships
        
    def is_valid_move(self, row, col):
        if row < len(self.maze) and row >= 0 and col < len(self.maze) and col >= 0: # within bounds
            return self.square_grid[row][col] != WALL and self.square_grid not in self.visited_list # AI Citation 1a
        return False
        
    def create_relationships(self):
        maze_size = len(self.maze)
        for row in range (maze_size):
            for col in range (maze_size):

                square_val = self.maze[row][col]
                square = Square(square_val, row, col, square_val == WALL)

                if square_val == START: # START square
                    square.isStart = True
                    self.stack.append(square) 
                    self.sln_path.append(square)
                
                if square_val == GOAL: # GOAL square
                    square.isGoal = True

########################## BEGIN AI CITATION 1a #####################################
                self.square_grid[row][col] = square # track newly instantiated Square in square_rid

                for item in dirs:
                    new_row, new_col =  row + item[0], col + item[1]
                    if self.is_valid_move(new_row, new_col):
                        neigh = [new_row, new_col]
                        if neigh not in square.neighbor_list:
                            square.neighbor_list.append(neigh)
########################## END AI CITATION 1a #######################################
    def print_sln(self):
        for sq in self.sln_path:
            print(sq.val, ":", sq.row, sq.col)

    def dfs(self):
        square = self.stack.pop()
        self.visited_list.append([square.row, square.col]) # add START square to the stck
        for n_idx in square.neighbor_list:
            self.stack.append(self.square_grid[n_idx[0]][n_idx[1]]) # and add its neighbors

        while self.stack != None:
            n = self.stack.pop() # explore a neighbor
            self.visited_list.append([n.row, n.col])

            self.sln_path.append(n)

            if n.isGoal:
                print("Solution found!")
                self.print_sln()
                return True

            for nn_idx in n.neighbor_list: # explore the neighbor's neighbors
                nRow = nn_idx[0]
                nCol = nn_idx[1]
                if self.is_valid_move(nRow, nCol):
                    self.stack.append(self.square_grid[nRow][nCol])

        print("No solution.")
        return False


example_maze = [[99, 0, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 0],
                [100, 1, 1, 1]]

mymaze = MazeSolver(example_maze)
mymaze.create_relationships()
mymaze.dfs()
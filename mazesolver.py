# right, down, left, up
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # AI Citation

class Square():
    def __init__(self, val, x, y, isWall):
        self.val = val
        self.x = x
        self.y = y
        self.isWall = isWall
        self.visited = False
        self.isStart = False
        self.isGoal = False
        self.neighbor_list = []

    def get_neighbors(self):
        return self.neighbor_list
    

class MazeSolver():
    def __init__(self, maze):
        self.maze = maze
        self.cur_path = []
        self.sln_path = []
        self.square_grid = None     # AI Citation [1a]
        
    def is_valid_move(self, row, col):
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze):
            square = self.square_grid[row][col]                         # AI CITATION [1a]
            return not square.isWall and not square.visited
        return False
        
    def create_relationships(self):
        maze_size = len(self.maze)
########################### BEGIN AI CITATION [1a] ############################
##########################################################################
        self.square_grid = [[None for _ in range(maze_size)] for _ in range(maze_size)]

        # First pass: Initialize all squares
        for row in range(maze_size):
            for col in range(maze_size):
                square_val = self.maze[row][col]
                square = Square(square_val, row, col, square_val == 1)
                self.square_grid[row][col] = square

########################### END AI CITATION [1a]############################
##########################################################################

                if square_val == 99:  # START square
                    square.isStart = True
                    square.visited = True
                    self.cur_path.append(square)

                if square_val == 100:  # GOAL square
                    square.isGoal = True

        # Second pass: Establish neighbor relationships
        for row in range(maze_size):
            for col in range(maze_size):
                square = self.square_grid[row][col]
                if not square.isWall:  # Only add neighbors for non-wall squares
                    for item in dirs:
                        new_row, new_col = row + item[0], col + item[1]
                        if self.is_valid_move(new_row, new_col):
                            neighbor = self.square_grid[new_row][new_col] # AI Citation
                            square.neighbor_list.append(neighbor) 

########################### BEGIN AI CITATION [2a] ############################
##########################################################################
    def print_maze(self):
        for row in self.square_grid:
            for square in row:
                if square.isStart:
                    print("S", end=" ")  # Start
                elif square.isGoal:
                    print("G", end=" ")  # Goal
                elif square in self.sln_path:
                    print(".", end=" ")  # Current path
                elif square.isWall:
                    print("#", end=" ")  # Wall
                else:
                    print(" ", end=" ")  # Empty space
            print()
        print("\n")

    def dfs_helper(self, square):
        self.print_maze()  # Print maze at each step
########################### END AI CITATION [2a] ############################
##########################################################################

        print("Visiting:", (square.x, square.y), square.val)
        self.cur_path.append(square)
        self.sln_path.append(square)
        square.visited = True

        if square.isGoal:
            print("GOAL FOUND")
            return True

        for neigh in square.neighbor_list: # AI CITATION [1a] 
            if not neigh.visited:
                if self.dfs_helper(neigh):
                    return True

        # Backtrack if no solution found
        self.sln_path.pop()
        return False

    def dfs(self):
        if self.cur_path:
            start_square = self.cur_path[0]  # Don't pop, just access # AI CITATION [1a]
            return self.dfs_helper(start_square)


example_maze = [[99, 0, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 0],
                [100, 1, 1, 1]]

########################### BEGIN AI CITATION [2a] ############################
##########################################################################
maze_1 = [[99, 0, 0, 1],
          [1, 1, 0, 1],
          [1, 0, 0, 0],
          [1, 1, 1, 100]]

maze_2 = [[99, 0, 1, 1],
          [1, 0, 1, 1],
          [1, 0, 0, 1],
          [1, 1, 1, 100]]

maze_3 = [[99, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 0, 1],
          [1, 1, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 100],
          [1, 1, 1, 1, 0, 1]]

maze_4 = [[99, 0, 0, 0, 1],
          [1, 1, 0, 1, 1],
          [0, 0, 0, 0, 1],
          [1, 0, 1, 0, 0],
          [1, 1, 1, 1, 100]]

########################### END AI CITATION [2a] ############################
##########################################################################

mymaze = MazeSolver(maze_4)
mymaze.create_relationships()
mymaze.dfs()


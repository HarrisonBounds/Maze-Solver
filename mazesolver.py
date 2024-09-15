from var_names import *
from square import Square

# right, down, left, up
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # AI Citation

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
            square = self.square_grid[row][col]
            return square.val != WALL and [square.row, square.col] not in self.visited_list # AI Citation 1a
        return False
        
    def setup_square_grid(self): # instantiate ALL the squares in the maze, including walls
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
#####################################################################################

                self.square_grid[row][col] = square # track newly instantiated Square in square_rid

    def create_relationships(self):
        self.setup_square_grid()

        maze_size = len(self.maze)
        for row in range (maze_size):
            for col in range (maze_size):

                square = self.square_grid[row][col] # access already created Square to establish neighbors

                if not square.isWall: 
                    for item in dirs:
                        new_row, new_col =  row + item[0], col + item[1]
                        if self.is_valid_move(new_row, new_col):
                            neigh_idx = [new_row, new_col]
                            if neigh_idx not in square.neighbor_list:
                                square.neighbor_list.append(neigh_idx)
########################## END AI CITATION 1a #######################################
#####################################################################################

    def print_sln(self):
        for sq in self.sln_path:
            print(sq.val, ":", sq.row, sq.col)

    def print_maze_each_step(self):
        for row in self.square_grid:
            for sq in row:
                if sq.isWall:
                    print("X", end=" ")
                elif sq.isStart:
                    print("S", end=" ")
                elif sq.isGoal:
                    print("G", end=" ")
                elif [sq.row, sq.col] in self.visited_list:
                    print(".", end=" ")
                else:
                    print(" ", end=" ")
            print("\n")
        print("######################################\n")

    def dfs(self): # TODO: Cite https://www.programiz.com/dsa/graph-dfs
        self.print_maze_each_step()
        print("\n")

        square = self.stack.pop()
        self.visited_list.append([square.row, square.col]) # add START square to the stck
        for n_idx in square.neighbor_list:
            self.stack.append(self.square_grid[n_idx[0]][n_idx[1]]) # and add its neighbors

        while len(self.stack) != 0 : # while there are still available squares to explore
            self.print_maze_each_step()
            
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


example_maze = [[START, FREE, FREE, WALL],
                [WALL, FREE, WALL, WALL],
                [FREE, FREE, FREE, FREE],
                [GOAL, WALL, WALL, WALL]]


########################## BEGIN AI CITATION 3a ##################################### #TODO: reorganize citation
#####################################################################################
solvable_maze = [
    [1, 1, 1, 1, 1],
    [1, 3, 2, 4, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]
]

unsolvable_maze = [
    [1, 1, 1, 1, 1],
    [1, 3, 2, 1, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 2, 1, 1],
    [1, 1, 1, 1, 4]
]
########################## END AI CITATION 3a #####################################
#####################################################################################

# mymaze = MazeSolver(example_maze)
# mymaze.create_relationships()
# mymaze.dfs()

# mymaze = MazeSolver(solvable_maze)
# mymaze.create_relationships()
# mymaze.dfs()

mymaze = MazeSolver(unsolvable_maze)
mymaze.create_relationships()
mymaze.dfs()
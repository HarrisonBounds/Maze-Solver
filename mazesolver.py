# right, down, left, up
dirs = [(0, 1), (1, 0), (0, -1), (1, 0)] # AI Citation

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
        # self.square_list = []
        self.cur_path = []
        self.sln_path = []
        self.dfs_list = []
        
    def is_valid_move(self, row, col):
        if row < len(self.maze) and row >= 0 and col < len(self.maze) and col >= 0: # within bounds
            return True
        
    def create_relationships(self):
        maze_size = len(self.maze)
        for row in range (maze_size):
            for col in range (maze_size):

                square_val = self.maze[row][col]
                if square_val != 1: # only add neighbors for valid squares
                    square = Square(square_val, row, col, square_val == 1)

                    if square_val == 99: # START square
                        square.isStart = True
                        self.cur_path.append(square) 
                        self.sln_path.append(square)
                    
                    if square_val == 100: # GOAL square
                        square.isGoal = True

                    for item in dirs:
                        new_row, new_col =  row + item[0], col + item[1] # AI Citation
                        if (self.is_valid_move(new_row, new_col)):
                            neigh_val = self.maze[new_row][new_col]
                            if neigh_val != 1: # not a wall
                                neigh = Square(neigh_val, new_row, new_col, False)
                                if neigh_val == 100: # GOAL square
                                    neigh.isGoal = True
                                square.neighbor_list.append(neigh)



    # def display_relationships(self):
    #     for square in self.square_list:
    #         print(square.val,":")
    #         for neigh in square.neighbor_list:
    #             print(neigh.val)

    def dfs(self):
        start_row, start_col = 0, 0
        start_squ_val = 99
        maze_size = len(self.maze)
        self.dfs_list.append(square_val, start_row, start_col, start_squ_val)

        for row in range (maze_size):
            for col in range (maze_size):
                square_val = self.maze[row][col]


example_maze = [[99, 0, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 0],
                [100, 1, 1, 1]]

mymaze = MazeSolver(example_maze)
mymaze.create_relationships()
# mymaze.display_relationships()

# for square in mymaze.square_list:
#     print(square.val,": ")
#     for neigh in square.get_neighbors():
#         print(neigh.val)


# use stack for dfs
# use queue for bfs

# left, right, up, down
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)] # AI Citation
# for item in dirs:
#     print(item[0])

class Square():
    def __init__(self, val, x, y, isWall):
        self.val = val
        self.x = x
        self.y = y
        self.isWall = isWall
        self.neighbor_list = []


class MazeSolver():
    def __init__(self, maze):
        self.maze = maze
        self.square_list = []
        
    def is_valid_move(self, row, col):
        if row < len(self.maze) and row >= 0 and col < len(self.maze) and row >= 0: # within bounds
            return True
        
    def create_relationship(self):
        maze_size = len(self.maze)
        # for row in range (1):
        for row in range (maze_size):
            for col in range (maze_size):

                square_val = self.maze[row][col]
                if square_val != 1: # only add neighbors for valid squares
                    square = Square(square_val, row, col, square_val == 1)

                    for item in dirs:
                        new_row, new_col =  row + item[0], col + item[1] # AI Citation
                        if (self.is_valid_move(new_row, new_col)):
                            neigh_val = self.maze[new_row][new_col]
                            if neigh_val != 1: # not a wall
                                square.neighbor_list.append(Square(neigh_val, row, col, False))
                    self.square_list.append(square)

    def display_relationships(self):
        for square in self.square_list:
            print(square.val,":")
            for neigh in square.neighbor_list:
                print(neigh.val)

    def get_neighbors(self, row, col):
        pass

example_maze = [[99, 0, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 0],
                [100, 1, 1, 1]]

mymaze = MazeSolver(example_maze)
mymaze.create_relationship()
mymaze.display_relationships()

class MazeSolver:
    def __init__(self, maze, start):
        """
        Initializes the maze solver with the maze grid and start position.
        
        :param maze: List of lists representing the maze grid.
        :param start: Tuple (row, col) for the starting position.
        """
        self.maze = maze
        self.start = start
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = set()

    def is_valid_move(self, row, col):
        """
        Checks if moving to (row, col) is within bounds, is traversable, and is not visited.
        
        :param row: Row index.
        :param col: Column index.
        :return: True if the move is valid; False otherwise.
        """
        return (0 <= row < self.rows and 0 <= col < self.cols and (self.maze[row][col] == 0 or self.maze[row][col] == 4) and (row, col) not in self.visited)

    def dfs(self, row, col):
        """
        Depth-First Search to explore paths in the maze.
        
        :param row: Current row index.
        :param col: Current column index.
        :return: True if a path to any target (marked as 4) is found; False otherwise.
        """
        # Check if we have reached a target cell marked as 4
        if self.maze[row][col] == 4:
            #self.maze[row][col] = 8  # Mark the target cell as part of the path
            return True
        
        # Mark the current cell as visited
        self.visited.add((row, col))
        self.maze[row][col] = 8  # Mark the current cell as part of the path
        
        # Explore all four possible directions (EAST, WEST, SOUTH, NORTH)
        for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + d_row, col + d_col
            if self.is_valid_move(new_row, new_col):
                if self.dfs(new_row, new_col):
                    return True
        
        # If no path found, backtrack
        self.maze[row][col] = 0
        return False

    def solve(self):
        """
        Solves the maze using DFS from the start position.
        """
        if self.dfs(self.start[0], self.start[1]):
            print("Solved Maze:")
            self.print_maze()
        else:
            print("No path found to any target cell.")

    def print_maze(self):
        """
        Prints the maze.
        """
        for row in self.maze:
            print(row)


# Example usage
example_maze = [[3, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 0, 0],
                [1, 1, 4, 0, 1, 1, 0],
                [1, 1, 1, 0, 0, 0, 0]]

start = (0, 0)  # Starting position

solver = MazeSolver(example_maze, start)
solver.solve()

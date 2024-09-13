class Maze:
    def __init__(self, maze, rows, cols) -> None:
        self.maze = maze
        self.rows = rows
        self.cols = cols
        self.visited = []
        
    def checkBounds(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and maze[row][col] != 1:
            return True
        
            
    def dfs(self, maze, row, col):
        
        stack = [(row, col)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while stack:
            #Use a stack to get the current position by popping
            current = stack.pop()
            row, col = current
            
            #If we reach our goal return true
            if maze[row][col] == 4:
                return True
            
            if current not in self.visited:
                self.visited.append(current)
                
                #Search north, south, east, west
                for direction in directions:
                    new_row = current[0] + direction[0]
                    new_col = current[1] + direction[1]
                    
                    if self.checkBounds(new_row, new_col) or current not in self.visited:
                        stack.append((new_row, new_col))
                        
                        if maze[row][col] != 3:
                            maze[row][col] = 8
                        
    
        return False
        
maze = [[3, 0, 0, 1],
        [1, 0, 1, 1],
        [1, 0, 0, 0],
        [4, 0, 0, 0]]

maze_solver = Maze(maze, len(maze[0]), (len(maze[1])))
maze_solver.dfs(maze, 0, 0)
print(maze)

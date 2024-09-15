class Maze:
    def __init__(self, maze, rows, cols) -> None:
        self.maze = maze
        self.rows = rows
        self.cols = cols
        self.visited = []
        
    def checkBounds(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and maze[row][col] != "W":
            return True
        
    def findStart(self, maze):
        for i in range(len(maze[0])):
            for j in range(len(maze[1])):
                if maze[i][j] == "S":
                    start = (i, j)
                    return start
                
    def bfs(self, maze, row, col):
        
        bfs_counter = 1
        start = self.findStart(maze)
        current = start
        print("type of current:", type(current[0]))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        print("type of directions:", type(directions[0]))
        
        while True:
            
            for direction in directions:
                new_row = current[0] + direction[0]
                new_col = current[1] + direction[1]
                
                if self.checkBounds(new_row, new_col):
                    current = (new_row, new_col)
                    maze[new_row][new_col] = bfs_counter
                    
            if maze[new_row][new_col] == "G":
                return True
                    
            bfs_counter += 1
            
            
        return False
                    
            
                    
        
        # while queue:
        #     current = queue.pop(0)
        #     row, col = current
            
        #     if maze[row][col] == "G":
        #         return True
            
        #     if current not in self.visited:
        #         self.visited.append(current)
                
        #         #Search north, south, east, west
        #         for direction in directions:
        #             new_row = current[0] + direction[0]
        #             new_col = current[1] + direction[1]
                    
                    
        #             if self.checkBounds(new_row, new_col):
        #                 queue.append((new_row, new_col))
        #                 maze[new_row][new_col] = bfs_counter
                        
        #         bfs_counter += 1
                             
    
        # return False
        
        
            
    def dfs(self, maze, row, col):
        start = self.findStart(maze)
        stack = [start]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while stack:
            #Use a stack to get the current position by popping
            current = stack.pop()
            row, col = current
            
            #If we reach our goal return true
            if maze[row][col] == "G":
                return True
            
            if current not in self.visited:
                self.visited.append(current)
                
                #Search north, south, east, west
                for direction in directions:
                    new_row = current[0] + direction[0]
                    new_col = current[1] + direction[1]
                    
                    if self.checkBounds(new_row, new_col) and (new_row, new_col) not in self.visited:
                            stack.append((new_row, new_col))
                            if maze[row][col] != "S":
                                maze[row][col] = "P"
                        
    
        return False
        
maze = [["S", '.', '.', 'W'],
        ["W", '.', "W", "W"],
        [".", ".", ".", "."],
        ["G", "W", "W", "W"]]

maze_solver = Maze(maze, len(maze[0]), (len(maze[1])))
maze_solver.bfs(maze, 0, 0)
print(maze)

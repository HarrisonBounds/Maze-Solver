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
                
    def bfs(self, maze):
        start = self.findStart(maze)
        queue = [[start]]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            path = queue.pop(0)
            row, col = path[-1]
                        
            if maze[row][col] == "G":
                return path
            
                
            for direction in directions:
                new_row = direction[0] + row
                new_col = direction[1] + col
                
                if self.checkBounds(new_row, new_col) and (new_row, new_col) not in self.visited:
                    new_path = list(path)
                    new_path.append((new_row, new_col))
                    queue.append(new_path)
                

                    
        return False
            
    def dfs(self, maze):
        start = self.findStart(maze)
        stack = [start]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while stack:
            #Use a stack to get the current position by popping
            current = stack.pop()
            row, col = current
            
            print("Current cell", current)

            #If we reach our goal return true
            if maze[row][col] == "G":
                self.visited.append((row, col))
                return self.visited
            
            if current not in self.visited:
                self.visited.append(current)
                
                #Search north, south, east, west
                for direction in directions:
                    new_row = current[0] + direction[0]
                    new_col = current[1] + direction[1]
                    
                    if self.checkBounds(new_row, new_col) and (new_row, new_col) not in self.visited:
                            stack.append((new_row, new_col))
                        
    
        return False
        
maze = [["S", '.', '.', 'W'],
        ["W", '.', "W", "W"],
        [".", ".", ".", "."],
        ["G", "W", "W", "W"]]

maze_solver = Maze(maze, len(maze[0]), (len(maze[1])))
path = maze_solver.bfs(maze)
print(path)

from maze_visualizer import MazeVisualizer
from collections import deque
import numpy as np

class Maze_Solver:
    def __init__(self, maze, rows, cols) -> None:
        self.maze = maze
        self.rows = rows
        self.cols = cols
        self.visited = []
        self.visualizer = MazeVisualizer()
        
    def checkBounds(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] != 1:
            return True
        
    def findStart(self, maze):
        for i in range(len(maze[0])):
            for j in range(len(maze[1])):
                if maze[i][j] == 3:
                    start = (i, j)
                    return start
                
    def bfs(self, maze):
        q = deque()
        start = self.findStart(maze)
        q.append(start)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            path = q.popleft()
            row, col = path[-1]
                        
            if maze[row][col] == 4:
                break
              
            for direction in directions:
                new_row = direction[0] + row
                new_col = direction[1] + col
                
                if self.checkBounds(new_row, new_col) and (new_row, new_col) not in self.visited:
                    new_path = list(path)
                    new_path.append((new_row, new_col))
                    q.append(new_path)
                    
                    if maze[new_row][new_col] != 4 and maze[new_row][new_col] != 3:
                        maze[new_row][new_col] = 7
                    
            self.visualizer.display_single_state(np.matrix(self.maze), interval=0.001)
                

        for x, y in path:
            maze[x][y] = 3
            self.visualizer.display_single_state(np.matrix(self.maze), interval=0.1)
        
        return path
              
        
    def dfs(self, maze):
        start = self.findStart(maze)
        stack = [start]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                
        while stack:
            #Use a stack to get the current position by popping
            current = stack.pop()
            row = current[0]
            col = current[1]

            #If we reach our goal return true
            if maze[row][col] == 4:
                self.visited.append((row, col))
                break
            
            if current not in self.visited:
                self.visited.append(current)
                
                #Search north, south, east, west
                for direction in directions:
                    new_row = current[0] + direction[0]
                    new_col = current[1] + direction[1]
                    
                    if self.checkBounds(new_row, new_col) and (new_row, new_col) not in self.visited:
                        stack.append((new_row, new_col))
                        maze[row][col] = 7
                        
                            
            self.visualizer.display_single_state(np.matrix(self.maze), interval=0.01)
            
        for x, y in self.visited:
            maze[x][y] = 3
            self.visualizer.display_single_state(np.matrix(self.maze), interval=0.1)
        
        return self.visited
                        
        



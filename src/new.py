import json
from maze_visualizer import MazeVisualizer
import numpy as np
from collections import deque

class BFSSolver:
    def __init__(self, maze):
        self.maze = maze
        
        with open('config.json', 'r') as config_file:
            self.config = json.load(config_file)
            
        self.goal = self.config["GOAL"]
        self.start = self.config["START"]
        self.wall = self.config["WALL"]
        self.free = self.config["FREE"]
        
        self.visited = set()
        self.directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        self.maze_length = len(self.maze[0])
        self.maze_width = len(self.maze[1])
        
        self.visualizer = MazeVisualizer()
        self.path = {}

        self.counter = 0

    def findStart(self, maze):
        for i in range(len(maze[0])):
            for j in range(len(maze[1])):
                if maze[i][j] == self.start:
                    start = (i, j)
                    return start
    
    def isValid(self, x, y):
        if 0 <= x < self.maze_length and 0 <= y < self.maze_width and self.maze[x][y] != self.wall:
            return True  
        
    def getNeighbors(self, current):
        neighbors = []
        x = current[0]
        y = current[1]
        
        for direction in self.directions:
            new_x = direction[0]+x
            new_y = direction[1]+y
            if self.isValid(x, y) and (new_x, new_y) not in self.visited: 
                neighbors.append((direction[0]+x, direction[1]+y))
                
        return neighbors
    
    def findShortestPath(self, end, start):
        current = end
        
        while not np.array_equal(current, start):
            print("Here")
            neighbors = self.getNeighbors(current)
            for nx, ny in neighbors:
                min = np.inf
                if self.path[(nx, ny)] < min:
                    min = self.path[(nx, ny)]
                    next_node = (nx, ny)
            current = next_node
            self.maze[current[0]][current[1]] = 3
            
            self.visualizer.display_single_state(self.maze, interval=1.0)
            
        return True
        
    def solver(self, maze):
        start = self.findStart(maze)
        current = start
        queue = deque([current])
        while queue:
            current = queue.popleft()
            self.visited.add(current)
            
            neighbors = self.getNeighbors(current)
            for nx, ny in neighbors:
                if (nx, ny) not in self.visited and self.isValid(nx, ny):
                    if self.maze[nx][ny] == self.goal:
                        self.findShortestPath(maze[nx][ny], start)
                        
                    self.visited.add((nx, ny))
                    queue.append((nx, ny))
                    self.maze[nx][ny] = 7
                    self.path[(nx, ny)] = self.counter
            
            #Update maze every 20 iterations       
            if self.counter % 20 == 0:  
                self.visualizer.display_single_state(self.maze, interval=0.01)
            self.counter += 1
            
        return False
    
    
            
        

                            
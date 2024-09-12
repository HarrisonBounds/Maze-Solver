import numpy as np
from random_generator import *
from visualizer import *
import copy

class DFSMazeSolver:
    def __init__(self, maze):
        self._maze = maze
        self._dim_m = self._maze.shape[0]
        self._dim_n = self._maze.shape[1]
        self._track = np.zeros((self._dim_m, self._dim_n), dtype=int)
        
        # Search for the start position
        for midx in range(self._dim_m):
            for nidx in range(self._dim_n):
                if(maze[midx, nidx]==3):
                    self.start_m_idx = midx
                    self.start_n_idx = nidx
                    
        # Search for the Goal position
        for midx in range(self._dim_m):
            for nidx in range(self._dim_n):
                if(maze[midx, nidx]==4):
                    self.goal_m_idx = midx
                    self.goal_n_idx = nidx
                    
        self._recorded_states = []
        self._succeed = False
        self._track_succeed = False
        self._count = 1
        self.path = []
        self.interval = 0.1
        
        self.vis = MazeVisualizer()
    
    def _is_idx_out_of_boundary(self, midx, nidx):
        if(midx < 0):
            return True
        elif(midx >= self._dim_m):
            return True
        
        if(nidx < 0):
            return True
        elif(nidx >= self._dim_n):
            return True
        
        return False
    
    def _generate_visiting_idx(self, current_midx, current_nidx):
        idx_to_be_visited = [[current_midx, current_nidx+1],
                             [current_midx+1, current_nidx],
                             [current_midx, current_nidx-1],
                             [current_midx-1, current_nidx]]
        
        return idx_to_be_visited

    def search(self):
        # Check if it's near the goal
        # print(self._maze[self._current_m_idx, self._current_n_idx])
        self.vis.display_single_state(self._maze, self.interval)
        # print(self._current_m_idx, self._current_n_idx)
        neighbours = self._generate_visiting_idx(self._current_m_idx, self._current_n_idx)
        for neighbour in neighbours:
            if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                pass
            else:
                if(self._maze[neighbour[0], neighbour[1]] == 4):
                    self._succeed = True
                    self._track[self._current_m_idx, self._current_n_idx] = self._count
        
        # Recursive Search
        for neighbour in neighbours:
            if(self._succeed == False):
                if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                    pass
                else:
                    if(self._maze[neighbour[0], neighbour[1]] == 2):
                        self._maze[neighbour[0], neighbour[1]] = 5
                        # print(self._maze[neighbour[0], neighbour[1]])
                        if(self._maze[self._current_m_idx, self._current_n_idx] != 3):
                            self._maze[self._current_m_idx, self._current_n_idx] = 6
                        self._track[self._current_m_idx, self._current_n_idx] = self._count
                        self._current_m_idx = neighbour[0]
                        self._current_n_idx = neighbour[1]
                        self._count += 1
                        
                        self.search()
                    else:
                        pass
                
    def get_shortest_path(self):
        neighbours = self._generate_visiting_idx(self._current_m_idx, self._current_n_idx)
        for neighbour in neighbours:
            if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                pass
            else:
                if(self._maze[neighbour[0], neighbour[1]] == 3):
                    self._track_succeed = True
                              
        minimum_val = np.inf
        minimum_idx = [self._current_m_idx, self._current_n_idx]
        neighbours = self._generate_visiting_idx(self._current_m_idx, self._current_n_idx)
        if(self._track_succeed == False):
            for neighbour in neighbours:
                if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                    pass
                else:
                    if(self._track[neighbour[0], neighbour[1]] < minimum_val and self._track[neighbour[0], neighbour[1]] > 0):
                        minimum_val = self._track[self._current_m_idx, self._current_n_idx]
                        minimum_idx = [neighbour[0], neighbour[1]]
            self.path.append(minimum_idx)
            self._maze[minimum_idx[0], minimum_idx[1]] = 7
            self.vis.display_single_state(self._maze, self.interval)
    
            self._current_m_idx = minimum_idx[0]
            self._current_n_idx = minimum_idx[1]
            self.get_shortest_path()
                    
    def solve_maze_recursive(self):     
        self._current_m_idx = self.start_m_idx
        self._current_n_idx = self.start_n_idx
        self.search()
        
        # print(self._track)
        # self.vis.display_single_state(self._maze, 5.0)
        
        self._current_m_idx = self.goal_m_idx
        self._current_n_idx = self.goal_n_idx
        
        self.get_shortest_path()
        for idx in self.path:
            self._maze[idx[0], idx[1]] = 7
        self.vis.display_single_state(self._maze, 2.0)
        

class BFSMazeSolver:
    def __init__(self, maze):
        self._maze = maze
        self._dim_m = self._maze.shape[0]
        self._dim_n = self._maze.shape[1]
        self._track = np.zeros((self._dim_m, self._dim_n), dtype=int)
        
        # Search for the start position
        for midx in range(self._dim_m):
            for nidx in range(self._dim_n):
                if(maze[midx, nidx]==3):
                    self.start_m_idx = midx
                    self.start_n_idx = nidx
                    
        # Search for the Goal position
        for midx in range(self._dim_m):
            for nidx in range(self._dim_n):
                if(maze[midx, nidx]==4):
                    self.goal_m_idx = midx
                    self.goal_n_idx = nidx
                    
        self._recorded_states = []
        self._succeed = False
        self._track_succeed = False
        self._count = 1
        self.path = []
        self.interval = 0.05
        
        self.bfscache = []
        
        self.vis = MazeVisualizer()
        
    def _is_idx_out_of_boundary(self, midx, nidx):
        if(midx < 0):
            return True
        elif(midx >= self._dim_m):
            return True
        
        if(nidx < 0):
            return True
        elif(nidx >= self._dim_n):
            return True
        
        return False
    
    def _generate_visiting_idx(self, current_midx, current_nidx):
        idx_to_be_visited = [[current_midx, current_nidx+1],
                             [current_midx+1, current_nidx],
                             [current_midx, current_nidx-1],
                             [current_midx-1, current_nidx]]
        
        return idx_to_be_visited

    def bfssearch(self):
        self.vis.display_single_state(self._maze, self.interval)
        # Check if current bfs cache has a grid near goal
        if(self._succeed == False):
            for current_position in self.bfscache:
                neighbours = self._generate_visiting_idx(current_position[0], current_position[1])
                for neighbour in neighbours:
                    if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                        pass
                    else:
                        if(neighbour[0] == self.goal_m_idx and neighbour[1] == self.goal_n_idx):
                            self._succeed = True
                            
            # Change the state of current bfscache
            for current_position in self.bfscache:
                if(self._is_idx_out_of_boundary(current_position[0], current_position[1])):
                    pass
                else:
                    if(self._maze[current_position[0], current_position[1]] == 2):
                        self._maze[current_position[0], current_position[1]] = 5
                        self._track[current_position[0], current_position[1]] = self._count
                        self._count += 1
                        self.vis.display_single_state(self._maze, self.interval)
                        
                        
            # Update bfscache
            bfscache = copy.deepcopy(self.bfscache)
            original_length = len(bfscache)
            
            for current_position in self.bfscache:
                neighbours = self._generate_visiting_idx(current_position[0], current_position[1])
                for neighbour in neighbours:
                    if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                        pass
                    else:
                        if(self._maze[neighbour[0], neighbour[1]] == 2):
                            bfscache.append([neighbour[0], neighbour[1]])
            self.bfscache = bfscache
            for i in range(original_length):
                if(self._maze[bfscache[0][0], bfscache[0][1]] != 1 and self._maze[bfscache[0][0], bfscache[0][1]] != 3 and self._maze[bfscache[0][0], bfscache[0][1]] != 4):
                    self._maze[bfscache[0][0], bfscache[0][1]] = 6
                self.bfscache.pop(0)
            # print(self.bfscache)
            # print(self._track)
                    
    def get_shortest_path(self):
        neighbours = self._generate_visiting_idx(self._current_m_idx, self._current_n_idx)
        for neighbour in neighbours:
            if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                pass
            else:
                if(self._maze[neighbour[0], neighbour[1]] == 3):
                    self._track_succeed = True
                    
        minimum_val = np.inf
        minimum_idx = [self._current_m_idx, self._current_n_idx]
    
        neighbours = self._generate_visiting_idx(self._current_m_idx, self._current_n_idx)
        if(self._track_succeed == False):
            for neighbour in neighbours:
                if(self._is_idx_out_of_boundary(neighbour[0], neighbour[1])):
                    pass
                else:
                    if(self._track[neighbour[0], neighbour[1]] < minimum_val and self._track[neighbour[0], neighbour[1]] > 0):
                        minimum_val = self._track[self._current_m_idx, self._current_n_idx]
                        minimum_idx = [neighbour[0], neighbour[1]]
            self.path.append(minimum_idx)
            self._maze[minimum_idx[0], minimum_idx[1]] = 7
            self.vis.display_single_state(self._maze, self.interval)
    
            self._current_m_idx = minimum_idx[0]
            self._current_n_idx = minimum_idx[1]
            self.get_shortest_path()
            
                  
    def solve_maze_recursive(self):     
        self._current_m_idx = self.start_m_idx
        self._current_n_idx = self.start_n_idx
        self.bfscache = [[self._current_m_idx, self._current_n_idx]]
        while(self._succeed == False):
        # for i in range(5):
            self.bfssearch()
            
        self._current_m_idx = self.goal_m_idx
        self._current_n_idx = self.goal_n_idx
        # print(self._track)
        self.get_shortest_path()
        for idx in self.path:
            self._maze[idx[0], idx[1]] = 7
        self.vis.display_single_state(self._maze, 2.0)
        
if __name__ == "__main__":        
    rg = RandomGenerator(dim_m=20, dim_n=20)
    maze = rg.generate_random_maze()
            
    # dfsms = DFSMazeSolver(maze)
    # dfsms.solve_maze_recursive()
    
    bfsms = BFSMazeSolver(maze)
    bfsms.solve_maze_recursive()
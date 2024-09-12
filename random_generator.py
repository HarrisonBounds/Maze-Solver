import numpy as np

class RandomGenerator:
    def __init__(self, dim_m=1, dim_n=1):
        self._dim_m = dim_m
        self._dim_n = dim_n
        self._maze = np.zeros((self._dim_m, self._dim_n), dtype=int)
        
        # Register other variables
        self.start_m_idx = None
        self.start_n_idx = None
    
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
        
    def generate_random_maze(self):
        # Generate start point randomly
        rand_m_idx = np.random.randint(0, self._dim_m)
        rand_n_idx = np.random.randint(0, self._dim_n)
        self._maze[rand_m_idx, rand_n_idx] = 3
        self.start_m_idx = rand_m_idx
        self.start_n_idx = rand_n_idx
        
        # Iterating
        out_of_bounds = False
        current_m_idx = self.start_m_idx
        current_n_idx = self.start_n_idx
        count = 0
        minimum_count = int(self._dim_m*self._dim_n/3)
        maximum_count = int(self._dim_m*self._dim_n)
        while(out_of_bounds == False):
            # If it stucks
            if(count > maximum_count):
                # The end point
                if(self._maze[current_m_idx, current_n_idx] != 3):
                    self._maze[current_m_idx, current_n_idx] = 4
                    break
                
            # Generate random next position
            choice = np.random.randint(0, 3+1) #0,1,2,3: n,w,s,e
            if(choice == 0):
                rand_m_increment_idx = -1
                rand_n_increment_idx = 0
            elif(choice == 1):
                rand_m_increment_idx = 0
                rand_n_increment_idx = -1
            elif(choice == 2):
                rand_m_increment_idx = 1
                rand_n_increment_idx = 0
            elif(choice == 3):
                rand_m_increment_idx = 0
                rand_n_increment_idx = 1
            # print(rand_m_increment_idx, rand_n_increment_idx)
            rand_m_idx = current_m_idx + rand_m_increment_idx
            rand_n_idx = current_n_idx + rand_n_increment_idx
            # print("new position: "+str(rand_m_idx)+", "+str(rand_n_idx))
            
            # check if the position is inside the maze
            flag = self._is_idx_out_of_boundary(rand_m_idx, rand_n_idx)
            if(flag):
                if(count<minimum_count):
                    count += 1
                    continue
                else:
                    # The end point
                    if(self._maze[current_m_idx, current_n_idx] != 3):
                        self._maze[current_m_idx, current_n_idx] = 4
                        break
                    else:
                        count += 1
                        continue
            else: # If th eposition is inside the maze
                if(self._maze[rand_m_idx, rand_n_idx] == 0):
                    self._maze[rand_m_idx, rand_n_idx] = 2
                    current_m_idx = rand_m_idx
                    current_n_idx = rand_n_idx
                else:
                    count += 1
                    continue
                
            # self.print_maze()
            # Counting path length
            count += 1
        
        for midx in range(self._dim_m):
            for nidx in range(self._dim_n):
                if(self._maze[midx, nidx] == 0):
                    choice = np.random.randint(0, 1+1) #0,1: wall,free
                    if(choice==0):
                        self._maze[midx, nidx] = 1
                    elif(choice==1):
                        self._maze[midx, nidx] = 2
                        
        return self._maze
            
    
    def print_maze(self):
        print(self._maze)
        
if __name__ == "__main__":
    rg = RandomGenerator(dim_m=5, dim_n=5)
    rg.generate_random_maze()
    rg.print_maze()
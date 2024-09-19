from src.data_structure import GraphNode
from src.state_define import *
import numpy as np
import random

class Maze:
    """
    Pre-defined Graph Node data structure.
    
    Attributes:
        self.num_rows: The number of rows in this 2D matrix maze
        self.num_columns = The number of columns in this 2D matrix maze
        self.num_nodes = The number of grapgh nodes in this 2D matrix maze
        self.state = The node's state for visualizing
        self.score The node's score for finding the shortest path
    """
    def __init__(self, num_rows=1, num_columns=1) -> None:
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.num_nodes = self.num_rows * self.num_columns
        self.start_node_index = 0
        self.goal_node_index = 0
        self.nodes = []
        self.position_to_node_index_table = {}
        self.init_node_to_be_wall_posibility = 0.65
        
        
        # Initialize a 2D graph with Node data structure
        node_index = 0
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                p = [i,j]
                neighbours = [[p[0]-1,p[1]], [p[0],p[1]+1], [p[0]+1,p[1]], [p[0],p[1]-1]]
                neighbours = self._neighbours_filter(neighbours)
                new_node = GraphNode(position=p, index=node_index, neighbours=neighbours, state=INIT)
                self.position_to_node_index_table[str(p)] = node_index
                self.nodes.append(new_node)
                node_index += 1
            
                
    def as_matrix(self):
        matrix = np.zeros((self.num_rows, self.num_columns), dtype=int)
        node_index = 0
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                matrix[i,j] = self.nodes[node_index].state
                node_index += 1
        return matrix
    
    
    def as_nodes(self):
        return self.nodes
    
    
    def init_random_maze_map(self):
        # Generate a random start node
        random_position = self._generate_random_position_within_matrix()
        start_node_index = self.position_to_node_index_table[str(random_position)]
        self.nodes[start_node_index].state = START
        self.start_node_index = start_node_index
        
        # Walk random steps and set FREE nodes
        num_steps = random.randint(1, self.num_rows*self.num_columns-1)
        current_node_index = self.nodes[start_node_index].index
        for i in range(num_steps):
            # Move to a random neighbour
            neighbour_positions = self.nodes[current_node_index].neighbours
            random_neighbour_choice_index = random.randint(0, len(neighbour_positions)-1)
            random_neighbour_position = neighbour_positions[random_neighbour_choice_index]
            random_neighbour_index = self.position_to_node_index_table[str(random_neighbour_position)]
            if(self.nodes[random_neighbour_index].state == INIT or self.nodes[random_neighbour_index].state == FREE):
                current_node_index = random_neighbour_index
                self.nodes[current_node_index].state = FREE
        
        # Set the end node
        self.nodes[current_node_index].state = GOAL
        self.goal_node_index = current_node_index
        
        # Set other nodes from INIT state to WALL and FREE randomly
        for i in range(self.num_nodes):
            if(self.nodes[i].state == INIT):
                choice = random.random()
                if(choice < self.init_node_to_be_wall_posibility): # Is wall
                    self.nodes[i].state = WALL
                else: # Is FREE
                    self.nodes[i].state = FREE
        
        
    def _neighbours_filter(self, position_list):
        # Remove positions out of the maze boundary
        valid_positions = []
        for position in position_list:
            if(position[0] < 0):
                continue
            if(position[0] >= self.num_rows):
                continue
            if(position[1] < 0):
                continue
            if(position[1] >= self.num_columns):
                continue
            valid_positions.append(position)
        return valid_positions
            
            
    def _generate_random_position_within_matrix(self):
        row_index = random.randint(0,self.num_rows-1)
        column_index = random.randint(0,self.num_columns-1)
        return [row_index, column_index]
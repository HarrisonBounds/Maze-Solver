from data_structure import Stack
from maze import Maze
from state_define import *
from maze_visualizer import MazeVisualizer
import numpy as np

class DFSSolver:
    def __init__(self, maze=Maze()) -> None:
        self.maze = maze
        self.visiting_stack = Stack()
        self.visualizer = MazeVisualizer()
            
            
    def find_the_goal(self):
        # Main loop
        self.visiting_stack.push(self.maze.start_node_index)
        found_the_goal = False
        score = 0
        while(found_the_goal == False):
            # Get all neighbours of current visiting nodes and update their states
            visiting_node_index = self.visiting_stack.get_top_element()
            self.maze.nodes[visiting_node_index].score = score
            neighbours = self.maze.nodes[visiting_node_index].neighbours
            num_free_neighbours = 0
            free_neighbour_index = None
            for neighbour_position in neighbours:
                neighbour_index = self.maze.position_to_node_index_table[str(neighbour_position)]
                if(neighbour_index == self.maze.goal_node_index):
                    found_the_goal = True
                if(self.maze.nodes[neighbour_index].state==FREE):
                    num_free_neighbours += 1
                    free_neighbour_index = neighbour_index
            if(num_free_neighbours > 0):
                self.visiting_stack.push(free_neighbour_index)
                self.maze.nodes[free_neighbour_index].state = VISITING
            else:
                visited_node_index = self.visiting_stack.pop()
                if(self.maze.nodes[visited_node_index].state == VISITING):
                    self.maze.nodes[visited_node_index].state = VISITED
            
            self.visualizer.display_single_state(self.maze.as_matrix(), interval=0.01)
            
            # Update score
            score += 1
            
    
    def find_the_shortest_path(self):
        path_node_indices = []
        current_index = self.maze.goal_node_index
        reached_start = False
        while(reached_start == False):
            # Find the neighbour of current node with lowest score
            minimum_score = np.inf
            minimum_index = 0
            neighbours = self.maze.nodes[current_index].neighbours
            for neighbour_position in neighbours:
                neighbour_index = self.maze.position_to_node_index_table[str(neighbour_position)]
                if(self.maze.nodes[neighbour_index].state == VISITING):
                    neighbour_score = self.maze.nodes[neighbour_index].score
                    if(neighbour_score < minimum_score):
                        minimum_index = neighbour_index
                        # print(neighbour_index, minimum_index)
                        minimum_score = neighbour_score
            
            path_node_indices.append(minimum_index)
            self.maze.nodes[minimum_index].state = FINAL_PATH
            current_index = minimum_index
            # self.visualizer.display_single_state(self.maze.as_matrix(), interval=0.01)
            
            # Check if current node has reached the start node
            neighbours = self.maze.nodes[current_index].neighbours
            for neighbour_position in neighbours:
                neighbour_index = self.maze.position_to_node_index_table[str(neighbour_position)]
                if(neighbour_index == self.maze.start_node_index):
                    reached_start = True
            
        self.visualizer.display_single_state(self.maze.as_matrix(), interval=3.0)
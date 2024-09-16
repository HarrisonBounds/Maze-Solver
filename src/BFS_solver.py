from data_structure import Queue
from maze import Maze
from state_define import *
from maze_visualizer import MazeVisualizer
import numpy as np

class BFSSolver:
    def __init__(self, maze=Maze()) -> None:
        self.maze = maze
        self.visiting_queue = Queue()
        self.visualizer = MazeVisualizer()
            
            
    def find_the_goal(self):
        # Main loop
        self.visiting_queue.push(self.maze.start_node_index)
        found_the_goal = False
        score = 0
        while(found_the_goal == False):
            # Check if current stack has nodes adjacent to the goal
            for visiting_node_index in self.visiting_queue.data:
                visiting_node = self.maze.nodes[visiting_node_index]
                neighbours = visiting_node.neighbours
                for neighbour_position in neighbours:
                    neighbour_index = self.maze.position_to_node_index_table[str(neighbour_position)]
                    if(neighbour_index == self.maze.goal_node_index):
                        found_the_goal = True
                
            # Get all neighbours of current visiting nodes and update their states
            num_nodes_in_the_queue = len(self.visiting_queue.data)
            neighbour_indices_to_be_visited = []
            for i in range(num_nodes_in_the_queue):
                visiting_node_index = self.visiting_queue.pop()
                visiting_node = self.maze.nodes[visiting_node_index]
                if(visiting_node.state == VISITING):
                    self.maze.nodes[visiting_node.index].state = VISITED
                neighbours = visiting_node.neighbours
                for neighbour_position in neighbours:
                    neighbour_index = self.maze.position_to_node_index_table[str(neighbour_position)]
                    if(neighbour_index not in neighbour_indices_to_be_visited):
                        # Visit the neighbour and change its state and score
                        if(self.maze.nodes[neighbour_index].state == FREE):
                            self.maze.nodes[neighbour_index].score = score
                            self.maze.nodes[neighbour_index].state = VISITING
                            self.visiting_queue.push(neighbour_index)
                            neighbour_indices_to_be_visited.append(neighbour_index)
            
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
                if(self.maze.nodes[neighbour_index].state == VISITED):
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
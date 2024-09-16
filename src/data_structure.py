import numpy as np

class GraphNode:
    """
    Pre-defined Graph Node data structure.
    
    Attributes:
        self.position: The node's 2D Position in a matrix
        self.index = The node's indenty ID, should be assigned uniquely
        self.neighbours = Indenty IDs of the node's beighbour nodes
        self.state = The node's state for visualizing
        self.score The node's score for finding the shortest path
    """
    def __init__(self, position=[0,0], index=0, neighbours=[], state=-1, score=np.inf) -> None:
        self.position = position # 2D Position in a matrix
        self.index = index # Indenty ID
        self.neighbours = neighbours # Indices of beighbour Nodes
        self.state = state # Every node has a state for visualizing
        self.score = score # Every node has a score for finding the shortest path
        
    def set_neighbours(self, neighbours):
        """
        Set the node's neighbours' indices
        
        Input: Neighbours' indices
        Return: None
        """
        self.neighbours = neighbours


class Stack:
    """
    Pre-defined Stack data structure.
    
    Attributes:
        self.data: The stack data is achieved by a Pyhton List object.
    """
    def __init__(self) -> None:
        self.data = []
        
    def push(self, push_data):
        """
        Push a new element to the top of the stack.
        
        Input: New element
        Return: None
        """
        self.data.append(push_data)
        
    def pop(self):
        """
        Pop the element on the top of the stack.
        
        Input: None
        Return: The poped element on the top of the stack
        """
        return self.data.pop()
    
class Queue:
    """
    Pre-defined Queue data structure.
    
    Attributes:
        self.data: The stack data is achieved by a Pyhton List object.
    """
    def __init__(self) -> None:
        self.data = []
        
    def push(self, push_data):
        """
        Push a new element to the end of the queue.
        
        Input: New element
        Return: None
        """
        self.data.append(push_data)
        
    def pop(self):
        """
        Pop the element on the front of the queue.
        
        Input: None
        Return: The poped element on the front of the queue
        """
        return self.data.pop(0)
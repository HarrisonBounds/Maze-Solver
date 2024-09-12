import numpy as np

example_maze = [[3, 2, 2, 1],
                [1, 2, 1, 1],
                [2, 2, 2, 2],
                [4, 2, 2, 2]]


'''
1: Wall
2: Free
3: Start
4: Goal
'''


def dfs(east, south, west, north):
        if east == 2:
            return "east"
        elif south == 2:
            return "south"
        elif west == 2:
             return "west"
        elif north == 2:
            return "north"
        
        #elif east == 1 or south == 1 or west == 1 or north == 1:
             
for row in range(len(example_maze)):
    for col in range(len(example_maze)):
        current = example_maze[row][col]

        #Get state of maze
        east = example_maze[row][col+1]
        south = example_maze[row+1][col]
        west = example_maze[row][col-1]
        north = example_maze[row-1][col]

        direction = dfs(east, south, west, north)

        if direction == 'east':
            example_maze[row][col+1] = 7
        elif direction == 'south':
             example_maze[row+1][col] = 7
        elif direction == "west":
             example_maze[row][col-1]
        elif direction == "north":
             example_maze[row-1][col]


           

        
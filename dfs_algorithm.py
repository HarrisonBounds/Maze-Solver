example_maze = [[3, 0, 0, 1],
                [1, 0, 1, 1],
                [0, 0, 0, 0],
                [4, 1, 1, 1]]
rows = len(example_maze)
cols = len(example_maze[0])
visited = set()

def dfs(row, col):
    # Check if out of bounds or cell is not traversable or already visited
    if row < 0 or row >= rows or col < 0 or col >= cols or example_maze[row][col] != 0 or (row, col) in visited:
        return
    
    # Mark the cell as visited
    visited.add((row, col))
    
    # Check if out of bounds or cell is not traversable or already visited
    if row < 0 or row >= rows or col < 0 or col >= cols or example_maze[row][col] != 0 or (row, col) in visited:
        return
    
    # Mark the cell as visited
    
    # If we reached the target cell (4 in this case), we can stop
    if example_maze[row][col] == 4:
        example_maze[row][col] = 8
        print("solved maze: ")
        for r in example_maze:
            print(r)
        return

    #EAST
    if example_maze[row][col+1] == 0:
        if visited:
            example_maze[cur[-1][0]][cur[-1][1]] = 8
        
        dfs(row, col+1)
    
    #WEST
    if example_maze[row][col-1] == 0:
        if visited:
            example_maze[cur[-1][0]][cur[-1][1]] = 8
        dfs(row, col+1)
        
    #SOUTH
    if example_maze[row][col-1] == 0:
        if visited:
            example_maze[cur[-1][0]][cur[-1][1]] = 8
        dfs(row, col+1)    
    
dfs(0, 0)
print("solved maze: ")  

# visited = []

# '''
# 1: Wall
# 2: Free
# 3: Start
# 4: Goal
# 7: Visited
# 8: Already visited
# '''

# print("STARTING EXAMPLE MAZE", example_maze)

# def planner():
#     #  pls send the final output as a return type here.
#     #  let me know if you need any current value to your file.
#     print("demo")

# def dfs(example_maze, row, col):
    
        
#         #Bounds checking, and exploring the spaces around the current position
#         if col+1 < len(example_maze):
#             east = example_maze[row][col+1]

#             if east == 0:
#                 cur = (row, col+1)
#                 if cur in visited:
#                     tmp_row = visited[-1][0]
#                     tmp_col = visited[-1][1]
#                     example_maze[tmp_row][tmp_col] = 8
                
#                 visited.append(cur)
                
#                 return

#         if row+1 < len(example_maze):
#              south = example_maze[row+1][col]

#              if south == 0:
#                 cur = (row+1, col)
#                 if cur in visited:
#                     tmp_row = visited[-1][0]
#                     tmp_col = visited[-1][1]
#                     example_maze[tmp_row][tmp_col] = 8
                
#                 visited.append(cur)
                
#                 return
              
#         if col-1 >= 0:
#              west = example_maze[row][col-1]

#              if west == 0:
#                 cur = (row, col+1)
#                 if cur in visited:
#                     tmp_row = visited[-1][0]
#                     tmp_col = visited[-1][1]
#                     example_maze[tmp_row][tmp_col] = 8
                
#                 visited.append(cur)
#                 return

#         if row-1 >= 0:
#             north = example_maze[row-1][col]

#             if north == 0:
#                 cur = (row, col+1)
#                 if cur in visited:
#                     tmp_row = visited[-1][0]
#                     tmp_col = visited[-1][1]
#                     example_maze[tmp_row][tmp_col] = 8
                
#                 visited.append(cur)
               
#                 return
                 
             
# for row in range(len(example_maze)):
#     for col in range(len(example_maze)):

#         dfs(example_maze, row, col)


# print("SOLVED EXAMPLE MAZE:", example_maze)



           

        
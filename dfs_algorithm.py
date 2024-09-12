example_maze = [[3, 2, 2, 1],
                [1, 2, 1, 1],
                [2, 2, 2, 2],
                [4, 2, 2, 2]]

visited = []

'''
1: Wall
2: Free
3: Start
4: Goal
7: Visited
8: Already visited
'''
print("STARTING EXAMPLE MAZE", example_maze)

def planner():
    #  pls send the final output as a return type here.
    #  let me know if you need any current value to your file.
    print("demo")

def dfs(example_maze, row, col, cur):
        
        
        #Bounds checking, and exploring the spaces around the current position
        if col+1 < len(example_maze):
            east = cur

            if example_maze[row][col+1] == 2:
                example_maze[row][col+1] = 7
                visited.append(east)
                return

        if row+1 < len(example_maze):
             south = example_maze[row+1][col]

             if south == 2:
                  example_maze[row+1][col] = 7
                  cur = (row+1, col)
                  visited.append(cur)
                  return
        if col-1 >= 0:
             west = (row, col-1)

             if example_maze[row][col-1] == 2:
                example_maze[row][col-1] = 7
                cur = (row, col-1)
                visited.append(cur)
                return
            
             if west in visited:
                  example_maze[row][col] = 8
                  
                  
                  
                  

        if row-1 >= 0:
            north = example_maze[row-1][col] = 7

            if north == 2:
                 example_maze[row-1][col] = 7
                 cur = (row-1, col)
                 visited.append(cur)
                 return

        if cur in visited:
            example_maze[row][col] = 8
        

            
        
             
             
        
             
for row in range(len(example_maze)):
    for col in range(len(example_maze)):

        
        cur = (row, col)
        dfs(example_maze, row, col, cur)



        # if direction == 'east':
        #     example_maze[row][col+1] = 7
        # elif direction == 'south':
        #      example_maze[row+1][col] = 7
        # elif direction == "west":
        #      example_maze[row][col-1] = 7
        # elif direction == "north":
        #      example_maze[row-1][col] = 7

print("SOLVED EXAMPLE MAZE:", example_maze)



           

        
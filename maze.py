import dfs_algorithm as dfs
import visualizer as viz
import numpy as np

# def updatePos():
#     print("demo")

def displayDebugStat():
    print("demo")

def readMap():
    matrix = np.loadtxt('./MapConfig/exMap.map', delimiter=",")
    return(matrix)

#Main loop
running = True
while (running):
    intialState = readMap() 
    dfs.init(intialState)
    currentMazeState = dfs.planner() #2-D numpy array.
    # # x,y = updatePos()
    visulalizer = viz.MazeVisualizer(currentMazeState)
    visulalizer.display_single_state(currentMazeState)
    visulalizer.play(interval=2.0)
    displayDebugStat()








import algorithms as algo
import visualizer as viz

def updatePos():
    print("demo")

def displayDebugStat():
    print("demo")

def readMap():
    print("demo")


#Main loop
running = True
while (running):

    # intialState = readMap() 
    # dfs.init(intialState)
    currentMazeState = algo.planner() #2-D numpy array.
    # x,y = updatePos()
    visulalizer = viz.MazeVisualizer(currentMazeState)
    visulalizer.display_single_state(currentMazeState)
    visulalizer.play(interval=2.0)

    displayDebugStat()








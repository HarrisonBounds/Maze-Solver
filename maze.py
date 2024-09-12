
import dfs_algorithm as dfs
import visualiser as viz

def updatePos():
    print("demo")

def displayDebugStat():
    print("demo")

def readMap():
    print("demo")


#Main loop
running = True
while (running):

    readMap()   
    dfs.planner()
    x,y = updatePos()
    viz.currentVal(x,y)
    # viz.displayMaz() confirm operation.
    displayDebugStat()








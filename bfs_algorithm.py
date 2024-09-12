import numpy as np

'''
1: Wall
2: Free
3: Start
4: Goal
'''

# class Neighbours():

#     def init(self, position):
#         self.list = list()
#         self.position = position
#     def visiting(flag):
#         self.visit = flag
#     def delete():
#     def add():

        
    # visited - or not
    # visiting/current node - or not

# The final matrix value is a dictionary. Eg: valMat[(0,1)] = 2
class bfs_planner():

    def init(self, goalPos, startPos, initMaze):
        self.goalPos = goalPos 
        self.startPos = startPos 
        self.maze = initMaze
        self.neighbourQueue = list()
        self.valMat = {}
        self.distance = 0
        self.visitedQueue = list()

    #  Need to make changes here, 
    def updateValMat(self, neighbourX, neighbourY, value):
        if (neighbourX, neighbourY) in self.valMat:
            prevVal = self.valMat[(neighbourX, neighbourY)]
            if ( prevVal < value):
                print("skip") # dont skip if visited, skip if distanceis lower than what u want: check if the else is working as it should..
        else:
            self.neighbour.append((neighbourX, neighbourY))
            self.valMat[(neighbourX, neighbourY)] = value

    def suitableNeighbour(self, neighbourX, neighbourY):
        # Assume rows = 4, coulmn = 4
        self.row = 4
        self.coulmn = 4
        if (neighbourX <= self.row and neighbourX > 0 and  neighbourY <= self.coulmn and neighbourY > 0 ):
            
            return(1)  

    def findNeighbours(self, currentNode):

        # Current node: ((neighbourX,neighbourX), distance)
        curNode, distance = currentNode.split()
        curNodeX = curNode[0]
        curNodeY = curNode[1]
        listH = list()
        #################################
        neighbourX = curNodeX + 1
        neighbourY = curNodeY         
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append((neighbourX,neighbourX), distance+1)
            self.updateValMat(neighbourX, neighbourY,distance+1)

        #################################
        neighbourX = curNodeX - 1
        neighbourY = curNodeY
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append((neighbourX,neighbourX), distance+1)
            self.updateValMat(neighbourX, neighbourY,distance+1)

        #################################
        neighbourX = curNodeX 
        neighbourY = curNodeY + 1        
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append((neighbourX,neighbourX), distance+1)
            self.updateValMat(neighbourX, neighbourY,distance+1)


        #################################
        neighbourX = curNodeX 
        neighbourY = curNodeY - 1
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append((neighbourX,neighbourX), distance+1)
            self.updateValMat(neighbourX, neighbourY,distance+1)

        return(list)



    def calc(self, currPos, val):
                
        self.goalPos = currPos
        self.goalPosX = self.goalPos[0]
        self.goalPosY = self.goalPos[1]

        # findNeighbour
        # val = 0

        #################################
        neighbourX = self.goalPosX + 1
        neighbourY = self.goalPosY         
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            self.updateValMat(neighbourX, neighbourY,val+1)

        #################################
        neighbourX = self.goalPosX - 1
        neighbourY = self.goalPosY
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            self.updateValMat(neighbourX, neighbourY,val+1)

        #################################
        neighbourX = self.goalPosX 
        neighbourY = self.goalPosY + 1        
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            self.updateValMat(neighbourX, neighbourY,val+1)


        #################################
        neighbourX = self.goalPosX 
        neighbourY = self.goalPosY - 1
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            self.updateValMat(neighbourX, neighbourY,val+1)

    def planner(self):
        print("later")

if __name__ == "__main__":
    example_maze = [[3, 2, 2, 1],
                [1, 2, 1, 1],
                [2, 2, 2, 2],
                [4, 2, 2, 2]]
    
    # goalPos, startPos, initMaze
    pln = bfs_planner()
    pln.init((1,4),(1,1), example_maze)    
    
 
    if ( len(pln.neighbourQueue) > 0 ):
        currentNode = pln.neighbourQueue[0] # current node: ((neighbourX,neighbourX), distance)
    else:
        currentNode = ((1,4),0)
        print("initial state")
        
    list = pln.findNeighbours(currentNode) 
    pln.visitedQueue.append(currentNode)
    pln.neighbourQueue.pop(0)

    for i in range(len(list)):
        neighbour, distance = list[i].split()
        neighbourX = neighbour[0] 
        neighbourY = neighbour[1]
        # pln.calc((1,4))
        # neighbour queue : ((neighbourX,neighbourX), distance)
        pln.neighbourQueue.append(((neighbourX,neighbourX), distance))
        print(pln.neighbourQueue)




 
    if (len(neighbourQueue) > 0):
        print("hj")

    for i in range(len(neighbours)):
        pln.calc((neighbours[i]))
        # print(neighbours[i])      
    
    # print(pln.neighbour)
    print(pln.valMat)
        

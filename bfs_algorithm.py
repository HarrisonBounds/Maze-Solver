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
        self.neighbour = list() # list of (neighbourX, neighbourY)

    def updateValMat(self, neighbourX, neighbourY, value):
        if (neighbourX, neighbourY) in self.valMat:
            prevVal = self.valMat[(neighbourX, neighbourY)]
            if ( prevVal < value):
                print("skip") # dont skip if visited, skip if distances lower than what u want: check if the else is working as it should..
        else:
            self.valMat[(neighbourX, neighbourY)] = value

    def suitableNeighbour(self, neighbourX, neighbourY):
        # Assuming rows = 4, coulmn = 4
        self.row = 4
        self.coulmn = 4
        if (neighbourX <= self.row and neighbourX > 0 and  neighbourY <= self.coulmn and neighbourY > 0 ):            
            return(1)  

    def findNeighbours(self, currentNode):

        # Current node: (neighbourX, neighbourY, distance)
        print(currentNode)
        print(currentNode[0])
        # curNode, distance =  currentNode[0]
        # curNode = (2,3)
        # distance = 8
        curNodeX, curNodeY, distance = currentNode[0] 
        listH = list()

        #################################
        neighbourX = curNodeX + 1
        neighbourY = curNodeY         
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append([neighbourX, neighbourY, distance+1])
            # self.updateValMat(neighbourX, neighbourY,distance+1)

        #################################
        neighbourX = curNodeX - 1
        neighbourY = curNodeY
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append([neighbourX, neighbourY, distance+1])
            # self.updateValMat(neighbourX, neighbourY,distance+1)

        #################################
        neighbourX = curNodeX 
        neighbourY = curNodeY + 1        
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append([neighbourX, neighbourY, distance+1])
            # self.updateValMat(neighbourX, neighbourY,distance+1)


        #################################
        neighbourX = curNodeX 
        neighbourY = curNodeY - 1
        # find 1 hop neighbour 
        if(self.suitableNeighbour(neighbourX, neighbourY)):
            listH.append([neighbourX, neighbourY, distance+1])
            # self.updateValMat(neighbourX, neighbourY, distance+1)

        return(listH)

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
    listK = list()

    if ( len(pln.neighbourQueue) > 0 ):
        print("Do nothing")
    else:
        print("initial state")
        currentNode = [[1,4,0]]

        listK = pln.findNeighbours(currentNode) 
        if (len(pln.visitedQueue) > 0):
            pln.visitedQueue.append(currentNode)
        else:
            pln.visitedQueue = currentNode   

        # Append all the list neghbour to neighbour queue.
        for i in range(len(listK)):

            pln.neighbourQueue.append(listK[i])
            print("neighbour queue was updated now")
            print(pln.neighbourQueue)

    
    # There needs to be a loop here.
    
    # Calculate current Node.    
    for i in range(len(pln.neighbourQueue)):
        if ( len(pln.neighbourQueue) > 0 ):
            print("non-initial state")   
            print(len(pln.neighbourQueue))         
            curNodeX, curNodeY, distance = pln.neighbourQueue[0]
            currentNode = [[curNodeX, curNodeY, distance]]
            # if current node comes same as goal poae skip tha find neighbour step, as it will gen twice.
            if (currentNode != [[1,4,0]]):
                print(currentNode)
                listK = pln.findNeighbours(currentNode) 
                if (len(pln.visitedQueue) > 0):
                    pln.visitedQueue.append(currentNode)
                else:
                    pln.visitedQueue = currentNode        
            

                #current node: (neighbourX, neighbourY, distance)
                # Append all the list neghbour to neighbour queue.
                for i in range(len(listK)):

                    pln.neighbourQueue.append(listK[i])
                    print("neighbour queue was updated now")
                    print(pln.neighbourQueue)

            neighbourX, neighbourY, distance = pln.neighbourQueue[0]
            pln.updateValMat(neighbourX, neighbourY, distance+1)
            print("neighbour queue before pop")
            print(pln.neighbourQueue)
            pln.neighbourQueue.pop(0)
            print("neighbour queue after pop")
            print(pln.neighbourQueue)


    
    print("debug the val matrix")
    print(pln.valMat)
        

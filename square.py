class Square():
    def __init__(self, val, row, col, isWall):
        self.val = val
        self.row = row
        self.col = col
        self.isWall = isWall
        self.isStart = False
        self.isGoal = False
        self.neighbor_list = [] # can just be a list of indices, not Square objects
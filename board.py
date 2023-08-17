
invalid = -1
empty = 0
black = 1
white = 2
removing_black = 3
removing_white = 4
removed = 5


class board:
    
    def __init__(self):
        self.pieces = [[[]]]
        
    def set_pieces(self):
        self.pieces = [[[empty for j in range(21)] for i in range(21)]]
        for i in range(21): # board borders are invalid, only exist to make searches easier
            self.pieces[0][i] = invalid
            self.pieces[20][i] = invalid
            self.pieces[i][0] = invalid
            self.pieces[i][20] = invalid
            
    def draw:
        pass
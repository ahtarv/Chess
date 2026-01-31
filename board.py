from pieces import Pawn, Rook, Knight


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        
        for col in range(8):
            self.grid[1][col] = Pawn("black")
            self.grid[6][col] = Pawn("white")

        self.grid[0][0] = self.grid[0][7] = Rook("black")
        self.grid[7][0] = self.grid[7][7] = Rook("white")

        self.grid[0][1] = self.grid[0][6] = Knight("black")
        self.grid[7][1] = self.grid[7][6] = Knight("white")

        # self.grid[0][2] = self.grid[0][5] = Bishop("black")
        # self.grid[7][2] = self.grid[7][5] = Bishop("white")

        # self.grid[0][3] = Queen("black")
        # self.grid[7][3] = Queen("white")

        # self.grid[0][4] = King("black")
        # self.grid[7][4] = King("white") 
    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        piece = self.grid[sr][sc]
        self.grid[er][ec] = piece
        self.grid[sr][sc] = None
        piece.has_moved = True

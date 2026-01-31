from pieces import Pawn, Rook, Knight, Bishop, Queen, King


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

        self.grid[0][2] = self.grid[0][5] = Bishop("black")
        self.grid[7][2] = self.grid[7][5] = Bishop("white")

        self.grid[0][3] = Queen("black")
        self.grid[7][3] = Queen("white")

        self.grid[0][4] = King("black")
        self.grid[7][4] = King("white")

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        piece = self.grid[sr][sc]
        self.grid[er][ec] = piece
        self.grid[sr][sc] = None
        piece.has_moved = True

    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece and piece.color == color and piece.__class__.__name__ == "King":
                    return(r,c)
        return None 

    def is_square_attacked(self, row, col, by_color):
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece and piece.color == by_color:
                    moves = piece.get_moves(self.grid, r, c)
                    if (row, col) in moves:
                        return True
        return False

    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return False

        enemy = "black" if color == "white" else "white"
        kr, kc = king_pos
        return self.is_square_attacked(kr, kc, enemy)
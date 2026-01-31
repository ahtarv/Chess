from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def move(self, start, end):
        sr, sc = start
        er, ec = end

        piece = self.board.grid[sr][sc]
        if piece is None or piece.color != self.turn:
            return False

        if end not in piece.get_moves(self.board.grid, sr, sc):
            return False
        

        captured = self.board.grid[er][ec]
        self.board.grid[er][ec] = piece
        self.board.grid[sr][sc] = None

        if self.board.is_in_check(self.turn):
            self.board.grid[sr][sc] = piece
            self.board.grid[er][ec] = captured
            return False

        
        piece.has_moved = True
        self.turn = "black" if self.turn == "white" else "white"
        return True

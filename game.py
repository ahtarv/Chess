from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def move(self, start, end):
        sr, sc = start
        er, ec = end

        piece = self.board.grid[sr][sc]
        if piece is None:
            return False

        if piece.color != self.turn:
            return False

        moves = piece.get_moves(self.board.grid, sr, sc)
        if end not in moves:
            return False

        self.board.move_piece(start, end)
        self.turn = "black" if self.turn == "white" else "white"
        return True

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

        if self.is_checkmate(self.turn):
            print(f"CHECKMATE! {piece.color.capitalize()} wins!")

        return True

    def has_legal_moves(self, color):
        for r in range(8):
            for c in range(8):
                piece = self.board.grid[r][c]
                if piece and piece.color == color:
                    moves = piece.get_moves(self.board.grid, r,c)
                    for er, ec in moves:
                        captured = self.board.grid[er][ec]
                        self.board.grid[er][ec] = piece
                        self.board.grid[r][c] = None

                        in_check = self.board.is_in_check(color)

                        self.board.grid[r][c] = piece
                        self.board.grid[er][ec] = captured

                        if not in_check:
                            return True
        return False    
    
    def is_checkmate(self, color):
        if not self.board.is_in_check(color):
            return False
        return not self.has_legal_moves(color)
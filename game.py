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

        moves = piece.get_moves(self.board.grid, sr, sc)
        if end not in moves:
            return False

        if piece.__class__.__name__ == "King" and abs(ec - sc) == 2:
            step = 1 if ec > sc else -1
            for c in range(sc, ec + step, step):
                captured_inner = self.board.grid[sr][c]
                self.board.grid[sr][sc] = None
                self.board.grid[sr][c] = piece

                if self.board.is_in_check(piece.color):
                    self.board.grid[sr][sc] = piece
                    self.board.grid[sr][c] = captured_inner
                    return False

                self.board.grid[sr][c] = None
                self.board.grid[sr][sc] = piece
        

        captured = self.board.grid[er][ec]
        self.board.grid[er][ec] = piece
        self.board.grid[sr][sc] = None

        # Move Rook if castling
        castling_rook = None
        if piece.__class__.__name__ == "King" and abs(ec - sc) == 2:
            rook_col = 7 if ec > sc else 0
            new_rook_col = ec - 1 if ec > sc else ec + 1
            castling_rook = self.board.grid[sr][rook_col]
            
            self.board.grid[sr][new_rook_col] = castling_rook
            self.board.grid[sr][rook_col] = None

        if self.board.is_in_check(self.turn):
            self.board.grid[sr][sc] = piece
            self.board.grid[er][ec] = captured
            
            # Revert Rook
            if castling_rook:
                rook_col = 7 if ec > sc else 0
                new_rook_col = ec - 1 if ec > sc else ec + 1
                self.board.grid[sr][rook_col] = castling_rook
                self.board.grid[sr][new_rook_col] = None
            return False

        
        piece.has_moved = True
        if castling_rook:
            castling_rook.has_moved = True

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
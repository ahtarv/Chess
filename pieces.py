class Piece:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def get_moves(self, board, row, col):
        raise NotImplementedError

class Pawn(Piece):
    def get_moves(self, board, row, col):
        moves = []
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1

        if board[row+direction][col] is None:
            moves.append((row+direction, col))
            if row == start_row and board[row+2 * direction][col] is None:
                moves.append((row+2*direction, col))

        for dc in (-1,1):
            r = row + direction
            c = col + dc
            if 0 <= r < 8 and 0<= c <8:
                target = board[r][c]
                if target and target.color != self.color:
                    moves.append((r,c))
        return moves
    
class Rook(Piece):
    def get_moves(self, board, row, col):
        moves = []
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                target = board[r][c]
                if target:
                    if target.color != self.color:
                        moves.append((r,c))
                    break
                moves.append((r,c))
                r += dr
                c += dc
        return moves
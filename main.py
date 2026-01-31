from game import Game

def print_board(board):
    for row in board.grid:
        for piece in row:
            if piece is None:
                print(".", end = " ")
            else:
                print(piece.color[0] + piece.__class__.__name__[0], end = " ")
        print()
    print()

game = Game()
print_board(game.board)           

game.board.grid[6][4] = None
game.board.grid[1][4] = None
game.board.move_piece((0,3), (4,7))
print("White in check:", game.board.is_in_check("white"))

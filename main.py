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
# Move white pawn forward
game.board.move_piece((6, 0), (5, 0))
print_board(game.board)

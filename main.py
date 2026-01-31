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

game.move((6,5), (5,5))
game.move((1,4), (3,4))
game.move((6,6), (4,6))
game.move((0,3), (4,7))

print("White in check:", game.board.is_in_check("white"))
print("White in checkmate:", game.is_checkmate("white"))

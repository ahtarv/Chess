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


print("Turn:", game.turn)
print("Move white pawn:", game.move((6,0), (5,0)))
print("Turn:", game.turn)
print("try moving white again:", game.move((6,1), (5,1)))
print("Move black pawn:", game.move((1,0), (2,0)))
print("Turn:", game.turn)

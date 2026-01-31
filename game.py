from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.selected = None
    
    def switch_turn(self):
        self.turn = "black" if self.turn == "white" else "white"

        
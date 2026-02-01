import pygame
from game import Game

import os

PIECE_IMAGES = {}

def load_piece_images():
    pieces = ["P", "R", "N", "B", "Q","K"]
    colors = ["w", "b"]

    for color in colors:
        for piece in pieces:
            path = os.path.join("assets", f"{color}{piece}.png")
            image = pygame.image.load(path)
            PIECE_IMAGES[color + piece] = pygame.transform.scale(image, (SQ_SIZE, SQ_SIZE))

pygame.init()

WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8 

load_piece_images() 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")
font  = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()
game = Game()

selected_square = None
legal_moves = []

def highlight_square(square, color, alpha = 120):
    r,c = square
    s = pygame.Surface((SQ_SIZE, SQ_SIZE))
    s.set_alpha(alpha)
    s.fill(color)
    screen.blit(s, (c * SQ_SIZE, r * SQ_SIZE))

def draw_check_indicator():
    if game.board.is_in_check("white"):
        king_pos = game.board.find_king("white")
        if king_pos:
            highlight_square(king_pos, (255,0,0), alpha=150)
    
    if game.board.is_in_check("black"):
        king_pos = game.board.find_king("black")
        if king_pos:
            highlight_square(king_pos, (255,0,0), alpha = 150)


def get_valid_moves_for_piece(game, row, col):
    piece = game.board.grid[row][col]
    if not piece:
        return []
    
    candidates = piece.get_moves(game.board.grid, row, col)
    valid_moves = []
    for er, ec in candidates:
        # Simulate move
        captured = game.board.grid[er][ec]
        game.board.grid[er][ec] = piece
        game.board.grid[row][col] = None
        
        if not game.board.is_in_check(piece.color):
            valid_moves.append((er, ec))
            
        # Revert
        game.board.grid[row][col] = piece
        game.board.grid[er][ec] = captured
        
    return valid_moves



def highlight_moves(moves):
    for r, c in moves:
        highlight_square((r,c), (0,255,0))

def draw_pieces():
    for r in range(8):
        for c in range(8):
            piece = game.board.grid[r][c]
            if piece:
                color = "w" if piece.color == "white" else "b"
                name = piece.__class__.__name__

                letter = name[0]
                if name == "Knight":
                    letter = "N"
                
                image = PIECE_IMAGES[color + letter]
                screen.blit(image, (c * SQ_SIZE, r * SQ_SIZE))

def draw_board():
    colors = [(240, 217, 181), (181, 136, 99)]
    for r in range(8):
        for c in range(8):
            color = colors[(r+c)%2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // SQ_SIZE
            col = x // SQ_SIZE
            
            if selected_square:
                # If we have a selection, try to move
                if (row, col) in legal_moves:
                    game.move(selected_square, (row, col))
                    selected_square = None
                    legal_moves = []
                else:
                    # If clicking on another own piece, select it
                    piece = game.board.grid[row][col]
                    if piece and piece.color == game.turn:
                        selected_square = (row, col)
                        legal_moves = get_valid_moves_for_piece(game, row, col)
                    else:
                        # Deselect
                        selected_square = None
                        legal_moves = []
            else:
                # Select a piece
                piece = game.board.grid[row][col]
                if piece and piece.color == game.turn:
                    selected_square = (row, col)
                    legal_moves = get_valid_moves_for_piece(game, row, col)

    draw_board()
    
    if selected_square:
        highlight_square(selected_square, (0, 0, 255))
        highlight_moves(legal_moves)
    draw_check_indicator()    
    draw_pieces()
    pygame.display.flip()


pygame.quit()

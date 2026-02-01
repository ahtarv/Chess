import copy

PIECE_VALUES = {
    "Pawn": 100,
    "Knight": 320,
    "Bishop": 330,
    "Rook": 500,
    "Queen": 900,
    "King": 20000   
}

def evaluate_board(board, color):
    score = 0
    for r in range(8):
        for c in range(8):
            piece = board.grid[r][c]
            if piece:
                value = PIECE_VALUES.get(piece.__class__.__name__, 0)
                if piece.color == color:
                    score += value
                else:
                    score -= value
    return score

def get_all_legal_moves(game, color):
    moves = []
    for r in range(8):
        for c in range(8):
            piece = game.board.grid[r][c]
            if piece and piece.color == color:
                candidates = piece.get_moves(game.board.grid, r, c)
                for er, ec in candidates:
                    # Basic validation by simulation
                    # Note: This simple simulation handles general moves 
                    # but assumes game.move will catch complex invalid moves like castling through check
                    captured = game.board.grid[er][ec]
                    game.board.grid[er][ec] = piece
                    game.board.grid[r][c] = None
                    
                    if not game.board.is_in_check(color):
                        moves.append(((r,c), (er,ec)))
                    
                    # Revert
                    game.board.grid[r][c] = piece
                    game.board.grid[er][ec] = captured
    return moves

def minimax(game, depth, alpha, beta, maximizing, ai_color):
    if depth == 0:
        return evaluate_board(game.board, ai_color), None

    current_turn = ai_color if maximizing else ("white" if ai_color == "black" else "black")
    moves = get_all_legal_moves(game, current_turn)

    if not moves:
        if game.board.is_in_check(current_turn):
            return (-float("inf") if maximizing else float("inf")), None
        return 0, None

    best_move = None
    
    if maximizing:
        max_eval = -float("inf")
        for start, end in moves:
            new_game = copy.deepcopy(game)
            if new_game.move(start, end):
                eval, _ = minimax(new_game, depth-1, alpha, beta, False, ai_color)
                
                if eval > max_eval:
                    max_eval = eval
                    best_move = (start, end)
                
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for start, end in moves:
            new_game = copy.deepcopy(game)
            if new_game.move(start, end):
                eval, _ = minimax(new_game, depth-1, alpha, beta, True, ai_color)
                
                if eval < min_eval:
                    min_eval = eval
                    best_move = (start, end)
                
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, best_move

def ai_move(game, color, depth=3):
    print(f"AI is thinking... (depth {depth})")
    _, move = minimax(game, depth, -float("inf"), float("inf"), True, color)
    if move:
        game.move(move[0], move[1])
        print(f"AI moved from {move[0]} to {move[1]}")
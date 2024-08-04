def minimax(board, depth, is_maximizing):
    if game_over(board) or depth == 0:
        return evaluate(board)
    
    if is_maximizing:
        best_score = -float('inf')
        for move in legal_moves(board):
            new_board = make_move(board, move)
            score = minimax(new_board, depth - 1, False)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in legal_moves(board):
            new_board = make_move(board, move)
            score = minimax(new_board, depth - 1, True)
            best_score = min(best_score, score)
        return best_score
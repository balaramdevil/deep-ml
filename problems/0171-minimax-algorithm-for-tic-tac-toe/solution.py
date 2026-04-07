import numpy as np

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i, j] == player for j in range(3)):
            return True
        if all(board[j, i] == player for j in range(3)):
            return True
    if all(board[i, i] == player for i in range(3)):
        return True
    if all(board[i, 2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return not any(board[i, j] == '' for i in range(3) for j in range(3))

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == '']

def minimax(board: np.ndarray, player: str):
    if is_full(board):
        if is_winner(board,player):
            if player == 'X':
                return 10
            else:
                return -10
        else:
            return 0
    moves = get_available_moves(board)
    score = 0
    if player == 'X':
        score = -100
        for j in moves:
            board[j[0]][j[1]] = 'X'
            score = max(score,minimax(board,'O'))
            board[j[0]][j[1]] = ''

    else:
        score = 100
        for j in moves:
            board[j[0]][j[1]] = 'O'
            score = min(score,minimax(board,'X'))
            board[j[0]][j[1]] = ''
    return score    
        


def minimax_tictactoe(board: np.ndarray, player: str) -> tuple:
    """
    Returns the optimal move (row, col) for the given player ('X' or 'O') on the current board using Minimax.
    Args:
        board: 3x3 NumPy array with entries 'X', 'O', or ''
        player: 'X' or 'O'
    Returns:
        Tuple (row, col) for the optimal move
    """
    moves = get_available_moves(board)
    score = 0
    answer = (5,5)
    if player == 'X':
        score = -100
        for j in moves:
            board[j[0]][j[1]] = 'X'
            score_new = max(score,minimax(board,'O'))
            if score_new > score :
                score = score_new
                answer = j
            board[j[0]][j[1]] = ''
    else:
        score = 100
        for j in moves:
            board[j[0]][j[1]] = 'O'
            score_new = min(score,minimax(board,'X'))
            board[j[0]][j[1]] = ''
            if score_new < score:
                score = score_new
                answer = j
    return answer if answer != (5,5) else None
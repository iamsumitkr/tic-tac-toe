"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    cntX = 0
    cntO = 0
    if not terminal(board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    cntX += 1
                elif board[i][j] == "O":
                    cntO += 1
        
        if cntX > cntO:
            return "O"
        else:
            return "O"
    else:
        return "X"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                actions.add((i, j))

    return actions                    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")
    
    new_board = copy.deepcopy(board)
    current_player = player(board)
    new_board[action[0]][action[1]] = current_player
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # No winner
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    return {"X": 1, "O": -1}.get(result, 0)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_value = None
        best_move = None

        for action in actions(board):
            new_board = result(board, action)
            value = min_value(new_board)
            if best_value is None or value > best_value:
                best_value = value
                best_move = action

        return best_move

    elif current_player == O:
        best_value = None
        best_move = None

        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)
            if best_value is None or value < best_value:
                best_value = value
                best_move = action

        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)

    v = None
    for action in actions(board):
        v = max(v, min_value(result(board, action))) if v is not None else min_value(result(board, action))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = None
    for action in actions(board):
        v = min(v, max_value(result(board, action))) if v is not None else max_value(result(board, action))
    return v

N = 8
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def print_board(board):
    for i in range(N):
        for j in range(N):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
def solve(row, board):
    if row == N:
        print("First Solution:")
        print_board(board)
        return True
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(row + 1, board):
                return True
    return False
board = [-1] * N
solve(0, board)
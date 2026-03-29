N = 8
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve(row, board):
    global count
    if row == N:
        count += 1
        return
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(row + 1, board)

board = [-1] * N
# Pre-place queen at (0,3)
board[0] = 3
count = 0
solve(1, board)
print("Solutions with queen at (0,3):", count)
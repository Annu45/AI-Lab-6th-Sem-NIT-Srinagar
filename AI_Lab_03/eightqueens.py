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
    print()
def solve(row, board):
    global count
    if row == N:
        count += 1
        print(f"Solution {count}:")
        print_board(board)
        return
    
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(row + 1, board)
count = 0
board = [-1] * N
solve(0, board)
print("Total solutions:", count)

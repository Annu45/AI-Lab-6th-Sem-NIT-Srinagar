def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve_n_queens(N):
    board = [-1] * N
    count = 0

    def solve(row):
        nonlocal count
        if row == N:
            count += 1
            return
        
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)

    solve(0)
    return count
# Testing

for n in [4, 6, 8, 10, 12]:
    print(f"N = {n}, Solutions = {solve_n_queens(n)}")

    
#N = int(input("Enter value of N: "))

#result = solve_n_queens(N)
#print("Total solutions:", result)  
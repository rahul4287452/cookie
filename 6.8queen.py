N = 8

def print_solution(board):
    for row in board:
        line = ""
        for cell in row:
            line += "Q " if cell else ". "
        print(line)
    print("\n")

def is_safe(board, row, col):
    # Check left side of the current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, col):
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0  # BACKTRACK

    return res

def solve():
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("No solution exists.")
    else:
        print("Solutions displayed above.")

# Run the function
solve()

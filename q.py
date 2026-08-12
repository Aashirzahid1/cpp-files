N = 8

def print_board(board):
    for row in board:
        line = ""
        for col in range(N):
            if col == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def is_safe(position, row, col):
    for i in range(row):
        if (position[i] == col or
            position[i] - i == col - row or
            position[i] + i == col + row):
            return False
    return True

def solve_queens(position, row):
    if row == N:
        print("Solution found:")
        print_board(position)
        return True

    for col in range(N):
        if is_safe(position, row, col):
            position[row] = col

            if solve_queens(position, row + 1):
                return True

    return False

def main():
    position = [-1] * N

    if not solve_queens(position, 0):
        print("No solution exists.")

if __name__ == "__main__":
    main()


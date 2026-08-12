
grid = [
    ['S', '.', 'P', 'W'],
    ['.', '.', '.', '.'],
    ['P', 'P', '.', 'P'],
    ['.', '.', '.', 'G']
]

ROWS = len(grid)
COLS = len(grid[0])

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

path = []

def is_safe(x, y):
    return (
        0 <= x < ROWS
        and 0 <= y < COLS
        and grid[x][y] not in ('P', 'W')
        and not visited[x][y]
    )

def backtrack(x, y):
    if grid[x][y] == 'G':
        path.append((x, y))
        return True

    visited[x][y] = True
    path.append((x, y))

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if is_safe(nx, ny):
            if backtrack(nx, ny):
                return True

    path.pop()
    return False

start_x, start_y = None, None

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == 'S':
            start_x, start_y = i, j
            break

if backtrack(start_x, start_y):
    print("Path to Gold Found:")
    for step in path:
        print(step)
else:
    print("No safe path to Gold found.")


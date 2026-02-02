from collections import deque

def break_bricks(board, x, y):
    q = deque()
    q.append((x, y, board[x][y]))
    board[x][y] = 0

    while q:
        x, y, power = q.popleft()

        for d in range(4):
            for k in range(1, power):
                nx = x + dx[d] * k
                ny = y + dy[d] * k

                if 0 <= nx < height and 0 <= ny < width:
                    if board[nx][ny] > 0:
                        q.append((nx, ny, board[nx][ny]))
                        board[nx][ny] = 0


def gravity(board):
    for col in range(width):
        stack = []

        for row in range(height - 1, -1, -1):
            if board[row][col] > 0:
                stack.append(board[row][col])

        row = height - 1
        for val in stack:
            board[row][col] = val
            row -= 1

        for r in range(row, -1, -1):
            board[r][col] = 0


def dfs(depth, board):
    global result

    if depth == num:
        remain = 0
        for i in range(height):
            for j in range(width):
                if board[i][j] > 0:
                    remain += 1
        result = min(result, remain)
        return

    for col in range(width):
        for row in range(height):
            if board[row][col] > 0:
                new_board = [b[:] for b in board]

                break_bricks(new_board, row, col)
                gravity(new_board)

                dfs(depth + 1, new_board)
                break
        else:
            dfs(depth + 1, board)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1,T+1):
    num, width, height = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(height)]

    result = float('inf')

    dfs(0, grid)
    print(f"#{tc} {result}")

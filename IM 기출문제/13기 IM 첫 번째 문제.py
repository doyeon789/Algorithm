dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

def get_len(x, y):
    candidates = []

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] < grid[x][y]:
                candidates.append((grid[nx][ny], nx, ny))

    if not candidates:
        return 1

    min_val = candidates[0][0]
    nx, ny = candidates[0][1], candidates[0][2]

    for value, x2, y2 in candidates[1:]:
        if value < min_val:
            min_val = value
            nx, ny = x2, y2
    return 1 + get_len(nx, ny)

for tc in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    mx_num = max(map(max, grid))
    ans = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == mx_num:
                ans = max(ans, get_len(i, j))

    print(f"#{tc} {ans}")

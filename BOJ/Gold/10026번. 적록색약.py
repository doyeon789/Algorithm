n = int(input())
picture = [list(input().strip()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False]*n for _ in range(n)]
visited_cb = [[False]*n for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and picture[x][y] == picture[nx][ny]:
                dfs(nx, ny)

def dfs_cb(x, y):
    visited_cb[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and not visited_cb[nx][ny]:
            if picture[x][y] in ('R', 'G') and picture[nx][ny] in ('R', 'G'):
                dfs_cb(nx, ny)
            elif picture[x][y] == picture[nx][ny]:
                dfs_cb(nx, ny)

ans = 0
ans_cb = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans += 1
            dfs(i, j)

for i in range(n):
    for j in range(n):
        if not visited_cb[i][j]:
            ans_cb += 1
            dfs_cb(i, j)

print(ans, ans_cb)

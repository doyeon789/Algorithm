n = int(input())
picture = [list(input().strip()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs_stack(x, y, visited):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and picture[cx][cy] == picture[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

visited = [[False] * n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans += 1
            dfs_stack(i, j, visited)

for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
ans_colorblind = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans_colorblind += 1
            dfs_stack(i, j, visited)

print(ans, ans_colorblind)
            dfs(i, j)

for i in range(n):
    for j in range(n):
        if not visited_cb[i][j]:
            ans_cb += 1
            dfs_cb(i, j)

print(ans, ans_cb)

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q.append((i, j))
            dist[i][j] = 0

while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] != 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    visited[x][y] = True

    if mine_cnt[x][y] != 0:
        return

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and board[nx][ny] == '.':
                dfs(nx, ny)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    mine_cnt = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                mine_cnt[i][j] = -1
                continue
            cnt = 0
            for d in range(8):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] == '*':
                        cnt += 1
            mine_cnt[i][j] = cnt

    visited = [[False] * N for _ in range(N)]
    answer = 0


    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and mine_cnt[i][j] == 0 and not visited[i][j]:
                dfs(i, j)
                answer += 1

    for i in range(N):
        for j in range(N):
            if board[i][j] == '.' and not visited[i][j]:
                answer += 1

    print(f"#{tc} {answer}")

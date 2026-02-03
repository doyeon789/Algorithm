T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, length, cut_used):
    global answer

    answer = max(answer, length)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if mountain[nx][ny] < mountain[x][y]:
                visited[nx][ny] = True
                dfs(nx, ny, length + 1, cut_used)
                visited[nx][ny] = False

            elif not cut_used and mountain[nx][ny] - K < mountain[x][y]:
                original_height = mountain[nx][ny]
                mountain[nx][ny] = mountain[x][y] - 1

                visited[nx][ny] = True
                dfs(nx, ny, length + 1, True)
                visited[nx][ny] = False

                mountain[nx][ny] = original_height


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    max_height = max(map(max, mountain))

    visited = [[False] * N for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_height:
                visited[i][j] = True
                dfs(i, j, 1, False)
                visited[i][j] = False

    print(f"#{tc} {answer}")

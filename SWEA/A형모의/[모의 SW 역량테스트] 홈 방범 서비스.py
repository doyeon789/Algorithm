from collections import deque

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sr, sc):
    global result

    visited = [[-1] * N for _ in range(N)]
    q = deque()

    q.append((sr, sc))
    visited[sr][sc] = 0 

    house_cnt = 0

    if matrix[sr][sc] == 1:
        house_cnt = 1

    cost = 1*1 + 0*0
    if house_cnt * M >= cost:
        result = max(result, house_cnt)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny] != -1:
                continue

            visited[nx][ny] = visited[x][y] + 1
            k = visited[nx][ny] + 1 

            if matrix[nx][ny] == 1:
                house_cnt += 1

            cost = k*k + (k-1)*(k-1)
            if house_cnt * M >= cost:
                result = max(result, house_cnt)

            q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(f"#{tc} {result}")

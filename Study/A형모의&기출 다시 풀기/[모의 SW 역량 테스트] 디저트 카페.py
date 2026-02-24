dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

def dfs(i, j, d, cnt, start_r, start_c, visited):
    global result

    for turn in range(2):  # 직진 or 방향 전환
        nd = (d + turn) % 4
        ni = i + dx[nd]
        nj = j + dy[nd]

        if 0 <= ni < N and 0 <= nj < N:

            # 시작점으로 돌아온 경우
            if (ni, nj) == (start_r, start_c) and nd == 3:
                result = max(result, cnt)
                return

            # 아직 안 먹은 디저트라면
            if matrix[ni][nj] not in visited:
                visited.append(matrix[ni][nj])
                dfs(ni, nj, nd, cnt+1, start_r, start_c, visited)
                visited.pop()


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = -1

    for i in range(N):
        for j in range(N):
            dfs(i, j, 0, 1, i, j, [matrix[i][j]])

    print(f"#{tc} {result}")
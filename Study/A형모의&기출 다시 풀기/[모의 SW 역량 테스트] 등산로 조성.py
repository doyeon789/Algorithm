dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, depth, is_used):
    global result

    result = max(result, depth)

    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]

        if 0 <= ni < N and 0 <= nj < N:
            if not visited[ni][nj]:
                if arr[ni][nj] < arr[i][j]:
                    visited[ni][nj] = True
                    dfs(ni, nj, depth + 1, is_used)
                    visited[ni][nj] = False

                elif not is_used and arr[ni][nj] - K < arr[i][j]:
                    original_height = arr[ni][nj]
                    arr[ni][nj] = arr[i][j] - 1

                    visited[ni][nj] = True
                    dfs(ni, nj, depth + 1, True)
                    visited[ni][nj] = False

                    arr[ni][nj] = original_height


T = int(input())
for tc in range(1,T+1):
    result = 0
    N, K= map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = max(map(max, arr))

    print(max_num)

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_num:
                visited =[[0]*N for _ in range(N)]
                visited[i][j] += 1
                dfs(i, j, 1, False)

    print(f"#{tc} {result}")
"""
1
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
"""
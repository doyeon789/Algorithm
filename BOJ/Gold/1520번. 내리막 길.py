import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i, j):
    if i == N-1 and j == M-1:
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]

    cnt = 0
    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]

        if not(0 <= ni < N and 0 <= nj < M):
            continue
        if matrix[i][j] > matrix[ni][nj]:
            cnt += dfs(ni, nj)

    dp[i][j] = cnt
    return dp[i][j]

N ,M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1]*M for _ in range(N)]

print(dfs(0,0))
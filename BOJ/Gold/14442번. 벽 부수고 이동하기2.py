from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
visited = [[[0]*(K+1) for _ in range(M)] for __ in range(N)]
arr = [list(map(int, input().strip())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append([0,0,K])
    visited[0][0][K] = 1
    while q:
        r,c,k = q.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c][k]
        for d in range(4):
            ni = r + dx[d]
            nj = c + dy[d]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and  k > 0 and not visited[ni][nj][k-1]:
                    visited[ni][nj][k-1] = visited[r][c][k] + 1
                    q.append([ni, nj, k-1])
                elif arr[ni][nj] == 0 and not visited[ni][nj][k]:
                    visited[ni][nj][k] = visited[r][c][k]+1
                    q.append([ni, nj, k])
    return -1
print(bfs())
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start][0] = True

    while q:
        x, t = q.popleft()

        NK = K + t*(t+1)//2
        if NK > MAX:
            return -1

        if visited[NK][t % 2]:
            return t

        for nx in (x-1, x+1, x*2):
            nt = t + 1
            if 0 <= nx <= MAX and not visited[nx][nt % 2]:
                visited[nx][nt % 2] = True
                q.append((nx, nt))

    return -1


N, K = map(int, input().split())

MAX = 500000
visited = [[False]*2 for _ in range(MAX+1)]

print(bfs(N))
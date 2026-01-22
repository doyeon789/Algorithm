from collections import deque

n, k = map(int, input().split())

MAX = 200000
visited = [False] * (MAX + 1)

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        x, t = q.popleft()

        if x == k:
            return t

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = True
                q.append((nx, t+1))

print(bfs(n))

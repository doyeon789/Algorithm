from collections import deque


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        x, t = q.popleft()

        if x == K:
            print(t)
            break
        
        for nx in (x*2, x-1, x+1):
            if 0 <= nx <= MAX and not visited[nx]:
                if nx == x*2:
                    q.append((nx, t))
                    visited[nx] = True
                else:
                    q.append((nx, t+1))
                    visited[nx] = True

N, K = map(int, input().split())

MAX = 100000
visited = [False] * (MAX + 1)

bfs(N)

from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited_dfs[next_v]:
            dfs(next_v)

def bfs(start):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next_v in graph[v]:
            if not visited_bfs[next_v]:
                visited_bfs[next_v] = True
                queue.append(next_v)

dfs(v)
print()
bfs(v)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, d):
    visited[x] = True
    depth[x] = d
    for nxt in graph[x]:
        if visited[nxt]:
            continue
        parent[nxt] = x
        dfs(nxt, d+1)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


n = int(input())

parent = [0] * (n+1)
depth = [0] * (n+1)
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
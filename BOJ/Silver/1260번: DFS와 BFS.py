n, m , v = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
print(graph)

visited1 = [False]*(n+1)
visited12 = visited1.copy()


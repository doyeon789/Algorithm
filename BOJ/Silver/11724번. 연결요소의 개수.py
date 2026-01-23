def dfs(start):
    visited[start] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)
    return


Vertex , Edge = map(int, input().split())

visited = [False]*(Vertex+1)

graph = [[] for _ in range(Vertex+1)]
for _ in range(Edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

for i in range(1,Vertex+1):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)

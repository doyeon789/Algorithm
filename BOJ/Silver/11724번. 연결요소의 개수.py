from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)
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
        bfs(i)
        count += 1

print(count)

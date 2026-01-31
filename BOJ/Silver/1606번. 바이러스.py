computer = int(input())
connect = int(input())

graph = [[] for _ in range(computer+1)]

for _ in range(connect):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

visited = [False] * (computer+1)

def dfs(n):
    global count
    for d in graph[n]:
        if not visited[d]:
            visited[d] = True
            count += 1
            dfs(d)

visited[1] = True
dfs(1)

print(count)

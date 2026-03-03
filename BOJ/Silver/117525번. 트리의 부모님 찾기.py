import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)
 

N = int(sys.stdin.readline())
 
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
visited = [0]*(N+1) 

dfs(1)
 
for x in range(2, N+1):
    print(visited[x])
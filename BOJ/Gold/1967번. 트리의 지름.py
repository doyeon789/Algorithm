import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

def dfs(x, distance):
    for i, w in graph[x]:
        if visited[i] == -1:
            visited[i] = distance + w
            dfs(i, distance + w)

visited = [-1] * (N+1)
visited[1] = 0 
dfs(1, 0)
max_distance = max(visited)
max_node = visited.index(max_distance)

visited = [-1] * (N+1)
visited[max_node] = 0 
dfs(max_node, 0)

print(max(visited))
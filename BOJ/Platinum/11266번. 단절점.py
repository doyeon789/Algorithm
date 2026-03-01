import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(now, last):
    global id
    
    visited[now] = ID[now] = id
    cnt = 0
    check = 0
    
    for next in graph[now]:
        if next == last:
            continue
        
        if ID[next]:
            visited[now] = min(visited[now], ID[next])
        
        else:
            cnt += 1
            id += 1
            DFS(next, now)
            
            visited[now] = min(visited[now], visited[next])
            
            if visited[next] >= ID[now]:
                check = 1
    
    if (last != now and check) or (last == now and cnt > 1):
        point.append(now)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
ID = [0] * (N+1)

point = []

for i in range(1, N+1):
    if not ID[i]:
        id = 1
        DFS(i, i)

print(len(point))
if point:
    print(*sorted(set(point)))
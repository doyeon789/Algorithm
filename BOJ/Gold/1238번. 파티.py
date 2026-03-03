import sys
import heapq
input = sys.stdin.readline

INF = float("inf")
def dijkstra(start):
    distance = [INF]*(N+1) 
    distance[start] = 0

    q = []

    heapq.heappush(q,(0,start))

    while q:
        d, current = heapq.heappop(q)
        
        if distance[current] < d:
            continue

        for node, cost in graph[current]:
            new_cost = d + cost
        
            if new_cost < distance[node]:
                distance[node] = new_cost 
                heapq.heappush(q,(new_cost,node))
    return distance


N, M, X = map(int,input().split())

graph = [[] for _ in range(N+1)]
total_length = [0]*(N+1)
for _ in range(M):
    start, end, t = map(int,input().split())
    graph[start].append((end,t))

for i in range(1,N+1):
    go = dijkstra(i)
    total_length[i] = go[X]

back = dijkstra(X)

for i in range(1,N+1):
    total_length[i] += back[i]

print(max(total_length[1:]))
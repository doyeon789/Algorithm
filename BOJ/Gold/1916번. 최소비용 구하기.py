import heapq

N = int(input()) 
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(graph, start):
    distances = [int(1e9)] * (N+1)
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [distances[start], start])

    while pq:
        dist, node = heapq.heappop(pq)
        
        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(pq, [distance, next_node]) 
    return distances

dist_start = dijkstra(graph, start)
print(dist_start[end])
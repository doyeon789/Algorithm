# <[ 다익스트라 알고리즘 ]>
# 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산한다.
# 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 떄 정상적으로 동작한다.
# 다익스트라 알고리즘은 최단 경롤르 구하는 과정에서 각 노드에 대한 현재까지의 최단 거리 정보를
#    항상 1차원 리스트에 저장하며 리스트를 계속 갱신한다는 특징이 있다

# < 알고리즘 원리 >
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화 한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3번과 4번을 반복한다.

"""
def dijkstra():

    dist = [[INF] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    dist[0][0] = 0
    
    for _ in range(N * N):
        
        # 방문 안 한 정점 중 최소 dist 찾기
        min_cost = INF
        min_x, min_y = -1, -1
        
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and dist[i][j] < min_cost:
                    min_cost = dist[i][j]
                    min_x, min_y = i, j
        
        # 선택한 정점 방문 처리
        visited[min_x][min_y] = True
        
        # 인접 정점 갱신
        for nx, ny in 인접한_정점들:
            
            new_cost = dist[min_x][min_y] + 이동비용
            
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
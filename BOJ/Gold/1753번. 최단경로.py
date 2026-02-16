import sys
import heapq  # 우선순위 큐 사용

input = sys.stdin.readline  # 빠른 입력 (E가 최대 300,000이라 필수)

# 정점 개수 V, 간선 개수 E
V, E = map(int, input().split())

# 시작 정점
K = int(input())

# 그래프를 인접 리스트로 생성
# 1번부터 V번까지 사용하므로 V+1 크기로 생성
graph = [[] for _ in range(V + 1)]

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # u -> v 로 가는 가중치 w 저장
    graph[u].append((v, w))

# 무한대 설정 (처음엔 모두 도달 불가능하다고 가정)
INF = float('inf')

# 각 정점까지의 최단 거리 저장 배열
dist = [INF] * (V + 1)

# 시작점은 자기 자신까지 거리 0
dist[K] = 0

# 우선순위 큐 생성
# (현재까지 거리, 정점번호) 형태로 저장
pq = []
heapq.heappush(pq, (0, K))

# 다익스트라 시작
while pq:
    # 가장 거리가 짧은 정점 꺼내기
    current_dist, now = heapq.heappop(pq)

    # 이미 더 짧은 거리로 처리된 적 있으면 무시
    if dist[now] < current_dist:
        continue

    # 현재 정점에서 갈 수 있는 모든 간선 탐색
    for next_node, weight in graph[now]:

        # 현재까지 거리 + 다음 간선 가중치
        cost = current_dist + weight

        # 더 짧은 경로 발견하면 갱신
        if cost < dist[next_node]:
            dist[next_node] = cost
            heapq.heappush(pq, (cost, next_node))

# 결과 출력
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")  # 도달 불가능
    else:
        print(dist[i])

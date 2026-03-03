# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 알고리즘
# 소스가 다익스타라에 비해 매우 짧아 구현이 쉽다.
# 다익스타라의 경우 최단 거리를 가지는 노드를 하나씩 반복적으로 선택한다.
#   이후 해당 노드를 거쳐가는 경롤르확인하며 최단 거리 테이블을 갱신하는 방식으로 동작한다.
#   플로이드 워셜 알고리즘 또한 단계마다 '거쳐 가느 노드'를 기준으로 알고리즘을 수행한다.
#   하지만, 매 단계마다 방문하지 않은 노드 중에서 가장 최단 거리르 갖는 노드를 찾을 필요가 없다.
# 플로이드 워셜은 2차원 테이블에 최단 거리 정보를 저장한다.

# Dab - min(Dab, Dak + Dkb)

import sys
input = sys.stdin.readline
INF = float('inf')

# 노드의 개수(n)와 간선의 개수(m)입력
n = int(input())
m = int(input())

# 2차원 리스트 (그래프 표현) 만들고, 무한대로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a== b:
            graph[a][b] == 0
    
# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a -> b로 가는 비용을 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 플로이드워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INF', end=' ')
        else:
            print(graph[a][b], end = ' ')
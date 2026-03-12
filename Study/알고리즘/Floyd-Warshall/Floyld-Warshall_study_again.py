# Floyd-Warshall Algorithm
# 모든 정점 쌍 간의 최단 경로를 구하는 알고리즘
# 동적 프로그래밍을 사용한 최단 경로 점진적으로 갱신
# 음수 가중치가 있어도 정상적으로 동작 (음수 사이클은 X)


# 동작원리
# 동적 계획 알고리즘으로 모든 쌍 최단 경로 문제들을 찾아야 한다.
# 이를 위해 일단 그래프 최단 정점의 수가 적을 때를 생각해보다.
# 그래프 3개의 점정점이 있는 경우, 정점 i에서 정점 j까지의 최단 경로를 찾으려면 2가지 경로,
#   즉, 정점 i에서 정점 j로 직접 가는 경로와 정점 1을 경유하느 경로중에서 짧은 것을 선택하면 된다.
# 또한 하나의 중요하 ㄴ아이디어는 경우 가능한 정점들을 정점1로부터 시작하여, 정덤1과 2, 그다음에는 정점 1,2,3 으로 하나씩 추가하ㅕ, 마지막에는 정점 1~n 까지의 모든 정점을 경유 가능한 정점들로 고려하면서, 모드 쌍의 최단 경로의 거리르 구한다. (dp)
# 부분 문제 정의: 단, 입력 그래프의 정점을 각 1,2,3,---n이라 하자.
#  Dij(^k) = 정ㅈ덤 {1,2,3...k}만 경유 가능한 정점들로 ㄱ려하여, 정점 i로부터 정점 j까지의 모든 경로 중에서 가장 짧은 경로 거리 
# 여기서 k != i, k != j, k = 0인 경우, 정점은 0은 그래프에 없으므로 어떤 정점도 경유하지 않는 다는 것을 의미, 따라서 Dij(^0)은 입력으로 주어지는 간선 (i,j)의 가중치 이다.
# 따라서 모든 쌍 i와 j에 대하여 Dij(^1)을 계산 하는 것이 가장 작은 부분 문제들이다.
# 그 다음엔 i에서 정점 2를 경우하여 j로 가는 경로 거리와 Dij(^1)중에서 짧은 거리를 Dij(^2)로 정한다.
# 단. 정덤2를 경우하는 경로의 거리는 Di2(^1)+D2j(^1)
# 모든 쌍 i와 j에 대하여 Dij(^2) 를 계산 하는 거싱 그 다음으로 큰 문제들이다.
# k를 계속 늘려 정점 i에서 정점 k를 경유하여 j로 가는 경로의 거리와 Dij(k-1)중에서 짧은 거리를 Dij(^k)로 정한다.
# 단,정점 k를 경유하는 경로의거리는 Dik(^k-1) + Dkj(^k-1).
# 이런 방식으로 k가 1에서 n이 될때 까지 Dij(^k)를 계산해서, Dij(^n), 즉, 모든 정점을 경유 가능한 정점들로 고려한 모든 쌍 i와 j의 최단 경로의 거리를 찾는 방식.

# 결론 : 모든 정점까지의 도달하는 최단 거리를 모두 구한 것

INF = float('inf')
def floyd_warshall(graph):
    v_len = len(graph)
    dist = [[INF] * v_len for _ in range(v_len)]

    for i in range(v_len):
        dist[i][i] = 0
    
    for u in range(v_len):
        for v in range(v_len):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]

    for k in range(v_len):
        for i in range(v_len):
            for j in range(v_len):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = [
    [0,3,INF,INF,INF,INF],
    [INF,0,1,INF,INF,INF],
    [INF,INF,0,7,INF,INF],
    [INF,INF,INF,0,INF,3],
    [INF,INF,-4,2,0,INF],
    [INF,INF,INF,INF,1,0],
]

result = floyd_warshall(graph)

for row in result:
    print(row)
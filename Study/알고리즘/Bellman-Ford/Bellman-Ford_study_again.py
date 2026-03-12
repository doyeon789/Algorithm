# Bellman-FOrd Algorithm
# 시작 정점에서 다른 모든 정점으로의 최단 경로를 구하는 알고리즘
# 음수 가중치를 갖는 간선이 있는 그래프에서도 동작
# 다익스트라 알고리즘과 달리, 탐욕 기법 대신 dp접근을 사용
# 우선순위 큐를 사용 안함

# 동작 순서
# 1. 시작 정점에서 각 정점까지의 최단 거리르 ㄹ저장할 리스트 생성
#    (모든 거리를 무한대로 초기화하고, 시작 정점의 거리는 0으로 설정)
# 2. 모든 정점을 반복해서 검사하고, 각 간선을 통해 더 짧은 경로가 발견되면 거리를 업데이트
# 3. 마지막 정점을 제외한 모든 정점에 대해서 2번 과정 반복(v-1번 탐색)
# 4. 마지막으로 한 번더 모든 간선을 검사하여 거리가 갱신되면, 음수 사이클이 존재한다는 것을 의미

def bellman_ford(graph,start):
    v_count = len(graph)
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    for i in range(v_count - 1):
        updated = False
        for u in graph:
            for v, weight in graph[u].items():
                if distances[v] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    updated = True
        if not updated:
            break

    for u in graph:
        for v, weight in graph[u].items(i):
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return "음수 사이클 발생"
            
    return distances

graph = {
    'a' : {'b': 3, 'c': 5},
    'b' : {'c': 2},
    'c' : {'b': 1, 'd': 4, 'e': 6},
    'd' : {'e': 2, 'f': 3},
    'f' : {}
}

start_vertex = 'A'

result = bellman_ford(graph, start_vertex)

print(f"{start_vertex} : {result}")
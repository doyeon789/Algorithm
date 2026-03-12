import heapq

def dijkstra(graph, start):
    """
    1. 모든 정점까지의 거리르 무한대로 초기화 한다.
    2. 시작정점은 0 거리로 세팅한다.
    3. 시작정점을 우선순위 큐에 너혹, 우선순위큐에 있느 정점을 하나씩 빼면서 최단거리를 갱신한다.(우선순위 큐가 빌 때 까지)
        3.1 ) 현재 정점까지의 거리가 이미 갱신된 거리보다 크면 skip
        3.2 ) 방문할 가치가 있는 정점의 인접한 정점까지의 거리를 확인한다.
        3.3 ) 최단거리가 갱신된다면, 갱시 후 우선순위 큐에 삽입한다.    
    """
    distance_dict = {v: float('inf') for v in graph}
    distance[start] = 0 # 시작 정점까지 도달 거리는 0으로 설정
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        cnt_dist, cnt_v = heapq.heappop(heap)

        # 꺼낸 정점의 도달 거리가 확인하려고 정점의 거리보다 크면, 굳이 화인할 필요가 없다.
        if distance_dict[cnt_v] <  cnt_dist: 
            continue
        
        # 인접한 노드들의 거리를 확인해서 최단거리를 갱신하자.
        for adj_v, dist in graph[cnt_v].items():
            distance = cnt_dist  + dist
            if distance < distance_dict[adj_v]:
                distance_dict[adj_v] = distance
                heapq.heappush(heap, [distance, adj_v])

    return distance_dict



graph = {
    'a' : {'b': 3, 'c': 5},
    'b' : {'c': 2},
    'c' : {'b': 1, 'd': 4, 'e': 6},
    'd' : {'e': 2, 'f': 3},
    'f' : {}
}


# 그래프가 주어지고,
# 출발지점에서 도착지점까지 이동하는데, 반드시 c와d를 거쳐서 이동할때의 최단거리를 구해라.
"""
출발 -> c -> d -> 도착
 (출발->c 최단거리, c->d 최단거리, d-> 도착까지 최단거리)
출발 -> d -> c -> 도착 
 (출발->d 최단거리, d->c 최단거리, c-> 도착까지 최단거리)

"""
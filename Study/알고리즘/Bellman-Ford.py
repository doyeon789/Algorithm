# < [벤만-포드 알고리즘] >
# 특정 출발 노드에서 다른 모든 노까지의 최단 경로 탐색
# 음수 가중치에 에지가 있어도 수행 ㄱㄴ
# 전체 그래프에서 음수 사이클의 존재 여부를 판단 할 수 있음.
# 시간 복잡도 O(VE)

# < 알고리즘 수행 과정>
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 다음과정을 노드개수-1번 반복한다.
#   1) 전체 간선 E개를 하나씩 확인.
#   2) 각 간선을 거쳐 다른 노드로 가는 비용을 계한하여 최단 거리 테이블을 갱신한다.
#       -> 출발 노드가 방문한 적 없는 노드(출발거리 == INF)일때 값을 업데이트 X
#       -> 출발 노드의 거리 리스트값+에지 가중치 < 종료 노드의 거리 리스트 값일때 
#          종료 노드의 거리 리스트 값을 없데이트한다.
# 4. 만약 음수 간선 순환이 발생하는지 체크 하고 싶다면 3번의 과정을 한번더 수행한다.

"""
n(노드 개수), m(에지 개수)
edges(에지 정보 저장 리스트)
distance(거리 리스트) #무한으로 초기화

for 에지 개수만큼 반복
    (s, e, w) # 에지 리스트에 에지 정보 저장

# 벨만 포드 수행
거리 리스트에 출발 노드 0으로 초기화

for 에지 개수 만큼 반복
    현재 에지 데이터 가져오기
    if 출발노드가 무한대가 아니고 종료 노드값 < 출발 노드 값 + 에지 가중치:
        업데이트 수행 -> 조료 노드 값 = 출발 노드 값 + 에지 가중치
        if n 번째 라운드:
            음수 사이클 존재

음수 사이클이 존재하면 -1출력
음수 사이클이 존재하지 않으면 -> 거리 리스트 출력
"""

import sys
input = sys.stdin.readline
INF = float('inf')

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보르 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번째 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a, b, c))

def bf(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 n-1번 라운드(round)반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False

#벨만 포드 알고리즘을 수행
negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우,  -1을 출력
        if distance[i] == INF:
            print(-1)
        # 도달할 수 있느 ㄴ경우 거리를 출력
        else:
            print(distance[i])
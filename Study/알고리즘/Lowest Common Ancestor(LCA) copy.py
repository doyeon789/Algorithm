# [Lowest Common Ancestor]
# LCA알고리즘은 트리에서 주어진 두개의 노드의 최소 공통 조상을 찾는 알고리즘이다.

# (간단한 LCA)
# O(N)
# 1. 루트 노드를 기준으로 dfs를 통해 각 노드의 트리 높이와 부모 노드를 저장해준다.
# 2. 두 노드의 높이를 맞춰준다.
# 3. 부모 노드가 일치할때까지 각 노드의 부모노드로 이동시켜준다.

# (LCA + DP)
# O(logN)
# dp[a][b]: a노드에서 2^b번째 노드

# 1. dp배열의 2번째 인덱스 최대값 구하기
""" 
#2번째인자 b는 2^b가 트리의 높이가 되므로 높이가 N일때 최대 b가 된다.
def getMaxIndex():
    return int(ceil(math.log(N)/math.log(2))) + 1
"""
# 2. dfs탐색을 통해 각 노드의 높이와 1번째 (2^0)부모 노드값 초기화 해주기
"""
def dfs(cur, h, parent):
    depth[cur] = h
    dp[cur][0] = parent   # 2^0 부모 설정

    for nxt in graph[cur]:
        if nxt == parent:
            continue
        dfs(nxt, h+1, cur)
"""
# 3. 나머지 dp테이블 채우기
"""
# dp[index][a] = index노드의 2^a번째 부모노드이다.
# 2^a = 2^(a-1) + 2^(a-1)이므로 DP[index][a] = DP[DP[index][a-1]][a-1] 이라는 점화식이 도출된다.
def fill_dp():
    for i in range(1, max_ind):
        for node in range(1, N+1):
            dp[node][i] = dp[dp[node][i-1]][i-1]
"""
# 4. LCA 구하기
#  1) 두 노드의 높이 맞춰주기
#  2) 두 노드를 최소 공통 조상 자식 노드들까지 동시에 업데이트시킨다.
#  3) 긱 노드의 부모노드가 최소 공통 조상 노드가 된다.
"""
def lca(a, b):
    # depth[a] >= depth[b] 로 맞추기
    if depth[a] < depth[b]:
        a, b = b, a

    # 깊이 맞추기
    diff = depth[a] - depth[b]
    for i in range(max_ind-1, -1, -1):
        if diff & (1 << i):
            a = dp[a][i]

    if a == b:
        return a

    # 동시에 위로 올리기
    for i in range(max_ind-1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]

    # 부모가 LCA
    return dp[a][0]
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import math

N = int(input())

# 인접 리스트
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dp 배열의 두 번째 인덱스 최대값 (log2(N))
max_ind = math.ceil(math.log2(N)) + 1

# dp[node][i] = node의 2^i번째 부모
dp = [[0] * max_ind for _ in range(N+1)]

# depth 배열
depth = [0] * (N+1)

# 1. DFS로 depth와 2^0 부모 초기화
def dfs(cur, h, parent):
    depth[cur] = h
    dp[cur][0] = parent

    for nxt in graph[cur]:
        if nxt == parent:
            continue
        dfs(nxt, h+1, cur)

# 루트를 1번으로 설정 (문제에 따라 변경 가능)
dfs(1, 0, 0)

# 2. DP 테이블 채우기
for i in range(1, max_ind):
    for node in range(1, N+1):
        dp[node][i] = dp[dp[node][i-1]][i-1]

# 3. LCA 함수
def lca(a, b):

    # depth[a] >= depth[b]로 맞추기
    if depth[a] < depth[b]:
        a, b = b, a

    # 1. 깊이 맞추기
    diff = depth[a] - depth[b]
    for i in range(max_ind-1, -1, -1):
        if diff & (1 << i):
            a = dp[a][i]

    # 이미 같은 노드면 반환
    if a == b:
        return a

    # 2. 동시에 위로 올리기
    for i in range(max_ind-1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]

    # 3. 부모가 LCA
    return dp[a][0]


# --------------------------
# LCA 질의 처리 예시
# --------------------------
M = int(input())  # LCA 질의 개수
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
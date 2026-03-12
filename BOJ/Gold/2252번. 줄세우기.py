import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
q = deque()
result = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    result.append(v)
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
print(*result)
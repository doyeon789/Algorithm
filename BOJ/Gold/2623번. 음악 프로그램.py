from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    temp = list(map(int, input().split()))
    for i in range(len(temp)-2):
        graph[temp[i+1]].append(temp[i+2])
        indegree[temp[i+2]] += 1

result = []
q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

if len(result) != N:
    print(0)
else:
    for n in result:
        print(n)

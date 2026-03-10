from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
res = []

for _ in range(T):
    n, k = map(int, input().split())
    time = [0]  + list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    dp = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        temp = q.popleft()
        for i in graph[temp]:
            indegree[i] -= 1
            dp[i] = max(dp[temp] + time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

    w = int(input())
    res.append(dp[w])

for i in res:
    print(i)
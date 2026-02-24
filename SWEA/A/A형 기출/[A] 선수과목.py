from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    semester = [0]*(N+1)
    
    for i in range(1, N+1):
        arr = list(map(int, input().split()))
        
        if arr[0] != 0:
            for pre in arr[1:]:
                graph[pre].append(i)
                indegree[i] += 1
    
    q = deque()
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            semester[i] = 1
    
    count = 0
    
    while q:
        now = q.popleft()
        count += 1
        
        for nxt in graph[now]:
            indegree[nxt] -= 1
            semester[nxt] = max(semester[nxt], semester[now] + 1)
            
            if indegree[nxt] == 0:
                q.append(nxt)
    
    if count != N:
        print(f"#{tc} -1")
    else:
        print(f"#{tc} {max(semester)}")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
visited = [False] * N

def dfs():
    if len(result) == M:
        print(*result)
        return
    
    prev = 0
    
    for i in range(N):
        if not visited[i] and arr[i] != prev:
            visited[i] = True
            result.append(arr[i])
            prev = arr[i]
            
            dfs()
            
            visited[i] = False
            result.pop()

dfs()
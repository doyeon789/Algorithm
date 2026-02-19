N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []

def dfs(start):
    if len(result) == M:
        print(*result)
        return
    
    prev = 0
    
    for i in range(N):
        if arr[i] != prev:
            result.append(arr[i])
            prev = arr[i]
            
            dfs(i + 1)
            
            result.pop()

dfs(0)
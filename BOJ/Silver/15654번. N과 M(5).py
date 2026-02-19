N, M = list(map(int,input().split()))
arr = list(map(int, input().split()))
arr.sort()

result = []
def dfs(start):
    if len(result) == M:
        for i in result:
            print(arr[i-1], end = ' ')
        print()
        return
    
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            dfs(start+1)
            result.pop()
dfs(1)
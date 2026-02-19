N, M = list(map(int,input().split()))
result = []
def dfs(start):
    if len(result) == M:
        print(' '.join(map(str,result)))
        return
    
    for i in range(start,N+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()
dfs(1)
 
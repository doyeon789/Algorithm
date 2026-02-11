"""

4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
"""
def dfs(cnt, honey, value, ci, cj):
    global max_honey

    if honey > C:
        return
    
    if cnt == M:
        max_honey = max(max_honey, value)
        return
    
    dfs(cnt+1, honey+honey_grid[ci][cj+cnt], value+honey_grid[ci][cj+cnt]**2,ci,cj)

    dfs(cnt+1, honey, value, ci, cj)

T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int, input().split())
    honey_grid = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    honey_h1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-(M-1)):
            max_honey = 0
            dfs(0,0,0,i,j)
            honey_h1[i][j] = max_honey

    
    for i1 in range(N):
        for j1 in range(N-(M-1)):
            for i2 in range(i1, N):
                sj = j1+M if i2 == i1 else 0 
                for j2 in range(sj, N-(M-1)):
                    ans = max(ans, honey_h1[i1][j1] + honey_h1[i2][j2])

    print(f"#{tc} {ans}")
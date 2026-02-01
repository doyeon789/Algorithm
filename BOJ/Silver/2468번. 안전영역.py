dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(i,j,map):
    map[i][j] = True

    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if not map[nx][ny]:
                dfs(nx,ny,map) 

n = int(input())
h_map = [list(map(int,input().split())) for _ in range(n)]

value = set()
value.add(0)
for row in h_map:
    value.update(row)


result = 0
for h in value:
    ans = 0
    map = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if h_map[i][j] <= h:
                map[i][j] = True
    
    for i in range(n):
        for j in range(n):
            if map[i][j] == 0:
                ans += 1
                dfs(i,j,map)

    result = max(result, ans)

print(result)

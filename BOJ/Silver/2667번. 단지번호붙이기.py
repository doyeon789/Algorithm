n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

apartment = []
count = 0

def dfs(i,j):
    global count 
    count += 1
    
    visited[i][j] = True
    
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and map[nx][ny] == 1:
                dfs(nx,ny)        
    
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and map[i][j] == 1:
            count = 0
            dfs(i,j)
            apartment.append(count)

print(len(apartment))
apartment.sort()
for i in range(len(apartment)):
    print(apartment[i])

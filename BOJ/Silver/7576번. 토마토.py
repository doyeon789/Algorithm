from collections import deque

def bfs(locations):
    q = deque()
    for x, y in locations_of_1:
        q.append((x, y))
    
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if tomato_box[ny][nx] == 0:
                    tomato_box[ny][nx] = tomato_box[y][x] + 1
                    q.append((nx,ny))
    return 

m,n = map(int, input().split())
tomato_box = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

locations_of_1 = []

for i in range(m):
    for j in range(n):
        if tomato_box[j][i] == 1:
            locations_of_1.append((i,j))

bfs(locations_of_1)

is_0_left = False
days = []

for i in range(m):
    for j in range(n):
        if tomato_box[j][i] == 0:
            is_0_left = True
        days.append(tomato_box[j][i])

if is_0_left == True:
    print("-1")
else:
    print(max(days)-1)
"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""

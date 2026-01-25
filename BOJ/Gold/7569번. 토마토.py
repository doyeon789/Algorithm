from collections import deque

m, n, h = map(int, input().split())

dz = [0,0,0,0,-1,1]
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]

tomato = []
for _ in range(h):
    layer = []
    for _ in range(n):
        layer.append(list(map(int, input().split())))
    tomato.append(layer)
locations_of_1 = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                locations_of_1.append((i,j,k))

def bfs(locations_of_1):
    q = deque(locations_of_1)

    while q:
        z, x, y = q.popleft()
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nz < h and 0 <= nx < m and 0 <= ny < n:
                if tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = tomato[z][x][y] + 1
                    q.append((nz, ny, nx))

    return
bfs(locations_of_1)

print(tomato)

is_0_left = False
days = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                is_0_left = True
            days.append(tomato[i][j][k])
            
if is_0_left == True:
    print("-1")
else:
    print(max(days)-1)

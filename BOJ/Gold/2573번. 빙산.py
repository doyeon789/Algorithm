import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def melt(x,y):
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        if sea[nx][ny]==0:
            around_sea[x][y]+=1


def bfs(i,j):
    q = deque()
    global temp
    q.append((i,j))
    temp += 1
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if sea[nx][ny]!=0 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = temp
around_sea = [[0 for _ in range(M)] for _ in range(N)]
year = 0
while True:
    temp = 0
    count = 0
    year += 1
    visited = [[0 for _ in range(M)] for i in range(N)]
    
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                count += 1 
                melt(i,j)
    if count == 0:
        print(0)
        break
    for i in range(N):
        for j in range(M):
            if sea[i][j] > around_sea[i][j]:
                sea[i][j]-=around_sea[i][j]
                around_sea[i][j] = 0 
            else:
                sea[i][j] = 0
                around_sea[i][j] = 0


    for i in range(N):
        for j in range(M):
            if sea[i][j]>0 and visited[i][j]==0: 
                bfs(i,j)
    if temp>=2:
        print(year)
        break

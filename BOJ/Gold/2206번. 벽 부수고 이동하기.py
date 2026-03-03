from collections import deque

def bfs():
    queue = deque()
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

    visited[0][0][True] = 1
    
    queue.append([0,0,True])
    while queue:
        i,j,chance = queue.popleft()
        if i == (N-1) and j == (M-1):
            return visited[i][j][chance]
                                
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < N and 0 <= ny < M:    
                if chance and maze[nx][ny]:
                    visited[nx][ny][False] = visited[i][j][True]+1
                    queue.append([nx,ny,False])

                elif not maze[nx][ny] and not visited[nx][ny][chance]:
                    visited[nx][ny][chance]=visited[i][j][chance]+1
                    queue.append([nx,ny,chance])
    return -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

print(bfs())
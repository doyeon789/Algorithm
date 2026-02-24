from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs(i, j):
    global result
    q = deque()
    q.append((i, j))
    
    visited = [[-1]*N for _ in range(N)]
    visited[i][j] = 1
    
    house_cnt = 0

    if arr[i][j] == 1:
        house_cnt = 1

    cost = 1*1 + 0*0
    if house_cnt * M >= cost:
        result = max(result, house_cnt)
    
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            ni = x + dx[d]
            nj = y + dy[d]
            
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1:
                    
                    visited[ni][nj] = visited[x][y] + 1
                    k = visited[ni][nj]
                    
                    if arr[ni][nj] == 1:
                        house_cnt += 1
                    
                    cost = k*k + (k-1)*(k-1)
                    if house_cnt * M >= cost:
                        result = max(result, house_cnt)
                    
                    q.append((ni, nj))
                        
    

T = int(input())
for tc in range(1,T+1):
    result = 0
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] 

    for i in range(N):
        for j in range(N):
            bfs(i, j)


    print(f"#{tc} {result}")    
    

"""
1
8 3
0 0 0 0 0 1 0 0
0 1 0 1 0 0 0 1
0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0
0 0 1 1 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0
1 0 0 0 0 0 0 0
"""
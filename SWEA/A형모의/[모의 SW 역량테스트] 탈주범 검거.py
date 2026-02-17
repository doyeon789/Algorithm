from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
reverse = [1, 0, 3, 2]

tunnel = [[],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 0]
]

def simulation(r, c):
    visited = [[False]*M for _ in range(N)]
    
    q = deque()
    q.append((r, c, 1))
    visited[r][c] = True
    
    count = 1
    
    while q:
        i, j, time = q.popleft()
        
        if time >= L:
            continue
        
        for d in range(4):

            if tunnel[matrix[i][j]][d] == 0:
                continue
            
            ni = i + dx[d]
            nj = j + dy[d]
            
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if matrix[ni][nj] == 0:
                    continue
                
                if tunnel[matrix[ni][nj]][reverse[d]] == 1:
                    visited[ni][nj] = True
                    q.append((ni, nj, time + 1))
                    count += 1
    return count


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    if matrix[R][C] == 0:
        result = 0
    else:
        result = simulation(R, C)
    
    print(f"#{tc} {result}")

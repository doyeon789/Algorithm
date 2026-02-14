# dfs로 구슬을 두는 위치
# bfs로 부수기

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def break_bricks(i,j,matrix):
    q = deque()
    q.append((i,j,matrix[i][j]))
    matrix[i][j] = 0
    
    while q:
        i,j,power = q.popleft()
        
        for d in range(4):
            for k in range(1, power):
                ni = i + dx[d] * k
                nj = j + dy[d] * k
                
                if 0 <= ni < H and 0 <= nj < W:
                    if matrix[ni][nj] > 0:
                        q.append((ni, nj, matrix[ni][nj]))
                        matrix[ni][nj] = 0


def gravity(matrix):
    for i in range(W):
        stack = []
        
        for j in range(H-1, -1, -1):
            if matrix[j][i] > 0:
                stack.append(matrix[j][i])
        
        j = H - 1
        for val in stack:
            matrix[j][i] = val
            j -= 1
        
        for r in range(j, -1, -1):
            matrix[r][i] = 0


def dfs(depth, matrix):
    global result
    
    if depth == N:
        remain = 0
        for i in range(H):
            for j in range(W):
                if matrix[i][j] > 0:
                    remain += 1
        result = min(result, remain)
        return
    
    for i in range(W):
        new_matrix = [m[:] for m in matrix]
        
        for j in range(H):
            if matrix[j][i] > 0:
                break_bricks(j, i, new_matrix)
                gravity(new_matrix)
                dfs(depth+1, new_matrix)
                break
        else:
            dfs(depth+1, new_matrix)


T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]    
    
    result = float('inf')
    dfs(0, matrix)
    
    print(f"#{tc} {result}")

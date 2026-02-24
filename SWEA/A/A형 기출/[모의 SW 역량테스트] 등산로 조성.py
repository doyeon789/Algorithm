def dfs(i, j, cnt, used_cut):
    global result
    
    result = max(result, cnt)

    for d in range(4):
        ni = i + dx[d]
        nj = j + dy[d]
        
        if 0 <= ni < N and 0 <= nj < N:
            if matrix[ni][nj] < matrix[i][j]:
                visited[ni][nj] = True
                dfs(ni, nj, cnt+1, used_cut)
                visited[ni][nj] = False
                
            elif used_cut == False and matrix[ni][nj]-K < matrix[i][j]:
                original_height = matrix[ni][nj]
                matrix[ni][nj] = matrix[i][j] - 1

                visited[ni][nj] = True
                dfs(ni, nj, cnt+1, True)
                visited[ni][nj] = False
                
                matrix[ni][nj] = original_height
                   
                
dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_num = max(map(max, matrix))
    visited = [[False] * N for _ in range(N)]
    
    result = 1
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == max_num:
                visited[i][j] = True
                dfs(i, j, 1, False)
                visited[i][j] = False
    
    print(f"#{tc} {result}")

"""
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
"""



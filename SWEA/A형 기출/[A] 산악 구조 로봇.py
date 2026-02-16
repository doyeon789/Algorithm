import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    dist[0][0] = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for _ in range(N * N):
        
        # 방문 안 한 곳 중 최소 dist 찾기
        min_cost = INF
        min_x = -1
        min_y = -1
        
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and dist[i][j] < min_cost:
                    min_cost = dist[i][j]
                    min_x = i
                    min_y = j
        
        # 더 이상 갈 수 있는 곳 없음
        if min_x == -1:
            break
        
        visited[min_x][min_y] = True
        
        # 상하좌우 갱신
        for d in range(4):
            nx = min_x + dx[d]
            ny = min_y + dy[d]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                
                now_h = board[min_x][min_y]
                next_h = board[nx][ny]
                
                if next_h == now_h:
                    cost = 1
                elif next_h < now_h:
                    cost = 0
                else:
                    cost = (next_h - now_h) * 2
                
                if dist[min_x][min_y] + cost < dist[nx][ny]:
                    dist[nx][ny] = dist[min_x][min_y] + cost
    
    print(f"#{tc} {dist[N-1][N-1]}")

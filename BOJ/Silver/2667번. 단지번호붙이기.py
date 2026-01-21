from collections import deque

def bfs(x,y):
    visited[i][j] = True
    q = deque()
    q.append((x,y))
    cnt = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if village[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt
n = int(input())
village = [list(map(int, input().strip())) for _ in range(n)]

cnt_lot_number = []


# > v < ^
dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if village[i][j] == 1 and not visited[i][j]:
            cnt_lot_number.append(bfs(i,j))
cnt_lot_number.sort()

print(len(cnt_lot_number))
for house_number in cnt_lot_number:
    print(house_number)

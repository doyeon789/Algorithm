from collections import deque

def bfs(r, y):
    visited = [[0]*N for _ in range(N)]
    q = deque([[r,y]])
    cand = []

    visited[r][y] = 1

    while q:
        i, j = q.popleft()

        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    if fish_tank[r][y] > fish_tank[ni][nj] and fish_tank[ni][nj] != 0:
                        visited[ni][nj] =  visited[i][j] + 1
                        cand.append((visited[ni][nj] - 1, ni, nj))

                    elif fish_tank[r][y] == fish_tank[ni][nj]:
                        visited[ni][nj] =  visited[i][j] + 1
                        q.append([ni,nj])

                    elif fish_tank[ni][nj] == 0:
                        visited[ni][nj] =  visited[i][j] + 1
                        q.append([ni,nj])
    
    return sorted(cand)


N = int(input())
fish_tank = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

shark_l = ()
for i in range(N):
    for j in range(N):
        if fish_tank[i][j] == 9:
            shark_l = (i,j)
cnt = 0

(i, j) = shark_l
shark_size = [2, 0]
while True:
    fish_tank[i][j] = shark_size[0]
    cand = deque(bfs(i,j))
    
    if not cand:
        break
        
    step, fish_i, fish_j = cand.popleft()
    cnt += step
    shark_size[1] += 1
    
    if shark_size[0] == shark_size[1]:
        shark_size[0] += 1
        shark_size[1] = 0

    fish_tank[i][j] = 0
    i = fish_i
    j = fish_j


print(cnt)
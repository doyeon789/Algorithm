from collections import deque

N = int(input())
K  = int(input())

matrix = [[0]*N for _ in range(N)]
for k in range(K):
    i, j = map(int,input().split())
    matrix[i-1][j-1] = 2

snake_move = {}
L = int(input())
for l in range(L):
    X, C = input().split()
    snake_move[int(X)] = C
    
time = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

matrix[0][0] = 1
d = 0
i, j = 0, 0
snake = deque()
snake.append((0,0))

while True:
    time += 1

    ni = i + dx[d]
    nj = j + dy[d]

    # 1. 벽 체크
    if ni < 0 or nj < 0 or ni >= N or nj >= N:
        break

    # 2. 사과 여부 먼저 판단
    if matrix[ni][nj] == 2:
        matrix[ni][nj] = 0
    else:
        a, b = snake.popleft()
        matrix[a][b] = 0

    # 3. 이제 몸통 충돌 체크
    if matrix[ni][nj] == 1:
        break

    # 4. 머리 이동
    matrix[ni][nj] = 1
    snake.append((ni, nj))
    i, j = ni, nj

    # 5. 방향 전환
    if time in snake_move:
        if snake_move[time] == "D":
            d = (d+1) % 4
        else:
            d = (d-1) % 4

print(time)

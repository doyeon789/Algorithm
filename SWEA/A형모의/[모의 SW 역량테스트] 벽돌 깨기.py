from collections import deque

num, width, height = map(int, input().split())
or_grid = [list(map(int, input().split())) for _ in range(height)]

result = float('inf')

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 벽돌 부쉬기
def break_bricks(x,y,grid):
    q = deque()
    q.append((x, y, grid[x][y]))
    #해당 위치 0
    grid[x][y] = 0

    while q:
        x, y, power = q.popleft()

        for d in range(4):
            # + 모양으로 탐색
            for k in range(1, power):
                nx = x + dx[d] * k
                ny = y + dy[d] * k

                if 0 <= nx < height and 0 <= ny < width:
                    # 탐색 도중 벽돌이 1이상이면 연쇄적으로 부쉬기 
                    if grid[nx][ny] > 0:
                        q.append((nx, ny, grid[nx][ny]))
                        grid[nx][ny] = 0

# 벽돌을 모두 부순 후 중력작용으로 아래로 내리기
def gravity(board):

    # 열(column) 단위로 중력을 적용
    # -> 중력은 좌우가 아니라 '아래 방향'만 있기 때문
    for col in range(width):
        stack = []   # 현재 열에서 살아남은 벽돌들을 담을 공간

        # 아래에서 위로 탐색
        #  아래쪽 벽돌부터 차곡차곡 모으기 위함
        for row in range(height - 1, -1, -1):
            if board[row][col] > 0:   # 벽돌이 있으면
                stack.append(board[row][col])  # 순서 유지한 채 저장

        # 이제 이 열을 아래부터 다시 채운다
        row = height - 1
        for val in stack:
            board[row][col] = val   # 벽돌을 맨 아래부터 차례대로 배치
            row -= 1

        # 남은 윗부분은 전부 빈 공간(0)으로 초기화
        for r in range(row, -1, -1):
            board[r][col] = 0
            
def dfs(depth, grid):
    global result

    # 3 번 구슬 던지면
    if depth == num:
        # 남은 벽돌수 세기
        remain = 0
        for i in range(width):
            for j in range(height):
                if grid[j][i] >= 1:
                    remain += 1
        result = min(result, remain)
        return

    #열 선택
    for col in range(width):
        #벽돌 존재 여부 확인
        for row in range(height):
            if grid[row][col] > 0:
                # 그리드 복사
                new_grid = [g[:] for g in grid]
                # 벽돌 깨기
                break_bricks(row, col, new_grid)
                # 중력
                gravity(new_grid)

                dfs(depth+1, new_grid)
                break
        else:
            new_grid = [g[:] for g in grid]
            dfs(depth + 1, new_grid)
            
dfs(0,or_grid)

print(result)

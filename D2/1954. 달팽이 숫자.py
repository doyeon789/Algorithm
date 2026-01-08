T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    x, y = 0, 0
    d = 0 
    num = 1

    for _ in range(n*n):
        arr[x][y] = num
        num += 1

        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    print(f"#{tc}")
    for row in arr:
        print(*row)

from collections import deque

testcase = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < width and 0 <= ny < height:
                if not visited[ny][nx] and plow[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))

for _ in range(testcase):
    width, height, napa_cabbage = map(int, input().split())

    plow = [[0] * width for _ in range(height)]
    visited = [[False] * width for _ in range(height)]

    for _ in range(napa_cabbage):
        x, y = map(int, input().split())
        plow[y][x] = 1

    worm = 0
    for y in range(height):
        for x in range(width):
            if plow[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                worm += 1

    print(worm)

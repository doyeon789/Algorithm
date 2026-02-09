di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(r, c):
    global is_possible

    visited = [[False]*16 for _ in range(16)]
    stack = []
    stack.append((r, c))
    visited[r][c] = True

    while stack:
        i, j = stack.pop()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if not (0 <= ni < 16 and 0 <= nj < 16):
                continue

            if visited[ni][nj]:
                continue

            if maze[ni][nj] == 1:
                continue

            if maze[ni][nj] == 3:
                is_possible = 1
                return

            if maze[ni][nj] == 0:
                visited[ni][nj] = True
                stack.append((ni, nj))


for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]
    is_possible = 0
    dfs(1,1)

    print(f"#{tc} {is_possible}")
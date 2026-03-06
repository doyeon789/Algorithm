import sys
from collections import deque
input = sys.stdin.readline

dy = [0,0,1,-1,1,-1,1,-1]
dx = [1,-1,0,0,1,1,-1,-1]

def bfs(i, j, dir_cnt, target):
    queue = deque([(i,j)])
    border = set()

    while queue:
        i, j = queue.popleft()

        if visited[i][j] == 0:
            visited[i][j] = 1
            for d in range(dir_cnt):
                ni = i + dy[d]
                nj = j + dx[d]
                if 0 <= ni < N and 0 <= nj < M:
                    if visited[ni][nj] == 0:
                        if board[ni][nj] == target:
                            queue.append((ni,nj))
                        else:
                            border.add((ni,nj))
    return border


def dfs(ocean):
    island = set()
    max_height = 0

    for i, j in ocean:
        if visited[i][j] == 0:
            border = bfs(i, j, 4, 0)
            for pos in border:
                island.add(pos)

    for i, j in island:
        if visited[i][j] == 0:
            inner_ocean = bfs(i, j, 8, 1)
            height = dfs(inner_ocean) + 1
            if height > max_height:
                max_height = height

    while len(result) <= max_height:
        result.append(0)
    result[max_height] += 1
    return max_height


N, M = map(int,input().split())

M += 2
board = [[0]*M]
for _ in range(N):
    row = [0]
    for c in input().strip():
        if c == 'x':
            row.append(1)
        else:
            row.append(0)

    row.append(0)
    board.append(row)

board.append([0]*M)

N += 2

visited = [[0]*M for _ in range(N)]
result = []

dfs([(0,0)])

if result:
    result.pop()

if result:
    print(*result)
else:
    print(-1)
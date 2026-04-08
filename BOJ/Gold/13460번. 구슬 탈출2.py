import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    row = list(input().strip())
    graph.append(row)
    for j in range(m):
        if row[j] == 'R':
            ri, rj = i, j
        elif row[j] == 'B':
            bi, bj = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, d):
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if graph[nx][ny] == '#':
            break
        x, y = nx, ny
        cnt += 1
        if graph[x][y] == 'O':
            break
    return x, y, cnt

def bfs(ri, rj, bi, bj):
    q = deque()
    q.append((ri, rj, bi, bj, 0))
    visited = set()
    visited.add((ri, rj, bi, bj))

    while q:
        ri, rj, bi, bj, count = q.popleft()

        if count >= 10:
            print(-1)
            return

        for d in range(4):
            nri, nrj, rc = move(ri, rj, d)
            nbi, nbj, bc = move(bi, bj, d)

            if graph[nbi][nbj] == 'O':
                continue

            if graph[nri][nrj] == 'O':
                print(count + 1)
                return

            # 위치 겹치면 조정
            if nri == nbi and nrj == nbj:
                if rc > bc:
                    nri -= dx[d]
                    nrj -= dy[d]
                else:
                    nbi -= dx[d]
                    nbj -= dy[d]

            if (nri, nrj, nbi, nbj) not in visited:
                visited.add((nri, nrj, nbi, nbj))
                q.append((nri, nrj, nbi, nbj, count + 1))

    print(-1)

bfs(ri, rj, bi, bj)
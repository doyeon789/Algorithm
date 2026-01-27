import sys
from collections import deque

delta = ((-1,0),(1,0),(0,1),(0,-1))

def bfs(r, c, flag):
    q = deque()
    q.append((r, c))
    grid[r][c] = flag

    while q:
        y, x = q.popleft()
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < row and 0 <= nx < col:
                if grid[ny][nx] == 1:
                    grid[ny][nx] = flag
                    q.append((ny, nx))

def findBridge(r, c, flag):
    for dy, dx in delta:
        y, x = r + dy, c + dx
        if not (0 <= y < row and 0 <= x < col):
            continue
        if grid[y][x] == 0:
            getDistance(y, x, dy, dx, flag)

def getDistance(y, x, dy, dx, flag):
    length = 1
    while True:
        y += dy
        x += dx
        if y < 0 or y >= row or x < 0 or x >= col:
            return
        if grid[y][x] == 0:
            length += 1
        elif grid[y][x] == flag:
            return
        else:
            if length >= 2:
                bridges.append((length, flag, grid[y][x]))
            return

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        return True
    return False


row, col = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

flag = 2
for r in range(row):
    for c in range(col):
        if grid[r][c] == 1:
            bfs(r, c, flag)
            flag += 1

island_cnt = flag - 2

bridges = []
for r in range(row):
    for c in range(col):
        if grid[r][c] >= 2:
            findBridge(r, c, grid[r][c])

bridge_set = {}
for l, a, b in bridges:
    if a == b:
        continue
    if a > b:
        a, b = b, a
    if (a, b) not in bridge_set or bridge_set[(a, b)] > l:
        bridge_set[(a, b)] = l

edges = []
for (a, b), l in bridge_set.items():
    edges.append((l, a, b))

edges.sort()

parent = list(range(flag))
total = 0
cnt = 0

for l, a, b in edges:
    if union(a, b):
        total += l
        cnt += 1
        if cnt == island_cnt - 1:
            break

if cnt == island_cnt - 1:
    print(total)
else:
    print(-1)

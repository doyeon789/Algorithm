import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))

def spread_virus(temp):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx, ny))

def count_safe_area(temp):
    return sum(row.count(0) for row in temp)

result = 0
for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(lab)
    for x, y in walls:
        temp_lab[x][y] = 1

    spread_virus(temp_lab)
    result = max(result, count_safe_area(temp_lab))

print(result)

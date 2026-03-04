# 신발끈 공식 (Shoelace Formula)

import sys
input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

area = 0

for i in range(N):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % N]
    area += x1 * y2 - x2 * y1

print(f"{abs(area) / 2:.2f}")  
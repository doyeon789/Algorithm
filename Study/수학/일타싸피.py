import math

# 입력으로 필요한 것들
"""
1. 내 공 좌표 -> (sx, sy)
2. 목적구 좌표 -> (tx, ty)
3. 홀 좌표 -> (hx, hy)
4. 공반지름 -> (r)
5. (있다면) 테이블 크기 -> (width, height)
"""

# 1. 목적구 → 홀 방향 단위벡터
dx = hx - tx
dy = hy - ty

# 2. 단위벡터 만들기
dist = math.hypot(dx, dy)

ux = dx / dist
uy = dy / dist

# 3. 접점 좌표 구하기
contact_x = tx - ux * 2*r
contact_y = ty - uy * 2*r

# 4. 내 공 → 접점 각도
theta = math.atan2(contact_y - sy, contact_x - sx)

print(math.degrees(theta))


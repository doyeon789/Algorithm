#삼각함수
import math

(x1,y1) = 0,0
(x2,y2) = 1, 1

print(math.sin(0)) #라디안
print(math.cos(0)) #라디안
print(math.tan(0)) #라이안

#도 -> 라디안
math.radians(90)#각도
angle = 30 
print(math.sin(math.radians(angle)))

#라디안 -> 도
math.degrees(math.pi)# 180

# atan2
# (x,y)의 각도 구할때 사용
# math.atan2(y,x)
print(math.degrees(math.atan2(y2,x2)))

#거리 구하기
dist = math.sqrt((x2-x1)+(y2-y1))

# 두 점 사이의 각도
dx = x2 - x1
dy = y2 - y1

angle = math.atan2(dy, dx)
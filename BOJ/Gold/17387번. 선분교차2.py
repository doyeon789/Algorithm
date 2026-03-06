x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
 
def ccw(a1, b1, a2, b2, a3, b3):
    s = (a1*b2 + a2*b3 + a3*b1) - (a2*b1 + a3*b2 + a1*b3)
    
    if s > 0: return 1
    elif s == 0: return 0
    else: return -1
 
flagA = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
flagB = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
 
if flagA == 0 and flagB == 0:
    if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
        print(1)
    else:
        print(0)
else:
    if flagA <= 0 and flagB <= 0:
        print(1)
    else:
        print(0)
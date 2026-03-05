import sys
input = sys.stdin.readline


def ccw(line, x3, y3):
    x1, y1, x2, y2 = line

    result = (x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2)

    if result == 0:
        return 0
    elif result > 0:
        return 1
    else:
        return -1


def meet(l1, l2):
    res1 = ccw(l1, l2[0], l2[1]) * ccw(l1, l2[2], l2[3])
    res2 = ccw(l2, l1[0], l1[1]) * ccw(l2, l1[2], l1[3])

    if res1 == 0 and res2 == 0:
        if min(l1[0], l1[2]) <= max(l2[0], l2[2]) and \
           min(l2[0], l2[2]) <= max(l1[0], l1[2]) and \
           min(l1[1], l1[3]) <= max(l2[1], l2[3]) and \
           min(l2[1], l2[3]) <= max(l1[1], l1[3]):
            return True
        else:
            return False

    elif res1 <= 0 and res2 <= 0:
        return True

    else:
        return False


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[a] = b


N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

parents = [i for i in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if meet(lines[i], lines[j]):
            union(i, j)

group = {}
max_size = 1

for i in range(N):
    root = find(i)

    if root in group:
        group[root] += 1
        max_size = max(max_size, group[root])
    else:
        group[root] = 1

print(len(group))
print(max_size)
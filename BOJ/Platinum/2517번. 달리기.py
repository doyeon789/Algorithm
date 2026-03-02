import sys
input = sys.stdin.readline

def update(i):
    while i <= n:
        tree[i] += 1
        i += (i & -i)

def query(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s

n = int(input())
arr = [int(input()) for _ in range(n)]

sorted_unique = sorted(set(arr))
compress = {value: i+1 for i, value in enumerate(sorted_unique)}

compressed_arr = [compress[x] for x in arr]

tree = [0] * (n + 1)

for skill in compressed_arr:
    total = query(n)
    not_bigger = query(skill)
    bigger = total - not_bigger
    
    print(bigger + 1)
    
    update(skill)
"""
8
2
8
10
7
1
9
4
15
"""
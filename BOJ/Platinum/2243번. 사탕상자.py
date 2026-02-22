import sys
input = sys.stdin.readline

def update(start, end, index, target, diff):
    if target < start or target > end:
        return
    
    tree[index] += diff
    
    if start == end:
        return
    
    mid = (start + end) // 2
    update(start, mid, index*2, target, diff)
    update(mid+1, end, index*2+1, target, diff)

def query(start, end, index, k):
    if start == end:
        return start
    
    mid = (start + end) // 2
    
    if tree[index*2] >= k:
        return query(start, mid, index*2, k)
    else:
        return query(mid+1, end, index*2+1, k - tree[index*2])

N = int(input())

SIZE = 1000000
tree = [0] * (SIZE * 4)

for _ in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        b = arr[1]
        flavor = query(1, SIZE, 1, b)
        print(flavor)
        update(1, SIZE, 1, flavor, -1)
        
    elif arr[0] == 2:
        b, c = arr[1], arr[2]
        update(1, SIZE, 1, b, c)

"""
6
2 1 2
2 3 3
1 2
1 2
2 1 -1
1 2
"""
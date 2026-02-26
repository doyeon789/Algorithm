import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]


def propagate(start, end, index):
    if lazy[index] != 0:
        tree[index] += (end - start + 1) * lazy[index]
        if start != end:
            lazy[index*2] += lazy[index]
            lazy[index*2+1] += lazy[index]
        lazy[index] = 0


def update_range(start, end, index, left, right, value):
    propagate(start, end, index)

    if left > end or right < start:
        return  
    
    if left <= start and end <= right:
        lazy[index] += value
        propagate(start, end, index)
        return
    
    mid = (start+end)//2
    update_range(start, mid, index*2, left, right, value)
    update_range(mid+1, end, index*2+1, left, right, value)

    tree[index] = tree[index*2]+tree[index*2+1]


def query(start, end, index, target):
    propagate(start, end, index)

    if start == end:
        return tree[index]

    mid = (start + end) // 2

    if target <= mid:
        return query(start, mid, index*2, target)
    else:
        return query(mid+1, end, index*2+1, target)

N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (N*4)
lazy = [0] * (N*4)

init(0, N - 1, 1)

M = int(input())
for _ in range(M):
    order = list(map(int, input().split()))
    if len(order) == 4:
        _, i, j, k = order
        update_range(0,N-1,1,i-1,j-1,k)

    elif len(order) == 2:
        _, x = order
        print(query(0, N-1, 1, x-1))

"""
5
1 2 3 4 5
4
1 3 4 6
2 3
1 1 3 -2
2 3
"""
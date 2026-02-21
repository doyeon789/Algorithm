import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
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
    
    mid = (start + end) // 2
    update_range(start, mid, index*2, left, right, value)
    update_range(mid+1, end, index*2+1, left, right, value)
    
    tree[index] = tree[index*2] + tree[index*2+1]


def interval_sum(start, end, index, left, right):
    
    propagate(start, end, index)

    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return interval_sum(start, mid, index*2, left, right) + \
           interval_sum(mid+1, end, index*2+1, left, right)


N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

tree = [0] * (N * 4)
lazy = [0] * (N * 4)

init(0, N-1, 1)

for _ in range(M + K):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        b, c, d = query[1]-1, query[2]-1, query[3]
        update_range(0, N-1, 1, b, c, d)
    
    elif query[0] == 2:
        b, c = query[1]-1, query[2]-1
        print(interval_sum(0, N-1, 1, b, c))
def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return interval_sum(start, mid, index*2, left, right) + \
           interval_sum(mid+1, end, index*2+1, left, right)

def update(start, end, index, target, diff):
    if target < start or target > end:
        return
    
    tree[index] += diff
    
    if start != end:
        mid = (start + end) // 2
        update(start, mid, index*2, target, diff)
        update(mid+1, end, index*2+1, target, diff)


N, M, K = map(int, input().split())

arr = []
tree = [0] * (N * 4)

for _ in range(N):
    arr.append(int(input()))

init(0, N-1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    if a == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(0, N-1, 1, b, diff)
        
    elif a == 2:
        print(interval_sum(0, N-1, 1, b-1, c-1))
import sys
input = sys.stdin.readline

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    return interval_sum(start, mid, index*2, left, right) + interval_sum(mid+1, end, index*2+1, left, right)

def update(start, end, index, target, diff):
    if target < start or target > end:
        return
    
    tree[index] += diff
    
    if start != end:
        mid = (start + end) // 2
        update(start, mid, index*2, target, diff)
        update(mid+1, end, index*2+1, target, diff)

N, M = map(int, input().split())
arr = [0]*N
tree = [0] * (N * 4)

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        if b > c:
            print(interval_sum(0,N-1,1,c-1,b-1))
        else:
            print(interval_sum(0,N-1,1,b-1,c-1))
    if a == 1:
        b -= 1 
        diff = c - arr[b]
        arr[b] = c
        update(0,N-1,1,b,diff)
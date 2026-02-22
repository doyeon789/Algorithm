import sys
input = sys.stdin.readline

MOD = 1000000007

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start+end)//2
    tree[index] = (init(start,mid,index*2) *
                   init(mid+1, end, index*2+1)) % MOD
    return tree[index]


def interval_mul(start, end, index, left, right):
    if left > end or right < start:
        return 1
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start+end)//2
    return (interval_mul(start, mid, index*2, left, right) *
            interval_mul(mid+1, end, index*2+1, left, right)) % MOD


def update(start, end, index, target, value):
    if target < start or target > end:
        return
    
    if start == end:
        tree[index] = value
        return
    
    mid = (start + end) // 2
    update(start, mid, index*2, target, value)
    update(mid+1, end, index*2+1, target, value)

    tree[index] = (tree[index*2] * tree[index*2+1]) % MOD
    
    
N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
tree = [0] * (N*4)

init(0,N-1,1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    
    if a == 1:
        b -= 1
        arr[b] = c
        update(0, N-1, 1, b, c)
    
    elif a == 2:
        print(interval_mul(0, N-1, 1, b-1, c-1))
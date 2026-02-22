import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = start
        return
    
    mid = (start + end) // 2
    init(start, mid, index*2)
    init(mid+1, end, index*2+1)
    
    left = tree[index*2]
    right = tree[index*2+1]
    
    if arr[left] <= arr[right]:
        tree[index] = left
    else:
        tree[index] = right


def update(start, end, index, target):
    if target < start or target > end:
        return
    
    if start == end:
        return
    
    mid = (start + end) // 2
    update(start, mid, index*2, target)
    update(mid+1, end, index*2+1, target)
    
    left = tree[index*2]
    right = tree[index*2+1]
    
    if arr[left] <= arr[right]:
        tree[index] = left
    else:
        tree[index] = right


N = int(input())
arr = list(map(int, input().split()))

tree = [0] * (1 << ((N - 1).bit_length() + 1))

init(0, N-1, 1)

M = int(input())
for _ in range(M):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        i, v = query[1]-1, query[2]
        arr[i] = v
        update(0, N-1, 1, i)
        
    else:
        print(tree[1] + 1)   # 1-indexed 출력
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


def query(start, end, index, left, right):
    if right < start or left > end:
        return -1
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start + end) // 2
    
    l = query(start, mid, index*2, left, right)
    r = query(mid+1, end, index*2+1, left, right)
    
    if l == -1:
        return r
    if r == -1:
        return l
    
    if arr[l] <= arr[r]:
        return l
    else:
        return r


# 입력
N = int(input())
arr = list(map(int, input().split()))

tree = [0] * (4*N)

init(0, N-1, 1)

M = int(input())
for _ in range(M):
    query_input = list(map(int, input().split()))
    
    if query_input[0] == 1:
        i, v = query_input[1]-1, query_input[2]
        arr[i] = v
        update(0, N-1, 1, i)
        
    else:
        i, j = query_input[1]-1, query_input[2]-1
        result = query(0, N-1, 1, i, j)
        print(result + 1)
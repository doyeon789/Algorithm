import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end :
        tree[index] = arr[start]
        return
    
    mid = (start+end)//2
    init(start, mid, index*2)
    init(mid+1, end, index*2+1)

    tree[index] = min(tree[index*2],tree[index*2+1])
    return

def update(start, end, index, target, diff):
    if target < start or target > end:
        return
    
    if start == end:
        tree[index] = diff
        return
    
    mid = (start+end)//2
    update(start, mid, index*2, target, diff)
    update(mid+1, end, index*2+1, target, diff)
    tree[index] = min(tree[index*2],tree[index*2+1])

def query(start, end, index, left, right):
    if left > end or right < start:
        return float('inf')
    
    if left <= start and end <= right:
        return tree[index]
    
    mid = (start+end)//2
    return min(query(start, mid, index*2, left, right),query(mid+1, end, index*2+1, left, right))

N = int(input()) 
arr = list(map(int, input().split()))
tree = [0]*(N*4)

init(0,N-1,1)

M = int(input())
for i in range(M):
    a,b,c = map(int, input().split())
    if a == 1:
        update(0,N-1,1,b-1,c)
    if a == 2:
        print(query(0,N-1,1,b-1,c-1))

"""
5
5 4 3 2 1
6
2 1 3
2 1 4
1 5 3
2 3 5
1 4 3
2 3 5
"""
def init(start, end, index):
    if start == end:
        min_tree[index] = arr[start]
        max_tree[index] = arr[start]
        return
    
    mid = (start+end)//2
    init(start, mid, index*2)
    init(mid+1, end, index*2+1)
    
    min_tree[index] = min(min_tree[index*2], min_tree[index*2+1])
    max_tree[index] = max(max_tree[index*2], max_tree[index*2+1])
    return

"""
완전히 벗어나면 → (아주 작은 최대값, 아주 큰 최소값) 반환
완전히 포함되면 → 그 노드 그대로 반환
일부 겹치면 → 왼쪽/오른쪽 재귀 후 합치기
"""

def query(start, end, index, left, right):
    if left > end or right < start:
        return (float('inf'), 0)
    
    if left <= start and end <= right:
        return (min_tree[index], max_tree[index])
    
    mid = (start + end) // 2
    
    left_min, left_max = query(start, mid, index*2, left, right)
    right_min, right_max = query(mid+1, end, index*2+1, left, right)
    
    return (min(left_min, right_min), max(left_max, right_max))

N ,M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

INF = float('inf')
min_tree = [INF] * (N*4)
max_tree = [0] * (N*4)

init(0,N-1,1)

for i in range(M):
    a, b = map(int, input().split())
    min_value, max_value = query(0, N-1, 1, a-1, b-1)
    print(min_value, max_value)

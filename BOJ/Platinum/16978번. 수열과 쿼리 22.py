import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + \
           interval_sum(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, target, diff):
    if target < start or target > end:
        return
    tree[index] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, target, diff)
    update(mid + 1, end, index * 2 + 1, target, diff)


N = int(input())
arr = list(map(int, input().split()))
tree = [0] * (4 * N)

init(0, N - 1, 1)

M = int(input())

updates = []
sum_queries = []

for idx in range(M):
    query = list(map(int, input().split()))
    if query[0] == 1:
        updates.append((query[1] - 1, query[2]))
    else:
        sum_queries.append((query[1], query[2] - 1, query[3] - 1, len(sum_queries)))

# k 기준 정렬
sum_queries.sort()

answers = [0] * len(sum_queries)
update_count = 0

for k, left, right, original_idx in sum_queries:
    
    # k번째 update까지 적용
    while update_count < k:
        idx, value = updates[update_count]
        diff = value - arr[idx]
        arr[idx] = value
        update(0, N - 1, 1, idx, diff)
        update_count += 1
    
    # 구간합 계산
    answers[original_idx] = interval_sum(0, N - 1, 1, left, right)

# 출력
for ans in answers:
    print(ans)
import sys
input = sys.stdin.readline

# <세그먼트 트리를 배열의 각 구간 합으로 채워주기>
# start:  배열의 시작 인덱스, end : 배열의 마지막 인덱스
# index: 세그먼트 트리의 인덱스 (무조건 1부터 시작)
def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = (
        init(start, mid, index*2) +
        init(mid+1, end, index*2+1)
    )
    return tree[index]


# <lazy 전파 함수>
# start : 배열의 시작 인덱스, end: 배열의 마지막 인덱스
# index: 세그먼트 트리의 인덱스(무조건 1부터 시작)
def propagate(start, end, index):
    # 1. lazy[index]가 0이 아니라면
    if lazy[index] != 0:
        
        # 2.현재 구간(tree[index])에 lazy 반영
        tree[index] += (end - start + 1) * lazy[index]
        
        # 3. 리프가 아니라면 자식에게 lazy 넘김
        if start != end:
            lazy[index*2] += lazy[index]
            lazy[index*2+1] += lazy[index]
        
        # 현재 lazy[index] 초기화
        lazy[index] = 0


# <구간 업데이트하는 함수>
# start : 시작 인덱스, end: 마지막 인덱스
# left, right : 업데이트하고자 하는 범위
# value : 업데이트할 값
def update_range(start, end, index, left, right, value):
    
    # 1. 먼저 propagate 호출
    #    현재 노드에 밀린 lazy 먼저 처리
    propagate(start, end, index)
    
    # 2. 범위 밖이면 종료(return)
    if left > end or right < start:
        return 0
    
    # 3. 완전히 포함되면:
    #    lazy에 value 더하고 propagate 호출 후 return
    #    완전히 포함되면 lazy만 기록하고 종료
    if left <= start and end <= right:
        lazy[index] += value
        propagate(start, end, index)
        return
    
    # 4. 일부만 겹치면:
    #    왼쪽, 오른쪽 재귀 호출
    #    일부만 겹치면 자식으로 내려감
    mid = (start + end) // 2
    update_range(start, mid, index*2, left, right, value)
    update_range(mid+1, end, index*2+1, left, right, value)

    # 5. tree[index] 갱신
    #    자식 업데이트 후 현재 노드 값 갱신
    tree[index] = tree[index*2] + tree[index*2+1]


# <구간 합 조회하는 함수>
# start : 시작 인덱스, end: 마지막 인덱스
# left, right : 조회하고자 하는 범위
def query(start, end, index, left, right):
    
    # 1. propagate 호출
    #    현재 노드에 밀린 lazy 먼저 처리
    propagate(start, end, index)
    
    # 2. 범위 밖이면 0
    if left > end or right < start:
        return 0
    
    # 3. 완전히 포함되면 tree[index] 반환
    if left <= start and end <= right:
        return tree[index]
    
    # 4. 일부만 겹치면
    #    왼쪽, 오른쪽 재귀 호출
    #    일부만 겹치면 자식으로 내려감
    mid = (start + end) // 2

    left_sum = query(start, mid, index*2, left, right)
    right_sum = query(mid+1, end, index*2+1, left, right)
    return left_sum + right_sum

N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]

tree = [0] * (N * 4)
lazy = [0] * (N * 4)

init(0, N-1, 1)

for _ in range(M + K):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        # 구간에 값 더하기
        b, c, d = cmd[1]-1, cmd[2]-1, cmd[3]
        update_range(0, N-1, 1, b, c, d)
    
    elif cmd[0] == 2:
        # 구간 합 구하기
        b, c = cmd[1]-1, cmd[2]-1
        print(query(0, N-1, 1, b, c))


    """
5 2 2
1
2
3
4        
5
1 3 4 6
2 2 5
1 1 3 -2
2 2 5
    """
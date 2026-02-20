# N에서 가장 가까운 제곱수를 구한뒤 그것의 2배를 하여 미리 세그먼트 트리를 만들어 놓아야 한다.

arr = [1,2,3,4,5,6,7,8,9,10]
tree = [0]* (len(arr) * 4)

# <세그먼트 트리를 배열의 각 구간 합으로 채워주기>
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스 
# index : 세그먼트 트리의 인덱스 (무조건 1부터 시작 )
def init(start,end, index):
    #가장 끝까지 도달했으면 arr 삽입
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start+end)//2
    
    # 좌측 노드와 우측노드를 채워주면서 부모 모드값도 채워준다.
    tree[index] = init(start, mid, index*2) + init(mid + 1, end, index*2+1)
    return tree[index]


# <구간 합을 구하는 함수>
# start : 시작 인덱스, end : 마지막 인덱스
# left, right : 구간합을 구하고자 하는 범위 
def interval_sum(start,end,index,left,right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return tree[index]
    
    #그렇지 않으면 두 부분으로 나누어 합하기
    mid = (start+end)//2
    return interval_sum(start, mid, index*2, left,right) + interval_sum(mid+1, end, index*2+1, left, right)


# <특정 원소의 값을 구정하는 함수>
# start: 시작 인덱스, end : 마지막 인덱스
# what: 구간 합을 수정하고자 하는 코드
# value : 수정할 값
def update(start, end, index, what, value):
    # 범위 밖에 있는 경우
    if what < start or what > end:
        return
    
    # 범위 안에 있으면 내려가서 다른 원소도 갱신
    tree[index] += value
    if start == end:
        return
    
    mid = (start+end)//2
    update(start, mid, index*2, what, value)
    update(mid+1, end, index*2+1, what, value)    

init(0,len(arr)-1, 1)
print(interval_sum(0, len(arr)-1, 1, 0, 9))
print(interval_sum(0, len(arr)-1, 1, 0, 2))
print(interval_sum(0, len(arr)-1, 1, 6, 7))

# arr[0]를 +4만큼 수정
update(0, len(arr)-1, 1, 0, 4)
print(interval_sum(0, len(arr)-1, 1, 0, 2))


# arr[9]를 +4만큼 수정
update(0, len(arr)-1, 1, 9, 11)
print(interval_sum(0, len(arr)-1, 1, 8, 2))




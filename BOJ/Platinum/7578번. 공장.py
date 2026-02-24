import sys
input = sys.stdin.readline

# init과 동시에 교차저머 개수 구하기
def locate(start, end, index, loc_b):
    tree[index] += 1
    
    if start == end:
        return 0
    
    mid = (start+end)//2
    
    # index보다 오른쪽에 있는 구간합을 구하기
    if loc_b <= mid:
        return locate(start, mid, index*2, loc_b) + tree[index*2+1]
    else:
        return locate(mid+1, end, index*2+1, loc_b)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tree = [0]*(4*N)
loc = {} # A배열에 배치된 기계 인덱스
count = 0

for i, a in enumerate(A):
    loc[a] = i

for b in B:
    count += locate(0, N-1, 1, loc[b])

print(count)
"""
5
132 392 311 351 231
392 351 132 311 231
"""
# B를 돌면서 A에서 나보다 뒤에 있는데 
# 이미 먼저 나온 애들의 개수르 더하기
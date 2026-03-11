import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    l, r = 0, len(arr)
    while l < r:
        mid = (l+r)//2
        if arr[mid] >= target:
            r = mid
        else:
            l = mid+1
    return l

N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]

lines.sort()  # A 기준 정렬

B = [b for a,b in lines]

lis = []
idx = [0]*N

for i in range(N):
    pos = lower_bound(lis, B[i])
    
    if pos == len(lis):
        lis.append(B[i])
    else:
        lis[pos] = B[i]
        
    idx[i] = pos

length = len(lis)-1
keep = set()

for i in range(N-1,-1,-1):
    if idx[i] == length:
        keep.add(lines[i][0])
        length -= 1

print(N-len(keep))
for a,b in lines:
    if a not in keep:
        print(a)
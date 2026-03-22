import sys
import heapq
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
gem_lst = []
back_lst = []
hq = []
result = 0
for _ in range(N):
    M, V = map(int, input().split())
    gem_lst.append((M, V))

back_lst = [int(input()) for _ in range(K)]
gem_lst.sort(key=lambda x: x[0])
back_lst.sort()

gem_lst = deque(gem_lst)

for back in back_lst:
    while gem_lst:
        m, v = gem_lst[0]
        if m <= back:
            heapq.heappush(hq, -v)
            gem_lst.popleft() 
        else:
            break 

    if hq:
        result += -heapq.heappop(hq)

print(result)
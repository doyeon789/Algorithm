import sys
import heapq
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
lrc = [list(map(int, input().split())) for _ in range(M)]

start = tuple(A)
target = tuple(sorted(A))

pq = [(0, start)]
dist = {start:0}

answer = -1

while pq:
    cost, cur = heapq.heappop(pq)
    
    if dist[cur] < cost:
        continue

    if cur == target:
        answer = cost
        break

    for l, r,c in lrc:
        next = list(cur)
        next[l-1], next[r-1] = next[r-1], next[l-1]
        next = tuple(next)

        new_cost = cost + c

        if next not in dist or dist[next] > new_cost:
            dist[next] = new_cost
            heapq.heappush(pq, (new_cost, next))

print(answer)
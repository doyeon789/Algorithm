import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    
    min_h = []
    max_h = []
    count = {}

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_h, num)
            heapq.heappush(max_h, -num)
            count[num] = count.get(num, 0) + 1
        else:
            if not count:
                continue

            if num == 1:
                while max_h:
                    x = -heapq.heappop(max_h)
                    if count.get(x, 0) > 0:
                        count[x] -= 1
                        if count[x] == 0:
                            del count[x]
                        break
            else:
                while min_h:
                    x = heapq.heappop(min_h)
                    if count.get(x, 0) > 0:
                        count[x] -= 1
                        if count[x] == 0:
                            del count[x]
                        break

    if count:
        print(max(count), min(count))
    else:
        print("EMPTY")

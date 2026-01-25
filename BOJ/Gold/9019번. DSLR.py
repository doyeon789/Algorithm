import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    before, after = map(int,sys.stdin.readline().rstrip().split())

    visited = [False for i in range(10001)]
    q = deque()
    q.append([before,''])
    visited[before] = True

    while q:
        num, command = q.popleft()

        if num == after:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append([s, command + 'S'])

        l = ((num % 1000)*10) + (num // 1000)
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        r = ((num % 10) * 1000) + (num // 10)
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])

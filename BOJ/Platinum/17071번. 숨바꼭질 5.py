from collections import deque
import sys
input=sys.stdin.readline

def bfs():

    q = deque()
    q.append((N,0))

    while q:
        x,time=q.popleft()
        time+=1
        NK = K + time*(time+1)//2

        if N==K:
            print(time)

        if not 0<=NK<=MAX:
            print(-1)
            break

        for nx in [x-1, x+1, x*2]:

            if 0 <= nx <= MAX:
                if nx == NK:
                    print(time)
                    break
                else:
                    q.append((nx,time))

    print(-1)

N, K = map(int, input().split())

MAX = 500000
time = 0

bfs()
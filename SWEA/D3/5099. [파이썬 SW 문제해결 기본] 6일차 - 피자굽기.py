from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    fire_queue = deque()
    for i in range(N):
        fire_queue.append([i, cheeses[i]])   # 리스트로 변경

    waiting_queue = deque()
    for i in range(N, M):
        waiting_queue.append([i, cheeses[i]])

    while len(fire_queue) > 1:
        idx, cheese = fire_queue.popleft()
        cheese //= 2

        if cheese > 0:
            fire_queue.append([idx, cheese])
        else:
            if waiting_queue:
                fire_queue.append(waiting_queue.popleft())

    print(f"#{tc} {fire_queue[0][0] + 1}")

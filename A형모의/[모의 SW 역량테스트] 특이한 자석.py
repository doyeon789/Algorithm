from collections import deque


def rotate(index, d):
    if d == 1:
        gears[index].appendleft(gears[index].pop())
    elif d == -1:
        gears[index].append(gears[index].popleft())

T = int(input())
for tc in range(1,T+1):
    K = int(input())
    gears = [deque(map(int, input().split())) for _ in range(4)]
    
    for _ in range(K):
        n, d = map(int, input().split())
        n -= 1
        move = [(n, d)]
    
        temp = d
        for i in range(n - 1, -1, -1):
            if gears[i][2] != gears[i + 1][6]:
                temp *= -1
                move.append((i, temp))
            else:
                break
    
        temp = d
        for i in range(n + 1, 4):
            if gears[i][6] != gears[i - 1][2]:
                temp *= -1
                move.append((i, temp))
            else:
                break
    
        for idx, direction in move:
            rotate(idx, direction)
    
    answer = 0
    for i in range(4):
        if gears[i][0] == 1:
            answer += 2**i
    
    print(f"#{tc} {answer}")

'''
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1 
1 1
3 -1
'''

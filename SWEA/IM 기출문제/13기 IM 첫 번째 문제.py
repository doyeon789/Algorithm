from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def get_len(r,c):


    q = deque()
    q.append((r,c))
    cnt = 1

    while q:
        i, j = q.popleft()

        min_value = mx_num+1
        mi = 0
        mj = 0

        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]
            if 0 <= ni < N and 0 <= nj < N:     
                if grid[ni][nj] < grid[i][j]:    
                    if min_value > grid[ni][nj]:
                        min_value = grid[ni][nj]
                        mi = ni
                        mj = nj

        if min_value == mx_num+1:
            continue
        else:
            q.append((mi,mj))
            cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    mx_num = max(map(max, grid))
    ans = 0

    for i in range(N):
        for j in range(N):
            if mx_num == grid[i][j]:
                ans = max(ans, get_len(i, j))

    print(f"#{tc} {ans}")
'''
1
3
1 15 3
2 20 6
3 14 9
'''
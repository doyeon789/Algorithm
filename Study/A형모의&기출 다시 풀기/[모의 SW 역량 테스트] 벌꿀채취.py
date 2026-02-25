def get_A_honey(arr, C):
    best = 0
    for mask in range(1<<len(arr)):
        profit = 0
        honey_cnt = 0
        for k in range(len(arr)):
            if mask & (1<<k):
                honey_cnt += arr[k]
                if honey_cnt > C:
                    break
                profit += arr[k]*arr[k]
        else:
            best = max(best, profit)
    return best

T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int, input().split())
    beehive = [list(map(int, input().split())) for _ in range(N)]

    A_honey = [[0]*N for _ in range(N)]
    result = 0
    for i1 in range(N):
        for j1 in range(N-M+1):
            M_arr = beehive[i1][j1:j1+M]
            A_honey[i1][j1] = get_A_honey(M_arr, C)

    for i1 in range(N):
        for j1 in range(N-M+1):
            for i2 in range(i1, N):
                start = 0
                if i1 == i2:
                    start = j1 + M
                for j2 in range(start, N-M+1):
                    result = max(result, A_honey[i1][j1] + A_honey[i2][j2])

    print(f"#{tc} {result}")

"""
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
"""
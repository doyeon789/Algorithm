T = int(input())

for t in range(1,T+1):
    N ,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_arr = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += arr[i+k][j+l]
            sum_arr.append(sum)
    print(f"#{t} {max(sum_arr)}")
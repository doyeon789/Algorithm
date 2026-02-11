T = int(input())
for tc in range(1,T+1):
    N = int(input())
    freights = [list(map(int, input().split())) for _ in range(N)]

    freights.sort(key=lambda x: x[1])

    cnt = 0
    end = 0

    for s, e in freights:
        if end <= s:
            end = e
            cnt += 1
    print(f'#{tc} {cnt}')
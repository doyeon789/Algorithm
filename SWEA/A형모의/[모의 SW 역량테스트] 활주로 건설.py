def check(line):
    is_runway = [0] * N

    for i in range(1, N):
        diff = line[i] - line[i-1]

        if abs(diff) > 1:
            return False

        # 오르막
        if diff == 1:
            if i - X < 0:
                return False

            for x in range(X):
                if line[i-1-x] != line[i-1] or is_runway[i-1-x]:
                    return False

            for x in range(X):
                is_runway[i-1-x] = 1

        # 내리막
        elif diff == -1:
            if i + X - 1 >= N:
                return False

            for x in range(X):
                if line[i+x] != line[i] or is_runway[i+x]:
                    return False

            for x in range(X):
                is_runway[i+x] = 1

    return True

T = int(input())
for tc in range(1,T+1):
    N, X = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 가로
    for i in range(N):
        if check(matrix[i]):
            cnt += 1

    # 세로
    for c in range(N):
        column = [matrix[r][c] for r in range(N)]
        if check(column):
            cnt += 1

    print(f"#{tc} {cnt}")

def dfs(idx, current_sum):
    if idx == N:
        sums.append(current_sum)
        return

    dfs(idx + 1, current_sum + H[idx])
    dfs(idx + 1, current_sum)

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    sums = []
    ans = []

    dfs(0, 0)

    for ss in sums:
        if ss >= B:
            ans.append(ss)

    print(f"#{tc} {min(ans)-B}")

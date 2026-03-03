import sys
sys.setrecursionlimit(10**6)

def solve(n, color):
    if n == 0:
        return arr[n][color]

    if dp[n][color]:
        return dp[n][color]

    ans = 10e6
    for diff_color in range(3):
        if diff_color == color:
            continue
        ans = min(ans, solve(n - 1, diff_color))

    dp[n][color] = ans + arr[n][color]
    return dp[n][color]

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(N + 1)]

ans = min(solve(N - 1, 0), solve(N - 1, 1), solve(N - 1, 2))

print(ans)
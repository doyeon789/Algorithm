import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wv_list = [[0,0]]
for _ in range(N):
    wv_list.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = wv_list[i][0]
        value = wv_list[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[N][K])
N = int(input())
MOD = 1e9
dp = [[[0]*1024 for _ in range(10)] for _ in range(N+1)]
 
for i in range(1, 10):
    dp[1][i][1<<i] = 1
 
for n in range(2, N+1):
    for i in range(10):
        for bit in range(1024):
            if i == 0:
                dp[n][i][bit | (1<<i)] += dp[n-1][i+1][bit]
            elif i == 9:
                dp[n][i][bit | (1<<i)] += dp[n-1][i-1][bit]
            else:
                dp[n][i][bit | (1<<i)] += dp[n-1][i-1][bit] + dp[n-1][i+1][bit]
            
            dp[n][i][bit | (1<<i)] %= MOD
    
res = 0
for i in range(10):
    res += dp[N][i][2**10-1]
 
print(int(res%MOD))
import sys
input = sys.stdin.readline

INF = float('inf')

C, N = map(int, input().split())
mp_list = [[0,0]] #money human
for _ in range(N):
    mp_list.append(list(map(int, input().split())))

dp = [INF]*(C+101)
dp[0] = 0

for money, people in mp_list:
    for i in range(people,C+101):
        dp[i] = min(dp[i], dp[i-people]+money)

print(min(dp[C:]))
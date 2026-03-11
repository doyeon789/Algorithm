import bisect
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = []

for i in arr:
    k = bisect.bisect_left(dp, i)
    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))
n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n
prev = [-1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

length = max(dp)
idx = dp.index(length)

result = []
while idx != -1:
    result.append(arr[idx])
    idx = prev[idx]

result.reverse()

print(length)
print(*result)
def sol(array):
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

N = int(input())
arr = list(map(int, input().split()))
print(sol(arr))
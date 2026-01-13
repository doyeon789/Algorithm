N, K = map(int, input().split())
value = [0]*N
for i in range(N):
    value[i] = int(input())

count = 0

for coin in reversed(value):
    if K == 0:
        break
    count += K // coin
    K %= coin

print(count)

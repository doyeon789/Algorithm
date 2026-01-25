import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_unique = sorted(set(arr))

compress = {value: idx for idx, value in enumerate(sorted_unique)}

for x in arr:
    print(compress[x], end=' ')

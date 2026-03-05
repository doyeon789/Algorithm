N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0

sum_num = 0
min_len = 1e9


while True:
    if sum_num >= S:
        min_len = min(min_len, right - left)
        sum_num -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum_num += arr[right]
        right += 1

if min_len == 1e9:
    print(0)
else:
    print(min_len)
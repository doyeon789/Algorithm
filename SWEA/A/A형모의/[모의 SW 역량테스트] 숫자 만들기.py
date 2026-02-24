T = int(input())

def dfs(idx, current, plus, minus, mul, div):
    global max_num, min_num

    if idx == N:
        max_num = max(max_num, current)
        min_num = min(min_num, current)
        return

    if plus > 0:
        dfs(idx + 1, current + nums[idx], plus - 1, minus, mul, div)

    if minus > 0:
        dfs(idx + 1, current - nums[idx], plus, minus - 1, mul, div)

    if mul > 0:
        dfs(idx + 1, current * nums[idx], plus, minus, mul - 1, div)

    if div > 0:
        if current < 0:
            dfs(idx + 1, -(-current // nums[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, current // nums[idx], plus, minus, mul, div - 1)


for tc in range(1, T + 1):
    N = int(input())
    signs_num = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_num = -float('inf')
    min_num = float('inf')

    dfs(1, nums[0], signs_num[0], signs_num[1], signs_num[2], signs_num[3])

    print(f"#{tc} {max_num - min_num}")

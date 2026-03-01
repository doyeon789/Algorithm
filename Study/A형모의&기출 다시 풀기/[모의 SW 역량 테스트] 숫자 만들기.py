
def dfs(idx, num, plus, minus, mul, div):
    global max_num, min_num

    if idx == (N-1):
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return
    
    next_num = numbers[idx + 1]
    if plus > 0:
        dfs(idx + 1, num + next_num, plus - 1, minus, mul, div)

    if minus > 0:
        dfs(idx + 1, num - next_num, plus, minus - 1, mul, div)

    if mul > 0:
        dfs(idx + 1, num * next_num, plus, minus, mul - 1, div)

    if div > 0:
        if num < 0:
            dfs(idx + 1, -(-num // next_num), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, num // next_num, plus, minus, mul, div - 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    symbols = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_num = -float('inf')
    min_num = float('inf')

    dfs(0, numbers[0], symbols[0], symbols[1], symbols[2], symbols[3])

    print(f"#{tc} {max_num-min_num}")

"""
5
2 1 0 1
3 5 3 7 9
"""
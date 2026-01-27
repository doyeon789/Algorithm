
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))

    the_tallest = max(trees)
    tt_diff = 0
    odd = 0
    for tree in trees:
        diff = the_tallest - tree
        tt_diff += diff
        if diff % 2:
            odd += 1

    days = (tt_diff // 3) * 2 + (tt_diff % 3)
    one = days // 2 + days % 2
    two = days // 2

    if odd <= one:
        result = days
    else:
        result = 2 * odd - 1
        
    print(f'#{t} {result}')

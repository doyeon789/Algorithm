
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for tc in range(1, T + 1):
    y, m, d, w = map(int, input().split())
    n, k = map(int, input().split())

    total = 0

    while total < k:

        if w <= 3:
            eat = n
        elif w == 4:
            eat = 0
        elif w == 5 or w == 6:
            eat = n + 1

        total += eat

        if total >= k:
            break

        w = (w + 1) % 7
        d += 1

        if d > days[m]:
            d = 1
            m += 1
            if m > 12:
                m = 1
                y += 1

    print(f"#{tc} {y:04d} {m:02d} {d:02d}")

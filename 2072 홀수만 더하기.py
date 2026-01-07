T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0

    for n in numbers:
        if n % 2 == 1:
            total += n

    print(f"#{tc} {total}")

"""
T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print(f"#{tc} {sum(n for n in numbers if n % 2 == 1)}")
"""
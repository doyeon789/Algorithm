n = int(input())

def hanoi(n, start, to, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, end, to)
        print(start, end)
        hanoi(n - 1, to, start, end)

print(2 ** n - 1)
hanoi(n, 1, 2, 3)
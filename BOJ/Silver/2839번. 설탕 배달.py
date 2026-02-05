N = int(input())

if N == 0:
    print(0)
    exit()

count = 0
while N > 0:
    if N % 5 == 0:
        count += (N // 5)
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)
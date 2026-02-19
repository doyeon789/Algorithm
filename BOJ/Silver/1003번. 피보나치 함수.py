def fibonacci(n):
    global cnt_zero
    global cnt_one
    if (n == 0):
        cnt_zero+=1
        return 0
    elif (n == 1):
        cnt_one+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = int(input())

for _ in range(T):
    cnt_zero=0
    cnt_one=0
    N = int(input())
    fibonacci(N)
    print(cnt_zero, cnt_one)
T = int(input())
for tc in range(1,T+1):
    answer = 0
    N, K = map(int,input().split())
    arr = list(map(str,input().strip()))

    password = set()
        
    for _ in range(N // 4):
        side = N // 4
        start = 0
        for _ in range(4):
            password.add(''.join(arr[start:start+side]))
            start += side
        arr.insert(0, arr.pop())

    password = list(password)
    for i in range(len(password)):
        password[i] = int(password[i],16)

    password.sort(reverse=True)
    answer = password[K-1]
    print(f"#{tc} {answer}")
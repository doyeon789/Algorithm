T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    password_num = list(input().strip())
    
    password_cand = set()
    
    for _ in range(N // 4):
        for i in range(4):
            password_cand.add(''.join(password_num[i*3:i*3+3]))
     
        password_num.insert(0, password_num.pop())
    
    password_cand = list(password_cand)
    for i in range(len(password_cand)):
        password_cand[i]  = int(password_cand[i], 16)

    password_cand.sort(reverse = True)

    print(f"#{tc} {password_cand[K-1]}")

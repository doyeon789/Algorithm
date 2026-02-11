T = int(input())
for tc in range(1,T+1):
    
    N = int(input())
    
    lst = [2,3,5,7,11]
    cnt =[0]*5
    for i in range(5):
        while N % lst[i] == 0:
            cnt[i] += 1
            N //= lst[i]

    print(f"#{tc}", *cnt)
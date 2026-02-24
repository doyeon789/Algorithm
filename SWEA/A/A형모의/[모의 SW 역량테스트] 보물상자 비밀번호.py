T = int(input())
for tc in range(1,T+1):
    answer = 0
    n, k = map(int,input().split())
    lock_num = list(map(str,input().strip()))

    possible_outcomes = set()
     
    for _ in range(n // 4):
        side = n // 4
        start = 0
        for _ in range(4):
            possible_outcomes.add(''.join(lock_num[start:start+side]))
            start += side
        lock_num.insert(0, lock_num.pop())
    
    possible_outcomes = list(possible_outcomes)
    for i in range(len(possible_outcomes)):
        possible_outcomes[i] = int(possible_outcomes[i],16)

    possible_outcomes.sort(reverse=True)
    answer = possible_outcomes[k-1]

    print(f"#{tc} {answer}")

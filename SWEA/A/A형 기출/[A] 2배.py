T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    
    total = sum(A)
    target = 2 * N
    
    # 이미 조건 만족하면 0
    if total >= target:
        print(f"#{tc} 0")
        continue
    
    gains = []
    
    # 각 위치에서 작업했을 때 증가량 계산
    for i in range(N):
        idx = i + 1
        new_value = max(A[i] + idx, idx)
        gain = new_value - A[i]
        gains.append(gain)
    
    # 증가량 큰 순서대로 정렬
    gains.sort(reverse=True)
    
    count = 0
    
    # 큰 것부터 더하기
    for g in gains:
        total += g
        count += 1
        if total >= target:
            break
    
    print(f"#{tc} {count}")

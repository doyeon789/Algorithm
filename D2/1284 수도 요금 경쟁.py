T = int(input())

for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    a_ans = P * W
    b_ans = Q if W <= R else Q + (W - R) * S
    
    print(f"#{tc} {min(a_ans, b_ans)}")

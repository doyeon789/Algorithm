import sys
input = sys.stdin.readline

N, B, C = map(int, input().split())
x = list(map(int, input().split()))
x += [0, 0]

result = 0

if B <= C:
    print(sum(x[:N]) * B)
else:
    for i in range(N):

        if x[i+1] > x[i+2]:
            two = min(x[i], x[i+1] - x[i+2])
            x[i] -= two
            x[i+1] -= two
            result += (B + C) * two

        three = min(x[i], x[i+1], x[i+2])
        x[i] -= three
        x[i+1] -= three
        x[i+2] -= three
        result += (B + 2*C) * three

        two = min(x[i], x[i+1])
        x[i] -= two
        x[i+1] -= two
        result += (B + C) * two

        result += B * x[i]
        x[i] = 0

    print(result)

"""
1. 1개 = B원, 2개 묶음 = B + C원, 3개 묶음 = B + 2C원
    B > C 일때 3 -> 2 -> 1 순으로 구매
    B <= C 일때 묶는 이득 X -> 전부 1개씩 구매

2. 하지만 항상 3개부터 시작 -> 최적 X
   ex) 2 3 2 1
   원인: x[i+1] > x[i+2] 인 상황
   (3개 먼저 사면 -> i+1 위치 수량이 남음
    -> 이후 1개(B원)로 처리될 가능성 증가)
   3개를 먼저 사면 오히려 손해 발생 가능

3. x[i+1] > x[i+2]일 때, (x[i+1] - x[i+2])만큼 2개 묶음 먼저 구매 -> i+1과 i+2 수량 균형 맞추기

4. 이후 3개 -> 2개 -> 1개 순으로 처리
   -> 항상 최솟값
"""
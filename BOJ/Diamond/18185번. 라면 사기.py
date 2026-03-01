import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
x += [0, 0] 

result = 0

for i in range(N):

    if x[i+1] > x[i+2]:
        two_cnt = min(x[i], x[i+1] - x[i+2])
        x[i] -= two_cnt
        x[i+1] -= two_cnt
        result += 5 * two_cnt
        
    three_cnt = min(x[i], x[i+1], x[i+2])
    x[i] -= three_cnt
    x[i+1] -= three_cnt
    x[i+2] -= three_cnt
    result += 7 * three_cnt

    two_cnt = min(x[i], x[i+1])
    x[i] -= two_cnt
    x[i+1] -= two_cnt
    result += 5 * two_cnt

    result += 3 * x[i]
    x[i] = 0

print(result)

"""
1. 3개 묶음(7원), 2개(5원), 1개(3원)순으로 작아짐
    기본 전략은 3개 → 2개 → 1개 순

2. 항상 3개부터 시작 -> 최적 X
    ex) 2 3 2 1
    (원인: x[i+1] > x[i+2] 인 상황)
    ( 3개 먼저 사면 i+1이 남음. -> 비싼거 1개로 구미 처리 가능성)
    3개를 먼저 사면 손해가 발생

3. x[i+1] > x[i+2] 일때 (x[i+1] - x[i+2])만큼 2개 묶음을 먼저 구매해 수량을 맞춘다.

5. 이후 3개, 2개, 1개 순으로 처리 -> 항상 최솟값
"""
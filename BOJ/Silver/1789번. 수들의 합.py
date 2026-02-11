# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알때, 자연수 N의 최대값은 ?
S = int(input())

minus = 0

while S >= 0:
    minus += 1
    S -= minus

if S == 0:
    print(minus)
else:
    print(minus-1)
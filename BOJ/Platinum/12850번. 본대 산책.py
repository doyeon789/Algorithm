import sys
input = sys.stdin.readline

MOD = 1000000007

D = int(input())

v = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

def multiply(M1, M2):
    ret = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            elem = 0
            for k in range(8):
                elem += M1[i][k] * M2[k][j]
                elem %= MOD
            ret[i][j] = elem
    return ret

# 단위 행렬
ans = [[0] * 8 for _ in range(8)]
for i in range(8):
    ans[i][i] = 1

factor = v

while D > 0:
    if D % 2 == 1:
        ans = multiply(ans, factor)
    factor = multiply(factor, factor)
    D //= 2

print(ans[0][0])
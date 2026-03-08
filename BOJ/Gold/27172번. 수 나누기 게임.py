import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

S = set(arr)
M = max(arr)
score = [0] * (M+1)
for i in S:
    if i == M :
        continue
    else:
        for j in range(2*i, M+1, i):
            if j in S:
                score[i] += 1
                score[j] -= 1

for i in arr:
    print(score[i], end=' ')
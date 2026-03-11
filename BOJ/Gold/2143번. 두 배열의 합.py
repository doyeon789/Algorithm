import sys
import bisect
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = 0
Asum = A
Bsum = B

for start in range(N):
    for end in range(start+1, N):
        Asum.append(sum(A[start:end+1]))

for start in range(M):
    for end in range(start+1, M):
        Bsum.append(sum(B[start:end+1]))

Asum.sort()
Bsum.sort()

for i in range(len(Asum)):
    l = bisect.bisect_left(Bsum, T-Asum[i])
    r = bisect.bisect_right(Bsum, T-Asum[i])
    result += r-l

print(result)
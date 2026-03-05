import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

palindrom = [[0]*N for _ in range(N)]

for i in range(N):
    palindrom[i][i] = 1
    if i+1 < N and arr[i] == arr[i+1]:
        palindrom[i][i+1] = 1

for i in range(N-2,-1,-1):
    for j in range(i,N):
        if arr[i] == arr[j] and palindrom[i + 1][j - 1]:
            palindrom[i][j] = 1

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(palindrom[a-1][b-1])
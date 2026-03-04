import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    visited[n] = True

    for nx in tree[n]:
        if not visited[nx]:
            dfs(nx)
            dp[n] += dp[nx]

N, R, Q = map(int, input().split())
tree =[[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for _ in range(N+1)]
dp = [1]*(N+1)

dfs(R)

for _ in range(Q):
    n = int(input())
    print(dp[n])
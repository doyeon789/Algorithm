import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

inp = [[] for _ in range(n + 1)]
g = [[] for _ in range(n + 1)]

dep = [0] * (n + 1)
fu = [0] * (n + 1)
su = [0] * (n + 1)
ab = [0] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    inp[s].append(e)
    inp[e].append(s)


def dfs(v, p):
    for i in inp[v]:
        if i == p:
            continue

        if dep[i] == 0:
            g[v].append(i)
            dep[i] = dep[v] + 1

            t = fu[v]
            dfs(i, v)

            ab[i] = fu[v] - t
            fu[v] += fu[i]
            su[v] += su[i]

        elif dep[i] < dep[v]:
            fu[i] += 1
            su[v] += 1


dep[1] = 1
dfs(1, -1)

ans = 0
for i in range(1, n + 1):
    ok = 1
    for ch in g[i]:
        if su[ch] - ab[ch] > 1 or fu[ch] != 0:
            ok = 0
            break

    if m - n + 1 - su[i] != 0:
        ok = 0

    if ok:
        ans += i

print(ans)
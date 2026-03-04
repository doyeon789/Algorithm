import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()
parent = [i for i in range(n+1)]

total = 0
count = 0
bg_cost = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        bg_cost = cost
        total += cost
        count += 1

        if count == n-1:
            break

print(total-bg_cost)

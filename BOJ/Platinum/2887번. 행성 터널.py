import sys
input = sys.stdin.readline

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True


N = int(input())

x_list = []
y_list = []
z_list = []

for idx in range(N):
    x, y, z = map(int, input().split())
    x_list.append((x, idx))
    y_list.append((y, idx))
    z_list.append((z, idx))

x_list.sort()
y_list.sort()
z_list.sort()

edges = []
for i in range(N - 1):
    cost = x_list[i + 1][0] - x_list[i][0]
    a = x_list[i][1]
    b = x_list[i + 1][1]
    edges.append((cost, a, b))

    cost = y_list[i + 1][0] - y_list[i][0]
    a = y_list[i][1]
    b = y_list[i + 1][1]
    edges.append((cost, a, b))

    cost = z_list[i + 1][0] - z_list[i][0]
    a = z_list[i][1]
    b = z_list[i + 1][1]
    edges.append((cost, a, b))

edges.sort()

parent = [i for i in range(N)]
result = 0

for cost, a, b in edges:
    if union(parent, a, b):
        result += cost

print(result)
"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19   
"""
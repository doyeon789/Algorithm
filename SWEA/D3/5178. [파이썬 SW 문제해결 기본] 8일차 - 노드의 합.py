T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 1, -1):
        tree[i//2] += tree[i]

    print(f"#{tc} {tree[L]}")
    
def dfs(start, end):

    if start == end:
        return 1
    
    stack = [start]
    visited = [False] * (V + 1)

    while stack:
        now = stack.pop()

        if visited[now]:
            continue
        visited[now] = True

        for nxt in graph[now]:
            if not visited[nxt]:
                stack.append(nxt)

    return 1 if visited[end] else 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    S, G = map(int, input().split())
    print(f"#{tc} {dfs(S, G)}")


'''
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''
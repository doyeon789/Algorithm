import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

# 정방향 그래프: a -> b (a가 b보다 뒤/작음)
graph = [[] for _ in range(N + 1)]
# 역방향 그래프: b <- a
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    reverse_graph[b].append(a)


# DFS 함수
def dfs(start, graph):
    visited = [False] * (N + 1)
    stack = [start]
    visited[start] = True
    count = 0

    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                count += 1
    return count


answer = 0

for v in range(1, N + 1):
    # 나보다 뒤에 있는 사람 수
    down = dfs(v, graph)
    # 나보다 앞에 있는 사람 수
    up = dfs(v, reverse_graph)

    if up + down == N - 1:
        answer += 1

print(answer)

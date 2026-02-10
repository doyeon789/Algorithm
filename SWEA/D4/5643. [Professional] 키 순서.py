from collections import deque

def than_cnt(graph, start):
    q = deque([start])
    visited = set()
    cnt = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N+1)]
    reversed_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        reversed_graph[b].append(a)

    answer = 0

    for i in range(1, N+1):
        smaller = than_cnt(reversed_graph, i)
        taller = than_cnt(graph, i)

        if smaller + taller == N - 1:
            answer += 1

    print(f"#{tc} {answer}")

'''
1
6
6
1 5
3 4
5 4
4 2
4 6
5 2
'''
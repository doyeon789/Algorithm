from itertools import combinations
import sys
sys.setrecursionlimit(10**6)

N = int(input())
nums = list(map(int, input().split()))

N_list = [i for i in range(1, N+1)]
case_list = []

for i in range(1, (N//2) + 1):
    for comb in combinations(N_list, i):
        first = list(comb)
        last = list(set(N_list) - set(first))
        case_list.append((first, last))

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in data[1:]:
        graph[i].append(j)

def check(area):
    visited = [False] * (N+1)

    def dfs(x):
        visited[x] = True
        for nxt in graph[x]:
            if not visited[nxt] and nxt in area:
                dfs(nxt)

    dfs(area[0])

    for i in area:
        if not visited[i]:
            return False
    return True


ans = float('inf')

for area1, area2 in case_list:

    if not check(area1):
        continue
    if not check(area2):
        continue

    sum_area1 = sum(nums[i-1] for i in area1)
    sum_area2 = sum(nums[i-1] for i in area2)

    ans = min(ans, abs(sum_area1 - sum_area2))


print(-1 if ans == float('inf') else ans)
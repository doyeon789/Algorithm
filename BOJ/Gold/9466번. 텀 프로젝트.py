import sys
input = sys.stdin.readline

def dfs(i):
    global team_members

    visited[i] = True
    team.append(i)
    select = arr[i]
     
    if visited[select]:
        if select in team:
            team_members += len(team[team.index(select):])
    else:
        dfs(select)

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    visited = [False] * (n+1)
    team_members = 0

    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n-team_members)
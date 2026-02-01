dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs_stack(si, sj, visited):
    stack = [(si, sj)]
    visited[si][sj] = True

    while stack:
        i, j = stack.pop()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

n = int(input())
h_map = [list(map(int, input().split())) for _ in range(n)]

value = {0}
for row in h_map:
    value.update(row)

result = 0
for h in value:
    ans = 0
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if h_map[i][j] <= h:
                visited[i][j] = True

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                ans += 1
                dfs_stack(i, j, visited)

    result = max(result, ans)

print(result)
    

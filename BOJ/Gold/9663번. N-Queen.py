import sys

n = int(sys.stdin.readline())

visited = [-1] * n

def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row]-visited[row]):
            return False
    return True

cnt = 0
def dfs(row):
    global cnt
    
    if row == n:
        cnt += 1
    
    else:
        for col in range(n):
            visited[row] = col
            if check(row):
                dfs(row + 1)
dfs(0)
print(cnt)

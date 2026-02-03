import sys

def dfs(x, y, count):
    global reuslt
    reuslt = max(reuslt, count)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if  0 <= nx < r and 0 <= ny < c:
            al_num = ord(board[nx][ny]) - 65
            if visited[al_num] == 0:
                visited[al_num] = 1
                dfs(nx, ny, count+1)
                visited[al_num] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, sys.stdin.readline().split())
board = [list(map(str,input().strip())) for _ in range(r)]

visited = [0] * 26
visited[ord(board[0][0])-65] = 1

reuslt = 1

dfs(0, 0, 1)
print(reuslt)
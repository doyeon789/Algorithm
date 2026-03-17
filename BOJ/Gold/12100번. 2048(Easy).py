import sys
input = sys.stdin.readline

def left_upd(board):
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if not board[i][cursor]:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[i][cursor] = tmp
    return board

def right_upd(board):
    for i in range(n):
        cursor = n - 1
        for j in range(n - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up_upd(board):
    for j in range(n):
        cursor = 0
        for i in range(n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down_upd(board):
    for j in range(n):
        cursor = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

result = 0
def dfs(k, arr):
    global result
    if k == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > result:
                    result = arr[i][j]
        return

    for i in range(4):
        copy_arr = [ar[:] for ar in arr]
        if i == 0:
            dfs(k + 1, left_upd(copy_arr))
        elif i == 1:
            dfs(k + 1, right_upd(copy_arr))
        elif i == 2:
            dfs(k + 1, up_upd(copy_arr))
        else:
            dfs(k + 1, down_upd(copy_arr))

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dfs(0, board)
print(result)
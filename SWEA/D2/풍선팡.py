def get_paper_flow_powder(i, j):
    total = board[i][j]
    for d in range(4):
        for a in range(1, board[i][j] + 1):
            nx = i + dx[d] * a
            ny = j + dy[d] * a
            if 0 <= nx < col and 0 <= ny < row:
                total += board[nx][ny]
    return total


dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for tc in range(1,T+1):
    result = 0
    col,row = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(col)]

    for i in range(col):
        for j in range(row):
            result = max(result, get_paper_flow_powder(i,j))

    print(f"#{tc} {result}")

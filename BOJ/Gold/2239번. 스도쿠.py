import sys
input = sys.stdin.readline

SIZE = 9

sudoku = [list(map(int, input().strip())) for _ in range(SIZE)]

row = [[False]*10 for _ in range(SIZE)]
col = [[False]*10 for _ in range(SIZE)]
box = [[False]*10 for _ in range(SIZE)]

blank = []

for i in range(SIZE):
    for j in range(SIZE):
        num = sudoku[i][j]
        if num == 0:
            blank.append((i, j))
        else:
            row[i][num] = True
            col[j][num] = True
            box[(i//3)*3 + (j//3)][num] = True

def dfs(idx):
    if idx == len(blank):
        for i in sudoku:
            print(''.join(map(str,i)))
        sys.exit()

    i, j = blank[idx]
    b = (i//3)*3 + (j//3)
    for num in range(1, 10):
        if not row[i][num] and not col[j][num] and not box[b][num]:
            sudoku[i][j] = num
            row[i][num] = col[j][num] = box[b][num] = True

            dfs(idx+1)

            sudoku[i][j] = 0
            row[i][num] = col[j][num] = box[b][num] = False

dfs(0)
T = int(input())

for t in range(1,T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    sudoku_R =  [[0]*9 for _ in range(9)]
    sudoku_s = []
    answer = 1

    for i in range(9):
        for j in range(9):
            sudoku_R[j][i] = sudoku[i][j]
    #3*3칸 비교
    for i in range(9):
        for j in range(9):
            arr = []
            if i%3==0 and j%3==0:
                for k in range(3):
                    for l in range(3):
                        arr.append(sudoku[i+k][j+l])
                sudoku_s.append(arr)

    for k in range(9):
        if len(set(sudoku[k])) != 9:
            answer = 0
            break
        if len(set(sudoku[k])) != 9:
            answer = 0
            break
        if len(set(sudoku[k])) != 9:
            answer = 0
            break

    print(f"#{t} {answer}")


sudocu = [list(map(int, input().split())) for _ in range(9)]
sudocu_R =  [[0]*9 for _ in range(9)]
sudocu_s = []
answer = 0

for i in range(9):
    for j in range(9):
        sudocu_R[j][i] = sudocu[i][j]
#3*3칸 비교
for i in range(9):
    for j in range(9):
        arr = []
        if i%3==0 and j%3==0:
            for k in range(3):
                for l in range(3):
                    arr.append(sudocu[i+k][j+l])
            sudocu_s.append(arr)

for k in range(9):
    if len(set(sudocu[k])) != 9:
        answer = 0
        break
    if len(set(sudocu_R[k])) != 9:
        answer = 0
        break
    if len(set(sudocu_s[k])) != 9:
        answer = 0
        break

print(answer)
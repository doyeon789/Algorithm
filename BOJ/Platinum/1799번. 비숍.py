N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]

ans = [0,0]
l = [0] * (2*N)
r = [0] * (2*N)
def tracking(row, col, count, color):
    if col >= N:
        row += 1
        if col % 2 == 0:
            col = 1
        else:
            col = 0
    if row >= N:
        ans[color] = max(ans[color],count)
        return
    
    if chess[row][col] and not l[col - row + N - 1] and not r[row+col]:
        l[col - row + N - 1] = r[row + col] = 1
        tracking(row, col+2, count+1, color)
        l[col - row + N - 1] = r[row + col] = 0
    tracking(row, col+2, count, color)

tracking(0, 0, 0, 0)
tracking(0, 1, 0, 1)

print(ans[0]+ans[1])
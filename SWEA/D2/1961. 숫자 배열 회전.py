T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]
    arr = [[0]*3 for _ in range(n)]

    for i in range(n):
        arr[i][0] = ''.join([str(board[j][i]) for j in range(n)])[::-1]
        arr[i][1] = ''.join([str(board[n-i-1][n-j-1]) for j in range(n)])
        arr[i][2] = ''.join([str(board[j][n-i-1]) for j in range(n)])
    
    print(f"#{test_case}")
    for i in range(n):
        print(''.join(str(arr[i][j])+" " for j in range(3)))

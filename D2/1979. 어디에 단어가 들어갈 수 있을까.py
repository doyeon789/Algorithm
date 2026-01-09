T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    word_count = 0
    
    for row in board:
        count = 0
        for i in range(N):
            if row[i] == 1:
                count += 1
            else:
                if count == M:
                    word_count += 1
                count = 0
        if count == M:
            word_count += 1
    
    for col in range(N):
        count = 0
        for row in range(N):
            if board[row][col] == 1:
                count += 1
            else:
                if count == M:
                    word_count += 1
                count = 0
        if count == M:
            word_count += 1
    
    print(f"#{t} {word_count}")


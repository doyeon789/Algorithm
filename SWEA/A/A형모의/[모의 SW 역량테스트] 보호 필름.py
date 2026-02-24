def check(film):
    for col in range(W):
        cnt = 1
    
        for row in range(1, D):
            if film[row][col] == film[row-1][col]:
                cnt += 1
                if cnt >= K:
                    break
            else:
                cnt = 1

        if cnt < K:
            return False

    return True

def dfs(cnt,row,film):
    global min_num
    
    if cnt >= min_num:
        return
    
    if row == D:
        if check(film):
            min_num = min(min_num, cnt)
        return

    # 아무것도 안하기
    dfs(cnt, row+1, film)

    # 전부 0으로 바꾸기
    original = film[row][:]
    film[row] = [0] * W
    dfs(cnt + 1, row + 1, film)
    film[row] = original

    # 전부 1로 바꾸기
    original = film[row][:]
    film[row] = [1] * W
    dfs(cnt + 1, row + 1, film)
    film[row] = original

T = int(input())
for tc in range(1,T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    min_num = float('inf')
    dfs(0,0,films)

    print(f"#{tc} {min_num}")

"""
6 8 3         
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1


6 8 4
1 1 0 0 0 1 1 0
1 0 1 0 0 1 1 1
0 1 0 0 1 1 0 0
1 0 1 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 0 0 1 1 1 1
"""

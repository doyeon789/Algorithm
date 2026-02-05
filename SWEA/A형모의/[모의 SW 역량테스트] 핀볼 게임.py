"""
-1 : 블랙홀 -> 게임 끝
0 : 빈공간
1~5 블록
6~10 웜홀

게임 끝: 블랙홀, 원좀으로 돌아옴

점수 : 벽이나 블록에 부딪힌 수, 웜홀 X
"""

from pprint import pprint

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

change_dir = ((),
    (1, 3, 0, 2),
    (3, 0, 1, 2),
    (2, 0, 3, 1),
    (1, 2, 3, 0),
    (1, 0, 3, 2))


def play_game(i, j, d):
    global wormhole_info
    
    score = 0
    start_i, start_j = i, j
    r, c = i, j

    while True:
        r += dx[d]
        c += dy[d]

        #원점으로 돌아오거나, -1을 만나면 종료
        if (r, c) == (start_i, start_j) or borard[r][c] == -1:
            return score
        
        #
        if 1 <= borard[r][c] <= 5:
            d = change_dir[borard[r][c]][d]
            score += 1
        elif 6 <= borard[r][c] <= 10:
            r, c = wormhole_info[(r, c)]


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    
    wormhole_check = [0] * 11
    wormhole_info = dict()
     
    borard = [[5] * (n+2)] #board의 첫 행 5로 초기화
    for i in range(1, n+1):
        # 양 끝 
        borard.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, n+1):
            #웜홀일때
            if 6 <= borard[i][j] <= 10:
                num = borard[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else: # 같은 번호의 원홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    borard.append([5] * (n+2)) #board의 마지막 행 5로 채우기

    print(wormhole_check)
    print(wormhole_info)
    
    result = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if borard[i][j] == 0:
                for d in range(4):
                    result = max(result, play_game(i, j, d))
    print(f"#{tc} {result}")
# 상, 하, 좌, 우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())

    # board : 해당 위치의 생명력
    #   0  -> 빈 칸
    #  >0  -> 살아있는 세포 (생명력 값)
    #  -1  -> 죽은 세포
    board = [[0] * (m + 2*k + 2) for _ in range(n + 2*k + 2)]

    # status : 세포의 상태 + 시간 관리
    #  <0 : 비활성 상태 (절댓값만큼 시간이 지나야 활성)
    #  >0 : 활성 상태 (남은 활성 시간)
    #   0 : 아무것도 없음 / 죽은 상태
    status = [[0] * (m + 2*k + 2) for _ in range(n + 2*k + 2)]

    # 초기 세포 배치
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(m):
            board[i][j] = data[j]
            if data[j] > 0:
                # 처음엔 비활성 상태 -> -생명력
                status[i][j] = -data[j]

    # k시간 동안 시뮬레이션
    for _ in range(k):

        # spread : 이번 시간에 새로 번식될 세포 저장용
        # (충돌 처리용 임시 배열)
        spread = [[0] * (m + 2*k + 2) for _ in range(n + 2*k + 2)]

        for i in range(n + 2*k + 2):
            for j in range(m + 2*k + 2):

                # 빈 칸이거나 이미 죽은 세포면 패스
                if board[i][j] == 0 or board[i][j] == -1:
                    continue

                # =======================
                # 1 비활성 상태
                # =======================
                if status[i][j] < 0:
                    # -1이 되면 -> 활성 상태로 전환
                    if status[i][j] == -1:
                        status[i][j] = board[i][j]
                    else:
                        # 비활성 시간 감소
                        status[i][j] += 1

                # =======================
                # 2 활성 상태
                # =======================
                elif status[i][j] > 0:
                    # 활성되는 "첫 순간"에만 번식
                    for d in range(4):
                        ni = (i + dx[d]) % (n + 2*k + 2)
                        nj = (j + dy[d]) % (m + 2*k + 2)

                        # 이미 다른 세포가 있으면 번식 불가
                        if board[ni][nj] == -1 or board[ni][nj] > 0:
                            continue

                        # 아직 번식 후보가 없으면 등록
                        if spread[ni][nj] == 0:
                            spread[ni][nj] = board[i][j]
                            status[ni][nj] = -board[i][j]

                        # 번식 충돌 -> 생명력 큰 쪽만 남김
                        elif spread[ni][nj] < board[i][j]:
                            spread[ni][nj] = board[i][j]
                            status[ni][nj] = -board[i][j]

                    # 활성 시간 처리
                    if status[i][j] == 1:
                        # 활성 끝 -> 죽음
                        board[i][j] = -1
                        status[i][j] = 0
                    else:
                        status[i][j] -= 1

        # =======================
        #  번식 결과 board에 반영
        # =======================
        for i in range(n + 2*k + 2):
            for j in range(m + 2*k + 2):
                if spread[i][j] > 0 and board[i][j] == 0:
                    board[i][j] = spread[i][j]

    # =======================
    # 살아있는 세포 수 계산
    # (비활성 + 활성)
    # =======================
    result = 0
    for i in range(n + 2*k + 2):
        for j in range(m + 2*k + 2):
            if status[i][j] != 0:
                result += 1

    print(f'#{tc} {result}')


""" 동작 X
dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # (i, j): [life, elapsed_time]
    stem_cells = dict()

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                stem_cells[(i, j)] = [board[i][j], 0]

    # k시간 시뮬레이션
    for _ in range(k):
        spread = dict()  # 번식 충돌 처리용

        # 번식 처리
        for (i, j), (life, status) in stem_cells.items():
            # 활성되는 순간만 번식
            if status == life:
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]

                    # 이미 차지하지 않은 곳
                    if (ni, nj) not in stem_cells:
                        if (ni, nj) not in spread:
                            spread[(ni, nj)] = life
                        else:
                            spread[(ni, nj)] = max(spread[(ni, nj)], life)


        # 번식 결과 반영
        for lction, life in spread.items():
            stem_cells[lction] = [life, 0]

        # 시간 증가 및 죽음 처리
        dead = []
        for lction in stem_cells:
            stem_cells[lction][1] += 1
            life, status = stem_cells[lction]
            if status == life * 2:
                dead.append(lction)

        for lction in dead:
            del stem_cells[lction]


    # 비활성 + 활성 세포 수
    result = len(stem_cells)
    print(f"#{tc} {result}")
"""

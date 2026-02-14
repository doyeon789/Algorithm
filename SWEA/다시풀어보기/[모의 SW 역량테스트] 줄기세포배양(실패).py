from collections import defaultdict

dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # (i, j): [life, state, used_time]
    # state: 0 = 비활성, 1 = 활성, 2 = 죽음
    stem_cells = dict()

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                stem_cells[(i, j)] = [board[i][j], 0, 0]

    for _ in range(K):
        new_cells = dict()

        # 현재 존재하는 세포들만 순회 (복사본 사용)
        for cells in list(stem_cells.keys()):
            life, state, used_time = stem_cells[cells]

            # 죽은 세포면 건너뛰기
            if state == 2:
                continue

            # 시간 증가
            used_time += 1
            stem_cells[cells][2] = used_time

            # 비활성 -> 활성
            if state == 0 and used_time == life:
                stem_cells[cells][1] = 1
                state = 1

                # 활성되는 순간 번식
                x, y = cells
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 이미 기존 세포 있으면 패스
                    if (nx, ny) in stem_cells:
                        continue

                    # 이번 턴에 생긴 세포 충돌 처리
                    if (nx, ny) in new_cells:
                        if new_cells[(nx, ny)][0] < life:
                            new_cells[(nx, ny)] = [life, 0, 0]
                    else:
                        new_cells[(nx, ny)] = [life, 0, 0]

            # 활성 -> 죽음
            if state == 1 and used_time == life * 2:
                stem_cells[cells][1] = 2

        # 한 시간 끝난 후 새 세포 추가
        stem_cells.update(new_cells)

    # K시간 후 살아있는 세포 개수
    result = 0
    for cells in stem_cells:
        if stem_cells[cells][1] != 2:
            result += 1

    print(f"#{tc} {result}")

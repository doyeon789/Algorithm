from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_water_temp(N, M, heaters):
    water_temp = [[-1]*M for _ in range(N)]
    dist = [[-1]*M for _ in range(N)]
    q = deque()
    for hr, hc in heaters:
        q.append((hr, hc))
        dist[hr][hc] = 0
        water_temp[hr][hc] = 28.0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                water_temp[nr][nc] = max(10.0, 28 - dist[nr][nc]*0.1)
                q.append((nr, nc))
    return water_temp

def get_ground(N, M, lands):
    is_land = [[False]*M for _ in range(N)]
    for Gr, Gc, Gra in lands:
        q = deque()
        q.append((Gr, Gc, 0))
        is_land[Gr][Gc] = True
        while q:
            r, c, d = q.popleft()
            if d == Gra:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and not is_land[nr][nc]:
                    is_land[nr][nc] = True
                    q.append((nr, nc, d+1))
    return is_land

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Hr, Hc, HL, D = map(int, input().split())
    heaters = []
    for i in range(HL):
        nr = Hr + dr[D]*i
        nc = Hc + dc[D]*i
        if 0 <= nr < N and 0 <= nc < M:
            heaters.append((nr, nc))
    water_temp = get_water_temp(N, M, heaters)
    GC = int(input())
    lands = [tuple(map(int, input().split())) for _ in range(GC)]
    is_land = get_ground(N, M, lands)
    move_T = int(input())
    MC = int(input())
    moves = [tuple(map(int, input().split())) for _ in range(MC)]
    cur_r, cur_c = Hr, Hc
    body_temp = 28.0
    move_idx = 0
    for _ in range(move_T):
        Rw, D = moves[move_idx]
        move_idx = (move_idx + 1) % MC
        for _ in range(Rw):
            attempts = 0
            while attempts < 4:
                nr = cur_r + dr[D]
                nc = cur_c + dc[D]
                if 0 <= nr < N and 0 <= nc < M:
                    cur_r, cur_c = nr, nc
                    break
                D = (D + 1) % 4
                attempts += 1
            if attempts == 4:
                break
            if is_land[cur_r][cur_c]:
                body_temp = min(28.0, body_temp + 0.2)
            else:
                body_temp = (body_temp + water_temp[cur_r][cur_c])/2
    print(f"#{tc} {body_temp:.2f}")
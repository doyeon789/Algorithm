from collections import deque

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

def mark_bc(sr, sc, coverage, power, bc_id):
    visited = [[-1] * 10 for _ in range(10)]
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 0

    while q:
        r, c = q.popleft()
        board[r][c].append((bc_id, power))

        for d in range(1, 5):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < 10 and 0 <= nc < 10):
                continue
            if visited[nr][nc] != -1:
                continue
            if visited[r][c] + 1 > coverage:
                continue

            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))


T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    A_move = [0] + list(map(int, input().split()))
    B_move = [0] + list(map(int, input().split()))

    board = [[[] for _ in range(10)] for _ in range(10)]

    for bc_id in range(A):
        x, y, c, p = map(int, input().split())
        mark_bc(y - 1, x - 1, c, p, bc_id)

    A_r, A_c = 0, 0
    B_r, B_c = 9, 9

    total_charge = 0

    for time in range(M + 1):
        A_r += dr[A_move[time]]
        A_c += dc[A_move[time]]
        B_r += dr[B_move[time]]
        B_c += dc[B_move[time]]

        a_list = board[A_r][A_c]
        b_list = board[B_r][B_c]

        max_charge = 0

        for a in a_list:
            for b in b_list:
                if a[0] == b[0]:
                    max_charge = max(max_charge, a[1])
                else:
                    max_charge = max(max_charge, a[1] + b[1])

        if not a_list and b_list:
            for b in b_list:
                max_charge = max(max_charge, b[1])
        if not b_list and a_list:
            for a in a_list:
                max_charge = max(max_charge, a[1])

        total_charge += max_charge

    print(f"#{tc} {total_charge}")

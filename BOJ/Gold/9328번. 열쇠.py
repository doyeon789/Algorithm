from collections import deque

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())

    # 맵 생성 (패딩)
    graph = [["."] * (w + 2)]
    for _ in range(h):
        graph.append(list("." + input() + "."))
    graph.append(["."] * (w + 2))

    # 열쇠
    keys = [0] * 26
    key_input = input()
    if key_input != "0":
        for k in key_input:
            keys[ord(k) - 97] = 1

    # BFS 준비
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    q = deque([(0, 0)])
    doors = [[] for _ in range(26)]

    answer = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < h + 2 and 0 <= nc < w + 2):
                continue
            if graph[nr][nc] == "*":
                continue

            ch = graph[nr][nc]
            code = ord(ch)

            # 문
            if 65 <= code <= 90:
                if not keys[code - 65]:
                    doors[code - 65].append((nr, nc))
                    continue

            # 열쇠
            elif 97 <= code <= 122:
                if not keys[code - 97]:
                    keys[code - 97] = 1
                    for door in doors[code - 97]:
                        q.appendleft(door)

            # 문서
            elif ch == "$":
                answer += 1

            graph[nr][nc] = "*"
            q.append((nr, nc))

    print(answer)
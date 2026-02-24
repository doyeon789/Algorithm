from collections import deque

# =========================
# 계단 내려가기 시뮬레이션
# =========================
def simulate(arrival_times, stair_len):
    # 해당 계단을 이용하는 사람이 없으면 시간 0
    if not arrival_times:
        return 0

    # 도착 시간 기준 정렬
    arrival_times.sort()

    q = deque()   
    # 계단을 내려가고 있는 사람들의 종료 시간
    time = 0

    for arrive in arrival_times:
        # 도착 전에는 계단 이용 불가
        time = max(time, arrive)

        # 계단에 3명이 이미 있으면
        # 가장 빨리 끝나는 사람이 나갈 때까지 대기
        while len(q) == 3:
            time = max(time, q.popleft())

        # 계단 진입 -> stair_len분 후 종료
        q.append(time + stair_len)

    # 가장 늦게 끝난 사람이 전체 종료 시간
    return max(q)


# =========================
# DFS로 사람 배정
# =========================
def dfs(idx, stair0, stair1):
    global answer

    # 모든 사람을 계단에 배정한 경우
    if idx == P:
        time0 = simulate(stair0, stairs[0][2])
        time1 = simulate(stair1, stairs[1][2])
        answer = min(answer, max(time0, time1))
        return

    # idx번째 사람을 0번 계단에 배정
    dfs(
        idx + 1,
        stair0 + [dist[idx][0] + 1],  # 이동시간 + 1
        stair1
    )

    # idx번째 사람을 1번 계단에 배정
    dfs(
        idx + 1,
        stair0,
        stair1 + [dist[idx][1] + 1]   # 이동시간 + 1
    )

# 테스트 케이스 갯수 입력 받기
T = int(input())

# 테스트케이스 수 만큼 반복
for tc in range(1, T + 1):
    N = int(input())                                            # 그리드 사이즈 입력 받기
    grid = [list(map(int, input().split())) for _ in range(N)]  # 그리드 입력 받기

    people = [] # 사람 위치 저장
    stairs = [] # 계단 위치 및 길이 저장

    # 사람과 계단 위치 수집
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:                     # grid의 i,j값이 1 이면
                people.append((i, j))               # people 변수에 (i,j) 추가
            elif grid[i][j] > 1:                    # gird의 i,j값이 2 이상이면
                stairs.append((i, j, grid[i][j]))   # stair 변수에 (i,j,grid[i][j]) 추가 

    P = len(people) # 사람의 수를 구하는 변수

    # =========================
    # 사람 -> 계단 거리 계산
    # =========================
    dist = [[0] * 2 for _ in range(P)]  # (거리 변수) 변수사람의 수 만큼 (0,0) 배열 변수 만들어 놓기
    for i in range(P):
        for s in range(2):
            # dist 변수에 2개의 거리 추가하기
            dist[i][s] = abs(people[i][0] - stairs[s][0]) + abs(people[i][1] - stairs[s][1])

    answer = float('inf')

    # DFS 시작
    dfs(0, [], [])

    print(f"#{tc} {answer}")

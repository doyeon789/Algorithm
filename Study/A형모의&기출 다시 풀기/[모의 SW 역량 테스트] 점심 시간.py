def stair_time(arrival, stair_len):
    # 도착한 사람이 없다면 0 리턴
    if not arrival:
        return 0
    
    # 빨리 온 사람 순으로 정렬하기
    arrival.sort()
    finish = []

    for i in range(len(arrival)):
        # 도착 후 1분 뒤 시작
        start = arrival[i] + 1
        
        if i >= 3:
            # 3명 제한 때문에 대기해야 할 수도 있음
            start = max(start, finish[i-3])
        finish.append(start + stair_len)
    return max(finish)


def simulation(stair1_list, stair2_list):
    # 계단의 길이 저장하기
    stair1_len = matrix[stair[0][0]][stair[0][1]]
    stair2_len = matrix[stair[1][0]][stair[1][1]]
    
    t1 = stair_time(stair1_list[:], stair1_len)
    t2 = stair_time(stair2_list[:], stair2_len)
    
    return max(t1, t2)


# 사람들이 계단을 선택하는 모든 경우의 수 구하기 
def dfs(idx, stair1_list, stair2_list):
    global answer
    
    # 사람 분배가 끝나면 시뮬레이션 돌리기 =
    if idx == len(to_start1):
        time = simulation(stair1_list, stair2_list)
        answer = min(answer, time)
        return
    
    # 계단 1 선택
    dfs(idx+1, stair1_list + [to_start1[idx]], stair2_list)
    # 계단 2 선택
    dfs(idx+1, stair1_list, stair2_list + [to_start2[idx]])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 계단1,2 의 멘헤튼 거리를 저장할 변수
    to_start1 = []
    to_start2 = []

    # 계단 위치 저장하기
    stair = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 1:
                stair.append([i, j])

    # 맨해튼 거리 구하기 
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                to_start1.append(abs(i - stair[0][0]) + abs(j - stair[0][1]))
                to_start2.append(abs(i - stair[1][0]) + abs(j - stair[1][1]))

    answer = float('inf')

    dfs(0, [], [])

    print(f"#{tc} {answer}")
def select_A_food(arr, r):
    idx = list(range(r))
    
    result = []
    
    while True:
        # 현재 idx 상태에 해당하는 조합을 result에 저장
        result.append(tuple(arr[i] for i in idx))

        # 뒤에서부터 증가 가능한 인덱스를 찾는다
        for i in reversed(range(r)):
            # idx[i]가 가질 수 있는 최대값:
            # i + len(arr) - r
            # (조합이므로 뒤에 남을 공간을 고려해야 함)
            if idx[i] != i + len(arr) - r:
                break
        else:
            # 더 이상 만들 수 있는 조합이 없음
            return result

        # 증가 가능한 위치 idx[i]를 1 증가
        idx[i] += 1

        # 그 뒤의 인덱스들은 순차적으로 다시 맞춰준다
        for j in range(i + 1, r):
            idx[j] = idx[j - 1] + 1


def get_taste(food_num):
    taste = 0
    #
    for i in food_num:
        for j in food_num:
            if i != j:
                taste += food_synergy[i][j]
    return taste


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # NxN 시너지 표
    food_synergy = [list(map(int, input().split())) for _ in range(N)]
    
    # 재료 번호 리스트 (0 ~ N-1)
    food = list(range(N))
    
    # A 음식 후보들
    A_food = select_A_food(food, N//2)
    
    result = float('inf')
    for food_num in A_food:
        A_set = set(food_num) # A 집합으로 만들기
        B_set = set(food) - A_set # 차집합으로 A에서 사용안한 food B에 할당

        A_taste = get_taste(food_num)
        B_taste = get_taste(B_set)

        result = min(result, abs(A_taste - B_taste))

    print(f"#{tc} {result}")

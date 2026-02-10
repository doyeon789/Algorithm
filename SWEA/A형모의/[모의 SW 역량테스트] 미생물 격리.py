'''
1. nmk 주어짐. 약품이 칠해진 부분에는 미생물이 배치되지 않았다.
2. 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.
3. 미생물 군집이 약품 가면 int(x//2), 이동방향 반대
4. 합쳐지면 -> 미생물수 더하기, 이동방향은 더 큰거 방향, 

M 시간 격리됨. -> 미생물들의 총합을 구하여라
'''
def simulation(microbes):
    # 일단 M시간 만큼 시뮬 돌리기


    for _ in range(M):
        locations = {}
        for i,j,num,dir in microbes:
            ni = i + dx[dir-1]
            nj = j + dy[dir-1]
            
            #약품 처리된곳을 밟았을때
            if ni == 0 or nj == 0 or ni == N-1 or nj == N-1:
                num //= 2
                dir = reverse[dir-1] + 1
                if num == 0:
                    continue

            #미생물 위치값 갱신, 정보 저장
            if (ni, nj) not in locations:
                locations[(ni, nj)] = []
            locations[(ni, nj)].append((num, dir))

        # 합치기
        new_microbes = []
        for (x, y), group in locations.items():
            if len(group) == 1:
                num, dir = group[0]
                new_microbes.append([x, y, num, dir])
                continue

            total_count = 0
            max_count = -1
            selected_dir = 0 

            for num, dir in group:
                total_count += num

                if num > max_count:
                    max_count = num
                    selected_dir = dir
            new_microbes.append([x, y, total_count, selected_dir])

        microbes = new_microbes
    return microbes

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
reverse = [1, 0, 3, 2]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microorganisms = [list(map(int, input().split())) for _ in range(K)]
    result = simulation(microorganisms)
    answer = sum(m[2] for m in result)

    print(f"#{tc} {answer}")

'''
1
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
'''
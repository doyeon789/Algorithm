'''
1. nmk 주어짐. 약품이 칠해진 부분에는 미생물이 배치되지 않았다.
2. 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.
3. 미생물 군집이 약품 가면 int(x//2), 이동방향 반대
4. 합쳐지면 -> 미생물수 더하기, 이동방향은 더 큰거 방향, 

M 시간 격리됨. -> 미생물들의 총합을 구하여라
'''

def simulation(microbes):
    for _ in range(M):
        locations = {}
        
        # 미생물 위치 이동
        for x, y, cnt, d in microbes:
            nx = x + dx[d-1]
            ny = y + dy[d-1]

            #약 밟으면
            if nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
                cnt //= 2
                d = reverse[d-1] + 1
                if cnt == 0:
                    continue
            
            #미생물 위치값 갱신, 정보 저장
            if (nx, ny) not in locations:
                locations[(nx, ny)] = []
            locations[(nx, ny)].append((cnt, d))

        # 합치기
        microbes = []
        for (x, y), group in locations.items():
            if len(group) == 1:
                microbes.append([x, y, group[0][0], group[0][1]])
            else:
                total = sum(c for c, _ in group)
                _, direction = max(group)
                microbes.append([x, y, total, direction])
        
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
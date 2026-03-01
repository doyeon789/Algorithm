dx = [-1,1,0,0]
dy = [0,0,-1,1]
reverse = [1,0,3,2]

def simulation(micro):
    for _ in range(M):
        # 새로 갱신할 미생물 정보가 담길 변수
        locations = {}

        # 미생물 이동
        for i,j,cnt,dir in micro:
            ni = i + dx[dir-1]
            nj = j + dy[dir-1]

            # 약품 처리 된 곳 밟았을떄 
            if ni == 0 or nj == 0 or ni == N-1 or nj == N-1:
                cnt //= 2
                dir = reverse[dir-1] + 1
                if cnt == 0:
                    continue

            #미생물 위치값 갱신, 정보 저장
            if (ni, nj) not in locations:
                locations[(ni, nj)] = []
            locations[(ni, nj)].append((cnt, dir))
        
        # 미생물 합치기
        new_microbes = [] # 위치가 갱신된 미생물들에 대한 정보가 저장될 변수
        for (x, y), group in locations.items():
            # 한 좌표에 미생물의 수가 1개인경우 그냥 변수에 추가
            if len(group) == 1:
                cnt, dir = group[0]
                new_microbes.append([x, y, cnt, dir])
                continue
            
            # 한 좌표에 미생물이 2개 이상인 경우
            # 미생물 합치기

            total_cnt = 0
            max_cnt = -1
            selected_dir = 0 

            for cnt, dir in group:
                total_cnt += cnt

                if cnt > max_cnt:
                    max_cnt = cnt
                    selected_dir = dir
            new_microbes.append([x, y, total_cnt, selected_dir])
        micro = new_microbes
    return micro

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]

    # 시뮬레이션이 완료된 후 미생물들의 정보가 담긴 변수    
    result = simulation(micro)

    # 남은 미생물들의 군집중 그 수를 합쳐서 저장하는 변수
    answer = sum(m[2] for m in result)

    print(f"#{tc} {answer}")


"""
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
"""
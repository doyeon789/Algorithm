directions = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

def simulation(atom_list):
    result = 0
    
    while len(atom_list) >= 2:
        # 이동 
        for i in range(len(atom_list)) :
            atom_list[i][0] += directions[atom_list[i][2]][0]
            atom_list[i][1] += directions[atom_list[i][2]][1]
        
        # 위치 저장
        location = {}
        for a in atom_list:
            key = (a[0], a[1])
            if key in location:
                location[key].append(a)
            else:
                location[key] = [a]

        # 합치기
        atom_list = []
        for l in location :
            if len(location[l]) >= 2 :
                for score in location[l] :
                    result += score[3]
            else :
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000 :
                    atom_list.append(location[l][0])
    
    return result
        
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    atom_list = [list(map(int, input().split())) for _ in range(N)]

    
    print(f"#{tc} {simulation(atom_list)}")

"""
1
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
"""
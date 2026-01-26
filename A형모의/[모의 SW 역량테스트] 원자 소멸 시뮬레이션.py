T = int(input())

for tc in range(1, T + 1) :
    n = int(input())
    atom = [list(map(int, input().split())) for _ in range(n)]

    directions = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

    result = 0

    while len(atom) >= 2 :
        for i in range(len(atom)) :
            atom[i][0] += directions[atom[i][2]][0]
            atom[i][1] += directions[atom[i][2]][1]

        location = {}
        for a in atom:
            key = (a[0], a[1])
            if key in location:
                location[key].append(a)
            else:
                location[key] = [a]

        atom = []
        for l in location :
            if len(location[l]) >= 2 :
                for score in location[l] :
                    result += score[3]
            else :
                if -1000 <= location[l][0][0] <= 1000 and -1000 <= location[l][0][1] <= 1000 :
                    print(location[l][0][0], location[l][0][1])
                    atom.append(location[l][0])

    print(f"#{tc} {result}")

"""
1
4
-5 0 3 5
5 0 2 3
0 5 1 7
0 -5 0 9
"""

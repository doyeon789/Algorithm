from pprint import pprint

origin_matirx = [[1,2,3],[4,5,6],[7,8,9]]
print("== origin_matrix ==")
pprint(origin_matirx,width=30)
print()

# ==================================================== #

"""
전치(행과 열을 바꿈)
언패킹으로 각 리스트를 추출하고, zip으로 각 열끼리 묶어준다.
"""
reversed_matrix = list(map(list,zip(*origin_matirx)))
print("== reversed_matrix ==")
pprint(reversed_matrix,width=30)
print()

# ==================================================== #

""" _______________________________ 회전
90도 시계방향 회전 (행을 뒤집고 전치)
(i, j) => (n-1-j, i)
2. (n-1,j, i) => 행을 뒤집고
3. (j, n-1-i) => 전치
"""
rotate_90_clockwise_matrix = list(zip(*origin_matirx[::-1]))
print("== rotate_90_clockwise_matrix ==")
pprint(rotate_90_clockwise_matrix,width=30)
print()



# <오프라인 쿼리>
# 즉시 처리하지 않고, 미리 정장해 두었다가 특정 조건에 따라 일관적으로 처리하는 알고리즘 설계 기법이다.
# 이 방법은 데이터가 많고 쿼리가 많은 상황에서 효율적인 처리를 가능하게 한다.

# 특징 : 즉시 응답하지 않음. 쿼리를 입력받을때 바로 처리 하지 않고, 나중에 한 번에 처리
# 정렬 기반 최적화 가능 : 쿼리를 정렬하거나 특정 조건에 따라 순서르 조정하여 효율성을 높일수 있다.
# 시간 복잡도 최적화 - 적절한 데이터 구조와 알고리즘을 사용하면 쿼리의 총 실해 시간을 줄일수 있다.

# <[Mo's Algorithm]>
# 구간 퀄을 효율적으로 처리하는 오프랑니 알고리즘.
# 구간합, 구간 최대값/최소값, 특정범위에서의 빈도 계산 등의 문제에서 사용된다.

# <동작 방식>
# 1. 쿼리를 블록 단위로 정렬한다.
#   블록 번호(인덱스 // 블록 크기)
#   같은 블록 내에서는 오른 인덱스의 크기
# 2. 정렬된 순서대로 쿼리를 처리하며 필요한 값을 갱신.
#   이전 쿼리의 결과를 재 활용하여 계산 시간을 줄인다.
#   구간[l1,r1]에서 [l2,r2]로 이동 시, 기존 결과를 호라용하여 추가/제거 작업만 수행

"""
대표 문제 예시
배열 A가 주어 졌을때, Q개의 쿼리가 주어진다.
각 쿼리 [L,R]에 대해,
해당 구간에 등장하는 서로 다른 수의 개수를 출력해라
"""

from math import sqrt
from collections import defaultdict

class Query :
    def __init__(self, l, r ,idx):
        self.l = l
        self.r = r
        self.idx = idx

BLOCK = 0
def mo_cmp(a: Query):
    return(a.l // BLOCK, a.r)

def mos(arr, queries):
    global BLOCK
    BLOCK = int(sqrt(len(arr)))

    queries.sort(key=mo_cmp)
    answer = [0] * len(queries)
    freq = defaultdict(int)
    cnt = 0

    l, r = 0 , -1
    for q in queries:
        while r < q.r:
            r += 1
            freq[arr[r]] += 1
            if freq[arr[r]] == 1:
                cnt += 1
        while r > q.r:
            if freq[arr[r]] == 1:
                cnt -= 1
            freq[arr[r]] -= 1
            r -= 1
        while l < q.l:
            if freq[arr[l]] == 1:
                cnt -= 1
            freq[arr[l]] -= 1
            l += 1
        while l > q.l:
            l -= 1
            freq[arr[l]] += 1
            if freq[arr[l]] == 1:
                cnt += 1

        answer[q.idx] = cnt
    return answer

"""
쿼리 결과가 정렬되어 있지 않다  ->  Query에 인덱스를 저장해 정렬 복원
숫자가 너무 크다	          ->  좌표 압축 활용
값이 추가/제거될 때 복잡하다    ->	add() / remove() 함수 분리
R 우선 정렬이 더 빠를 때       ->  Z 모양 정렬 (Hilbert order) 사용
"""
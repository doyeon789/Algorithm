"""

def combinations(arr,r):
    idx = list(range(r))

    while True:
        for i in reversed(range(r)):
            if idx[i] != i + len(arr) - r:
                break
        else:
            return
        
        yield tuple(arr[i] for i in idx)

        for i in reversed(range(r)):
            if idx[i] != i + len(arr) - r:
 
                idx[i] += 1
                
                for j in range(i + 1, r):
                    idx[j] = idx[j - 1] + 1                    
                break
"""


def combinations(arr, r):
    n = len(arr)
    idx = list(range(r))

    while True:
        # 현재 조합 먼저 출력
        yield tuple(arr[i] for i in idx)

        # 뒤에서부터 증가 가능한 위치 찾기
        for i in reversed(range(r)):
            if idx[i] != i + n - r:
                break
        else:
            return  # 더 이상 만들 조합이 없음

        # 해당 위치 증가
        idx[i] += 1

        # 뒤쪽은 순차적으로 재정렬
        for j in range(i + 1, r):
            idx[j] = idx[j - 1] + 1

for i in combinations([1,2,3,4,5],3):
    print(i)


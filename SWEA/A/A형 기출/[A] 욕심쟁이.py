import sys
input = sys.stdin.readline

def simulate(start, gems):
    arr = gems[:]  # 보석 복사 (원본 보호)
    pos = start

    while True:
        left_dist = float('inf')
        right_dist = float('inf')
        left_idx = -1
        right_idx = -1

        # 왼쪽에서 가장 가까운 보석 찾기
        for i in range(pos - 1, -1, -1):
            if arr[i] == 1:
                left_dist = pos - i
                left_idx = i
                break

        # 오른쪽에서 가장 가까운 보석 찾기
        for i in range(pos + 1, len(arr)):
            if arr[i] == 1:
                right_dist = i - pos
                right_idx = i
                break

        # 더 이상 보석이 없으면 성공
        if left_dist == float('inf') and right_dist == float('inf'):
            return True

        # 거리가 같으면 폭발
        if left_dist == right_dist:
            return False

        # 더 가까운 쪽으로 이동
        if left_dist < right_dist:
            arr[left_idx] = 0
            pos = left_idx
        else:
            arr[right_idx] = 0
            pos = right_idx


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    gems = list(map(int, input().split()))

    M -= 1
    answer = 0

    for d in range(N):
        found = False

        # 왼쪽 후보
        left = M - d
        if 0 <= left < N:
            if simulate(left, gems):
                answer = d
                found = True

        # 오른쪽 후보 (d=0이면 중복이므로 제외)
        if not found and d != 0:
            right = M + d
            if 0 <= right < N:
                if simulate(right, gems):
                    answer = d
                    found = True

        if found:
            break

    print(f"#{tc} {answer}")

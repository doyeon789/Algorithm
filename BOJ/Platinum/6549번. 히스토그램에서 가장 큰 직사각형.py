while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break

    n = arr[0]
    histogram = arr[1:]
    stack = []
    max_area = 0

    for i in range(n):
        while stack and histogram[stack[-1]] > histogram[i]:
            height = histogram[stack.pop()]
            
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    while stack:
        height = histogram[stack.pop()]
        
        if not stack:
            width = n
        else:
            width = n - stack[-1] -1
        max_area = max(max_area, height * width)

    print(max_area)

# stack 높이가 증가하는 인덱스만 저장 (1,4,5 ...)
# 낮은 막대가 나오면
# 이전 막대들의 최대 직사각형을 계산하는 구조
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1

min_value = float('inf')
answer = (0, 0)

while left < right:
    total = arr[left] + arr[right]
    
    if abs(total) < min_value:
        min_value = abs(total)
        answer = (arr[left], arr[right])
    
    if total > 0:
        right -= 1
    else:
        left += 1

print(*answer)
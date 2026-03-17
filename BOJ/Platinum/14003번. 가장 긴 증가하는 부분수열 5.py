from collections import deque
import sys
input = sys.stdin.readline

def binarySearch(lst, length, target):
    start = 0 
    end = length - 1
    result = length

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] >= target:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result

n = int(input())
arr = list(map(int,input().split()))

lst = [0]*n
idx_arr = [-1]*n

lst[0] = arr[0]
idx_arr[0] = 0

lenght = 1
for i in range(1, n):
    if lst[lenght-1] < arr[i]:
        idx_arr[i] = lenght
        lst[lenght] = arr[i]
        lenght += 1
    else:
        index = binarySearch(lst, lenght, arr[i])
        idx_arr[i] = index
        lst[index] = arr[i]

print(lenght)

stack = deque()
temp = lenght - 1
for i in range(n-1,-1,-1):
    if idx_arr[i] == temp:
        stack.append(arr[i])
        temp -= 1

result = []
while stack:
    result.append(stack.pop())

print(*result)
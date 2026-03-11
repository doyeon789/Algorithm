import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]

for arg in arr:
    if LIS[-1] < arg:
        LIS.append(arg)
    else:
        start = 0
        end = len(LIS)-1
        while start <= end:
            mid = (start+end)//2

            if LIS[mid] < arg:
                start = mid + 1
            else:
                end = mid - 1
            
        LIS[start] = arg

print(len(LIS))
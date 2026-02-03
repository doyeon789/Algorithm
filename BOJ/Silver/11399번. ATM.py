N = int(input())
wait = list(map(int, input().split()))
wait.sort()
sum_arr = []
temp = 0

for i in wait:
    temp += i
    sum_arr.append(temp)
print(sum(sum_arr))

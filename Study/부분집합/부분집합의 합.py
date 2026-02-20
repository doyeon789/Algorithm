def sum_subset(depth, num_sum):
    if depth == N:
        if num_sum == 10:
            result += 1
        return
    
    if num_sum >= 10:
        return

    sum_subset(depth+1, num_sum+arr[depth])

    sum_subset(depth+1, num_sum)

N = 10
arr = [1,2,3,4,5,6,7,8,9,10]
result = 0
sum_subset(0,0)

print(result)
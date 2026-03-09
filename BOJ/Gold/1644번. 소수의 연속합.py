prime_num_list = []

check = [0]*4000001
check[0:2] = [1,1]

for i in range(2, int(4000000**0.5)+1):
    if check[i] == 0:
        for j in range(i*2, 4000001, i):
            check[j] = 1

prime_num_list = [idx for idx, val in enumerate(check) if val == 0]

N = int(input())

left = 0
right = 0
sum_num = 0
cnt = 0

while True:

    if sum_num >= N:
        if sum_num == N:
            cnt += 1
        sum_num -= prime_num_list[left]
        left += 1

    else:
        if right == len(prime_num_list):
            break
        sum_num += prime_num_list[right]
        right += 1

print(cnt)
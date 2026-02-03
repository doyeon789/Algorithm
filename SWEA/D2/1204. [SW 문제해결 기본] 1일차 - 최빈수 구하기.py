T = int(input())

for tc in range(1, T + 1):
    tc_num = int(input())
    num_list = list(map(int, input().split()))
    num_check = [0] * 101
    max_count = 0
    max_index = 0 

    for num in num_list:
        num_check[num] += 1

    max_count = max(num_check)

    for b in range(101):
        if num_check[b] == max_count:
            if b > max_index: 
                max_index = b

    print(f"#{tc} {max_index}")

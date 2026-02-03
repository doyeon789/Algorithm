from pprint import pprint

T = int(input())

for test_case in range(1, T + 1):    
    N = int(input())                               
    box_list = list(map(int, input().split()))

    drop_list = [0] * N 

    for i in range(N) :
        for j in range(i+1, N) :
            if box_list[i] > box_list[j] :
                drop_list[i] += 1          
    
    max_drop = drop_list[0]
    for drop in drop_list :
        if max_drop < drop :
            max_drop = drop
 
    print(f'#{test_case} {max_drop}')

N = int(input())

for i in range(1, N + 1):
    cnt = 0
    for c in str(i):
        if c in '369':
            cnt += 1
    
    if cnt > 0:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')

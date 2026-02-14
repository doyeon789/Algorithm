n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
f.sort()

i = 0
result = 0
latest_end = (3, 1) 

while i < n:
    sm, sd, em, ed = f[i]
    if (sm, sd) <= latest_end < (em, ed):
        max_end = (em, ed)
        while i < n-1: 
            nsm, nsd, nem, ned = f[i+1]
            if latest_end < (nsm, nsd):
                break
            if max_end < (nem, ned):
                max_end = (nem, ned)
            i += 1
            
        result += 1
        latest_end = max_end
        
        if (11, 30) < latest_end:
            print(result)
            exit(0)
    i += 1

print(0)

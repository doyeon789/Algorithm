testcase = int(input())
for t in range(1,testcase+1):
    inequality_sign = '='
    a,b = map(int,input().split())
    if a>b:
        inequality_sign = '>'
    elif a<b:
        inequality_sign = '<'
    else:
        inequality_sign = '='
    print(f"#{t} {inequality_sign}")
    

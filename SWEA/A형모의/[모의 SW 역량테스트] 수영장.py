# 월        : 1 2 3 4 5 6 7 8 9 10 11 12
# 이용 계획  : 0 0 2 9 1 5 0 0 0  0  0  0
'''
10 40 100 300   
0 0 2 9 1 5 0 0 0 0 0 0
'''

month_money = list(map(int, input().split()))
days = list(map(int, input().split()))

money = []
def dfs(now_month, cost):
    #print(f"month:{now_month} cost:{cost}")
    if now_month == 12:
        money.append(cost)
        return
    
    for price in range(3):
        #print(f"month:{now_month} cost:{cost+month_money[price]}")
        dfs(now_month+1,cost+month_money[price])
    print()


dfs(1,0)
print(min(money))
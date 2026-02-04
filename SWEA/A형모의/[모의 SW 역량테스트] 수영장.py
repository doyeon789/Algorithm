
def dfs(month, cost):
    global answer

    if cost >= answer:
        return

    if month >= 12:
        answer = min(answer, cost)
        return

    if days[month] == 0:
        dfs(month + 1, cost)
    else:
        dfs(month + 1, cost + days[month] * month_money[0])
        dfs(month + 1, cost + month_money[1])
        dfs(month + 3, cost + month_money[2])

T = int(input())
for tc in range(1,T+1):
    month_money = list(map(int, input().split()))
    days = list(map(int, input().split()))

    answer = month_money[3]

    dfs(0, 0)
    print(f"#{tc} {answer}")
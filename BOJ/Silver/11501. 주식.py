T = int(input())

for t in range(T):

    N = int(input())
    price = list(map(int, input().split()))

    money = 0

    maxPrice = 0
    for i in range(len(price)-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
        else:
            money += maxPrice - price[i]

    print(money)

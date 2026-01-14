n = int(input())
flower = []
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, input().split())
    flower.append([start_m * 100 + start_d, end_m * 100 + end_d])

end_date = 301
count = 0

while (flower):
    if (end_date >= 1201 or flower[0][0] > end_date):
        break

    temp_end_date = -1

    for _ in range(len(flower)):
        if (flower[0][0] <= end_date):
            if (temp_end_date <= flower[0][1]):
                temp_end_date = flower[0][1]
            flower.remove(flower[0])
        else:
            break

    end_date = temp_end_date
    count += 1
if end_date < 1201:
    print(0)
else:
    print(count)
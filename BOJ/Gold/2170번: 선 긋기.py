n = int(input())
coordinate = []
for i in range(n):
    coordinate.append(list(map(int, input().split())))

coordinate.sort()
merged_length = 0
start, end = coordinate[0]

for i in range(1, n):
    if coordinate[i][0] <= end:
        end = max(end, coordinate[i][1])
    else:
        merged_length += end - start
        start, end = coordinate[i]
merged_length += end - start

print(merged_length)

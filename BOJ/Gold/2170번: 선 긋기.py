n = int(input())

lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])
lines.sort(key=lambda x : x[0])

start, end = lines[0][0], lines[0][1]
answer = 0
for i in range(1, n):
    if lines[i][0] <= end and lines[i][1] <= end:
        continue
    elif lines[i][0] <= end and lines[i][1] > end:
        end = lines[i][1]
    else:
        answer += end - start
        start = lines[i][0]
        end = lines[i][1]
answer += end-start
print(answer)

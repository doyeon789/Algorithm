n = int(input())

coordinate=[]

for i in range(n):
    coordinate.append(list(map(int, input().split())))

paper = [0]*max(max(row) for row in coordinate)

for i in range(n):
    for j in range(coordinate[i][0],coordinate[i][1]):
        paper[j-1] = 1
print(sum(paper))

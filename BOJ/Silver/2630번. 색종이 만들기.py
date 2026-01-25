n = int(input())
colors = [list(map(int,input().split())) for _ in range(n)]

white = 0
blue = 0

def divid(x, y, size):
    global white, blue

    first = colors[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if colors[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        if first == 0:
            white += 1
        else:
            blue += 1
        return

    half = size // 2
    divid(x, y, half)
    divid(x, y + half, half)
    divid(x + half, y, half)
    divid(x + half, y + half, half)


divid(0,0,n)

print(white)
print(blue)

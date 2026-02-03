Test_case = int(input())

for tc in range(1, Test_case + 1):
    area = [[0]*10 for _ in range(10)]
    count = 0
    N = int(input())

    for _ in range(N):
        row1, col1, row2, col2, color = map(int, input().split())

        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                if area[row][col] == 0:
                    area[row][col] = color
                elif area[row][col] + color == 3:
                    area[row][col] = 3
                    count += 1

    print(f"#{tc} {count}")

testcase = int(input())

for tc in range(1,testcase+1):
    numbers = list(map(int,input().split()))
    print(f"#{tc} {round((sum(numbers) - max(numbers) - min(numbers))/(len(numbers)-2))}")

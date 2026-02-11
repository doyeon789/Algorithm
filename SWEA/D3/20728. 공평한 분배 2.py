# 사탕이 담긴 N개의 주머니가 있다. 이 중 i (1≤i≤N) 번째 주머니에는 사탕이 ai개 들어 있다. 
# 당신은 이 주머니 중 정확히 K개를 선택하여 어린이들에게 나누어 주려고 한다.
# 공정성을 위해, 당신은 나눠 준 주머니 가운데 사탕의 개수가 가장 많은 것과 가장 적은 것의 사탕 개수 차이를 최소화하려고 한다.
# 모든 유효한 방법 중 차이의 최솟값을 구하는 프로그램을 작성하라.

T = int(input())
for tc in range(1,T+1):
    # 주머니의 개수, 나눠 줄 주머니의 개수
    N, K = map(int,input().split())
    candies = list(map(int,input().split()))

    candies.sort(reverse=True)
    answer = float('inf')
    for i in range(N-(K-1)):
        temp = []
        for j in range(i,K+i):
            temp.append(candies[j])
        answer = min(answer,temp[0]-temp[-1])

    print(f"#{tc} {answer}")
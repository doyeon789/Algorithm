for test_case in range(1,10+1):
    N = int(input())
    buildings = list(map(int,input().split()))
 
    total = 0  
 
    for i in range(2, N-2): 
        if (buildings[i] >= buildings[i-1] and 
                buildings[i] >= buildings[i-2] and 
                buildings[i] >= buildings[i+1] and 
                buildings[i] >= buildings[i+2]):
 
                left = buildings[i-2] if buildings[i-2] > buildings[i-1] else buildings[i-1]
                right = buildings[i+2] if buildings[i+2] > buildings[i+1] else buildings[i+1]
 
                if left > right:
                        total += (buildings[i] - left)
                else:
                        total += (buildings[i] - right)
    print("#" + str(test_case) + " " + str(total))

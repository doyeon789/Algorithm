for tc in range(1,10+1):
    ans = 0
    num = int(input())
    find_str = input()
    string = input()
    ans = string.count(find_str)
    
    print(f"#{tc} {ans}")

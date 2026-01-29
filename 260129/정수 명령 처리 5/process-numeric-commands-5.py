N = int(input())  # 입력된 명령의 개수

# 동적 배열을 관리할 리스트
arr = []

# 각 명령을 처리
for _ in range(N):
    command = input().split()
    
    if command[0] == "push_back":
        arr.append(int(command[1]))
    elif command[0] == "pop_back":
        if arr:
            arr.pop()
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "get":
        k = int(command[1]) - 1
        if 0 <= k < len(arr):
            print(arr[k])
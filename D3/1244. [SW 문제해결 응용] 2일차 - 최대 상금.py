def dfs(depth, nums):
    global result
    
    key = (depth, ''.join(nums))
    if key in visited:
        return
    visited.add(key)
    
    if depth == K:
        result = max(result, int(''.join(N)))
        return
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            dfs(depth + 1, nums)
            nums[i], nums[j] = nums[j], nums[i]

testcase = int(input())

for tc in range(1, testcase + 1):
    N , K = map(int, input().split())
    N = list(str(N))
    
    result = 0 
    visited = set() 
    dfs(0, N) 
    print(f"#{tc} {result}")

n = int(input())
nums = [int(input()) for _ in range(n)]
result = 0

for i in range(n-1, 0, -1):
  if nums[i] <= nums[i-1]:
    result += nums[i-1] - nums[i] + 1
    nums[i-1] = nums[i] - 1
print(result)

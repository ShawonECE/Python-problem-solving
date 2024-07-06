def findMaxK(nums):
    memo = {}
    max = -1
    for num in nums:
        if memo.get(num):
            memo[num] = memo[num] + 1
        else:
            memo[num] = 1
            
    for key in memo:
        if key > max and memo.get(-key):
            max = key
    return max

nums = [-1,10,6,7,-7,1]
print(findMaxK(nums))
def divideArray(nums):
    length = len(nums)
    if length % 2 != 0:
        return False
    memo = {}
    for num in nums:
        if memo.get(num):
            memo[num] += 1
        else:
            memo[num] = 1
            
    values = memo.values()
    
    for value in values:
        if value % 2 != 0:
            return False
    return True

nums = [1,2,3,4]
print(divideArray(nums))
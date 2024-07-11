def missingNumber(nums):
    n = len(nums)
    actualSum = (n*(n+1)) // 2
    presentSum = sum(nums)
    return actualSum - presentSum

nums = [0,1]
print(missingNumber(nums))
    
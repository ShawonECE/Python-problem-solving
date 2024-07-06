def sumOfUnique(nums):
    memo = {}
    sum = 0
    
    for num in nums:
        if memo.get(num):
            memo[num] = memo[num] + 1
        else:
            memo[num] = 1
    
    for key in memo:
        if memo[key] == 1:
            sum = sum + key
    return sum

nums = [1,2,3,4,5]
print(sumOfUnique(nums))
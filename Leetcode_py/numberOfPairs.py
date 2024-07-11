def numberOfPairs(nums):
    memo = {}
    length = len(nums)
    pair = 0
    for num in nums:
        if memo.get(num):
            memo[num] += 1
            if memo[num] == 2:
                pair += 1
                memo[num] -= 2
        else:
            memo[num] = 1
    return [pair, length - 2 * pair]

nums = [0]
print(numberOfPairs(nums))
def countKDifference(nums, k):
    count = 0
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] - nums[j] == k or nums[i] - nums[j] == -k:
                count += 1
    return count

nums = [3,2,1,5,4]
k = 2
print(countKDifference(nums, k))
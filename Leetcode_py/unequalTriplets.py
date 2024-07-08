def unequalTriplets(nums):
    length = len(nums)
    count = 0
    for i in range(length):
        for j in range(i + 1, length):
            if nums[j] != nums[i]:
                for k in range(j + 1, length):
                    if nums[k] != nums[i] and nums[k] != nums[j]:
                        count += 1
    return count

nums = [1,1,1,1,1]
print(unequalTriplets(nums))
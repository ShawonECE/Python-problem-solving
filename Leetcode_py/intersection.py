# def intersection(nums):
#     length = len(nums)
#     memo = {}
#     intersectionArr = []
    
#     for arr in nums:
#         for num in arr:
#             if memo.get(num):
#                 memo[num] += 1
#             else:
#                 memo[num] = 1
    
#     keys = memo.keys()
#     for key in keys:
#         if memo[key] == length:
#             intersectionArr.append(key)
            
#     intersectionArr.sort()
    
#     return intersectionArr

# using set
def intersection(nums):
    length = len(nums)
    
    if length == 1:
        nums[0].sort()
        return nums[0]
    
    intersect = set(nums[0])
    
    for arr in nums:
        intersect = intersect & set(arr)
    
    intersectArr = list(intersect)
    intersectArr.sort()
    return intersectArr
            
nums = [[44,21,48]]
print(intersection(nums))
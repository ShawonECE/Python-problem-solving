def findFinalValue(nums, original):
    numsSet = set(nums)
    while original in numsSet:
        original = original * 2
    return original

#using dictionary

# def findFinalValue(nums, original):
#     memo = {}
#     for num in nums:
#         if memo.get(num):
#             memo[num] += 1
#         else:
#             memo[num] = 1
            
#     while memo.get(original):
#         original = original * 2
        
#     return original

nums = [5,3,6,1,12]
original = 3
print(findFinalValue(nums, original))
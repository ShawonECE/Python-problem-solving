def findIntersectionValues(nums1, nums2):
    answer1 = 0
    answer2 = 0
    for element in nums1:
        if element in nums2:
            answer1 += 1
    for element in nums2:
        if element in nums1:
            answer2 += 1
    return [answer1, answer2]

nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
print(findIntersectionValues(nums1, nums2))
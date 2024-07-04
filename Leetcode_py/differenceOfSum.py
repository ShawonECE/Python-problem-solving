def digitSum(num: int) -> int:
    # num will be up to 2000
    sum = 0
    if num > 999:
        sum = num // 1000 + digitSum(num % 1000)
    elif num >= 100:
        sum = num // 100 + digitSum(num % 100)
    elif num >= 10:
        sum = num // 10 + num % 10
    else:
        return num
    return sum

def differenceOfSum(nums):
    digSum = 0
    elementSum = 0
    for num in nums:
        digSum = digSum + digitSum(num)
        elementSum = elementSum + num
    return abs(digSum - elementSum)

nums = [1,2,3,4]
print(differenceOfSum(nums))
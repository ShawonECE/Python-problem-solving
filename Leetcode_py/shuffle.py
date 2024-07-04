def shuffle(nums, n):
    x = 0
    y = n
    shuffled = []
    while y < 2*n:
        shuffled.append(nums[x])
        shuffled.append(nums[y])
        x+=1
        y+=1
    return shuffled

nums = [1,1]
n = 1

print(shuffle(nums, n))
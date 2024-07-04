def sumOddLengthSubarrays(arr):
    sum = 0
    length = len(arr)
        
    for i in range(length):
        start = length - i
        end = i + 1
        apps = start * end
        oddApps = apps / 2 if apps % 2 == 0 else (apps + 1) / 2 
        sum = sum + arr[i] * oddApps
        
    return int(sum)

arr = [10,11,12]
print(sumOddLengthSubarrays(arr))
        
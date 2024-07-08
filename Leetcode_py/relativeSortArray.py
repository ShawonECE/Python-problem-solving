def relativeSortArray(arr1, arr2):
    memo = {}
    output = []
    for num in arr1:
        if memo.get(num):
            memo[num] += 1
        else:
            memo[num] = 1
    
    for num in arr2:
        occurrences = memo[num]
        for i in range(occurrences):
            output.append(num)
        memo.pop(num)
        
    remaining = list(memo.keys())
    remaining.sort()
    
    for num in remaining:
        occurrences = memo[num]
        for i in range(occurrences):
            output.append(num)
    
    return output

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2))
def uniqueOccurrences(arr):
    memo = {}
    
    for num in arr:
        if memo.get(num):
            memo[num] = memo[num] + 1
        else:
            memo[num] = 1
            
    occurrences = set(memo.values())
    
    if len(occurrences) == len(memo.values()):
        return True
    else:
        return False

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))
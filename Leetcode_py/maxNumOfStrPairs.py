def maximumNumberOfStringPairs(words):
    length = len(words)
    count = 0
    memo = {}
    for i in range(length):
        reversed = words[i][1] + words[i][0]
        
        if memo.get(words[i]) == 1:
            count += 1
        else:
            memo[reversed] = 1
            
    return count

words = ["aa","ab"]
print(maximumNumberOfStringPairs(words))
def areOccurrencesEqual(s):
    memo = {}
    for char in s:
        if memo.get(char):
            memo[char] = memo[char] + 1
        else:
            memo[char] = 1
    if len(set(memo.values())) == 1:
        return True
    else:
        return False
    
s = "aaabb"
print(areOccurrencesEqual(s))
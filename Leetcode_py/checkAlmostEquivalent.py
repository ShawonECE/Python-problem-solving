def checkAlmostEquivalent(word1, word2):
    length = len(word1)
    memo1 = {}
    memo2 = {}
    for i in range(length):
        if memo1.get(word1[i]):
            memo1[word1[i]] += 1
        else:
            memo1[word1[i]] = 1
            
        if memo2.get(word2[i]):
            memo2[word2[i]] += 1
        else:
            memo2[word2[i]] = 1
    
    keys1 = memo1.keys()
    keys2 = memo2.keys()
    
    for key in keys1:
        diff = memo1[key]
        if memo2.get(key):
            diff = memo1[key] - memo2[key]
        if diff > 3 or diff < -3:
            return False
        
    for key in keys2:
        diff = memo2[key]
        if memo1.get(key):
            diff = memo1[key] - memo2[key]
        if diff > 3 or diff < -3:
            return False
    
    return True

word1 = "cccddabba"
word2 = "babababab"

print(checkAlmostEquivalent(word1, word2))
def findWords(words):
    table = {
        'q' : 1,
        'w' : 1,
        'e' : 1,
        'r' : 1,
        't' : 1,
        'y' : 1,
        'u' : 1,
        'i' : 1,
        'o' : 1,
        'p' : 1,
        'a' : 2,
        's' : 2,
        'd' : 2,
        'f' : 2,
        'g' : 2,
        'h' : 2,
        'j' : 2,
        'k' : 2,
        'l' : 2,
        'z' : 3,
        'x' : 3,
        'c' : 3,
        'v' : 3,
        'b' : 3,
        'n' : 3,
        'm' : 3,
    }
    result = []
    for word in words:
        current = table[word[0].lower()]
        wordLength = len(word)
        for i in range(wordLength):
            row = table[word[i].lower()]
            
            if row != current:
                break
            if i == wordLength - 1:
                result.append(word)
                
    return result


words = ["a","d"]
print(findWords(words))
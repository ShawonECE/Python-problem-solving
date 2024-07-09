def clearDigits(s):
    positionsToBeDeleted = set()
    length = len(s)
    result = ''
    for i in range(length):
        if s[i].isdigit():
            positionsToBeDeleted.add(i)
            if i != 0:
                for j in range(i - 1, -1, -1):
                    if j not in positionsToBeDeleted and not s[j].isdigit():
                        positionsToBeDeleted.add(j)
                        break
    
    for i in range(length):
        if i not in positionsToBeDeleted:
            result = result + s[i]
    
    return result

s = "1cb34x"
print(clearDigits(s))
                    
def frequency(str):
    memo = {}
    for char in str:
        if memo.get(char):
            memo[char] += 1
        else:
            memo[char] = 1
    
    return memo
    

def groupAnagrams(strs):
    memo = {}
    record = set()
    result = []
    length = len(strs)
    for str in strs:
        memo[str] = frequency(str)
        
    for i in range(length):
        arr = []
        
        if strs[i] in record:
            continue
        
        arr.append(strs[i])
        record.add(strs[i])
        for j in range(i + 1, length):
            if memo[strs[i]] == memo[strs[j]]:
                arr.append(strs[j])
                record.add(strs[j])
        
        result.append(arr)
        
    return result

strs = ["a"]
print(groupAnagrams(strs))
        
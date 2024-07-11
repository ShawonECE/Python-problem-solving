def repeatedCharacter(s):
    memo = {}
    for char in s:
        if memo.get(char):
            memo[char] += 1
            if memo[char] == 2:
                return char
        else:
            memo[char] = 1
            
s = "abcdd"
print(repeatedCharacter(s))
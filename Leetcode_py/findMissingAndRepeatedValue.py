def findMissingAndRepeatedValues(grid):
    n = len(grid)
    memo = {}
    actualSum = (n**4 + n**2) // 2
    presentSum = 0
    repeated = 0
    for row in grid:
        for num in row:
            presentSum += num
            if memo.get(num):
                memo[num] += 1
                if memo[num] == 2:
                    repeated = num
            else:
                memo[num] = 1
    return [repeated, actualSum - presentSum + repeated]


grid = [[1,3],[2,2]]
print(findMissingAndRepeatedValues(grid))
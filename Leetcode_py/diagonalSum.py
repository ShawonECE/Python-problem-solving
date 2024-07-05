def diagonalSum(mat):
    size = len(mat)
    sum = 0
    for i in range(size):
        sum = sum + mat[i][i] + mat[i][size - 1 - i]
    if size % 2 != 0:
        mid = int(( size + 1 ) / 2)
        sum = sum - mat[mid - 1][mid - 1]
    return sum

mat = [[5]]
print(diagonalSum(mat))
def oddCells(m, n, indices):
    mat = []
    emptyRow = []
    odd = 0
    for i in range(n):
        emptyRow.append(0)
    for i in range(m):
        mat.append(emptyRow[:])
    
    for index in indices:
        row = index[0]
        col = index[1]
        for i in range(n):
            mat[row][i] = mat[row][i] + 1
        
        for j in range(m):
            mat[j][col] = mat[j][col] + 1

    for r in mat:
        for element in r:
            if element % 2 != 0:
                odd += 1
    return odd
                
    
m = 2
n = 3
indices = [[0,1],[1,1]]
print(oddCells(m, n, indices))
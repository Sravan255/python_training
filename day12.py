# matrix
matrix = [ [1,2,3],[4,5,6],[7,8,9]]
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c] , end=' ')
    print()
    
#colwise : if shuoldbe squre matrix
for c in range(len(matrix[0])):
    for r in range(len(matrix)):
        print(matrix[r][c], end=' ')
    print()
matrix1 = [[5, 2],
          [4, 9]] 
matrix2 = [[8, 3],
          [9, 4]]  
result = [[0,0],
         [0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
for r in result:
    print(r) 
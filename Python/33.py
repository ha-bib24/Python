'''matrix = [
    [1, 2, 3],
    [3, 4, 5],
]
#matrix[0][2] = 20
#print(matrix[0][2])

for row in matrix:
    for col in row:
        print(col)


#Matrix korte hle obossoi  numpy import korte hbe
#kicho example ................

# matrix toiri kori numpy diyea............
#1......
import numpy as np
#matrix = np.array([[1, 2], [3, 4]])
#print(matrix)


#2. problem.........
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(matrix)'''


#matrix add and sub.........
import numpy as np
matrix = np.array([[1, 2], [3, 4]])
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5 ,6], [7, 8]])
add = matrix1 + matrix2
sub = matrix1 - matrix2
multi = np.dot(matrix1, matrix2)
#matrix ultano............
invers = np.linalg.inv(matrix)
#determinant matrix...............
deter = np.linalg.det(matrix)
print(add)
print(sub)
print(multi)
print(invers)
print(deter)

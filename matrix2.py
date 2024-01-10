def minit(rows, cols, val=0, inc=0):
    return [[val + inc * (j + cols * i) for j in range(cols)] for i in range(rows)]

def mprint(mat):
    for row in mat:
        print(" ".join(map(str, row)))

def madd(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None

    result = []
    for i in range(len(mat1)):
        result.append([mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))])

    return result

# Example usage:
# Creating matrices
matrix1 = minit(2, 3, val=1, inc=1)
matrix2 = minit(2, 3, val=2, inc=2)

# Printing matrices
print("Matrix 1:")
mprint(matrix1)

print("\nMatrix 2:")
mprint(matrix2)

# Adding matrices
result_matrix = madd(matrix1, matrix2)

print("\nResultant Matrix after addition:")
if result_matrix:
    mprint(result_matrix)

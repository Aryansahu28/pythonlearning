class Matrix:
    def __init__(self, rows, cols, val=0, inc=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[val + inc * (j + cols * i) for j in range(cols)] for i in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

def mprint(mat):
    if not isinstance(mat, Matrix):
        print("Input is not a valid matrix.")
        return
    print(mat)

def madd(mat1, mat2):
    if not isinstance(mat1, Matrix) or not isinstance(mat2, Matrix):
        print("Input is not valid matrices.")
        return

    if mat1.rows != mat2.rows or mat1.cols != mat2.cols:
        print("Matrices must have the same dimensions for addition.")
        return

    result = Matrix(mat1.rows, mat1.cols)
    result.matrix = [[mat1.matrix[i][j] + mat2.matrix[i][j] for j in range(mat1.cols)] for i in range(mat1.rows)]
    return result

# Example usage:
# Creating matrices
matrix1 = Matrix(2, 3, val=1, inc=1)
matrix2 = Matrix(2, 3, val=2, inc=2)

# Printing matrices
print("Matrix 1:")
mprint(matrix1)

print("\nMatrix 2:")
mprint(matrix2)

# Adding matrices
result_matrix = madd(matrix1, matrix2)

print("\nResultant Matrix after addition:")
mprint(result_matrix)

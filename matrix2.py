def minit(rows,cols,val=0,inc=0):
    m=[]
    for i in range(rows):
        for j in range(cols):
            m[i][j] = val
            val = val + val*inc
    return m

def mprint(mat):
    global rows
    global cols
    for i in range(rows):
        for j in range(cols):
            print(mat[i][j],end="")
        print("")

matrix1 = minit(2,3,val=1,inc=1)
mprint(matrix1)
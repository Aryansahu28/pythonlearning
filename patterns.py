n =5
for row in range(n):
    for col in range(n):
        print("* ",end="")
    print("")


for row in range(n):
    for col in range(row+1):
        print("* ",end=" ")
    print("")
print("")
for row in range(n):
    for col in range(n-row):
        print("* ",end="")
    print("")
    
print("")

for row in range(5):
    for col in range(1,row+1):
        print(f"{col} ",end="")
    print("")

print("")

for row in range(2*n):
    if row>n:
        col = 2*n-row

    else:
        col = row
    for col1 in range(col):
        print("* ",end="")

    print("")

print("")

for row in range(2*n):
    if row > n:
        col=2*n-row
    else:
        col = row
    for i in range(n-col):
        print(" ",end="")
    for col1 in range(col):
        print("* ",end="")
    print("")

print("")

for row in range(1,n+1):
    for space in range(n-row):
        print(" ",end="")

    for col in range(row,0,-1):
        print(f"{col}",end="")

    for col in range(2,row+1):
        print(f"{col}",end="")
    
    print("")

print("")
    
for row in range(1,2*n+1):
    if row>n:
        col = 2*n-row
    else:
        col = row
    
    for space in range(n-col):
        print(" ",end="")
    for col1 in range(col,0,-1):
        print(f"{col1}",end="")
    for col1 in range(2,col+1):
        print(f"{col1}",end="")
    print("")
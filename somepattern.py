n = 3
k = 6
for row in range(n+1):
    for col in range(k+1):
        if row==0 or row==n:
            print("*",end="")
        elif col==1 or col==k:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
        
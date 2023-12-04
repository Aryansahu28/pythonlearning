for row in range(5):
    x = 65
    for col in range(4-row):
        print(chr(x),end="")
        x = x+1
    print("")


for row in range(5):
    
    for col in range(1,5):
        print(f"{col} ",end="")
    for col in range(4,0,-1):
        print(f"{col} ",end="")
    print("")
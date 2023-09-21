n = int(input("Enter the number to find the factorial\n"))

if n==0 or n==1:
    print(1)

else:
    s = 1
    for i in range(1,n+1):
        s = s*i

    print(s)
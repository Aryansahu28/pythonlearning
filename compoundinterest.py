print("Today, here we are going to calculate the compound interest of the input values\n")
p = int(input("Enter the principal value \n"))
r = int(input("Enter the rate of interest in %\n"))
n = int(input("Enter the number of times the interest is compounded per year\n"))
t = int(input("Enter the number of year\n"))

A = float(p*((1+(r/n))**(n*t)))

print("The compound of",n,"years is ",A)

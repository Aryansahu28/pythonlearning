A = float(input("Enter A:"))
B = float(input("Enter B:"))
C = float(input("Enter C:"))

if A > B and A > C:
    print("A is greater")


elif B > A and B > C:
    print("B is greater")


elif C > B and A < C:
    print("C is greater")

else:
    print("A,B and C are equal")

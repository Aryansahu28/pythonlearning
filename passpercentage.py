print("Calculating passing percentage of class\n")
P = 0  #Passing students initially
i = 0 #index
#Input for numbers of students
n = int(input("Enter the number of student\n"))
while(i<n):
    m = int(input("Enter the marks of student\n"))
    if(m>=40):
        P=P+1
   
    i = i+1

#Percentage of passing students in the class
print(P)
Pass_students = P*100/n

print(Pass_students)
from datetime import datetime
curr_year = datetime.today().year
print("Determine the age of the person")
name = input("Enter your name :\n")
Year_of_birth = int(input("Enter your year of birth :\n"))
print(name,"your age should be",(curr_year-Year_of_birth-1),"\n")